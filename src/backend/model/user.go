package model

import (
	"backend/config"
	"backend/debug"
	"crypto/md5"
	"encoding/json"
	"errors"
	"fmt"
	"github.com/garyburd/redigo/redis"
	"github.com/jinzhu/gorm"
	"log"
)

type User struct {
	gorm.Model
	Name   string `gorm:"unique;not null;index"`
	Passwd string `gorm:"not null" json:"-"`
	Role   int    `gorm:"not null"`
	Status int 	  `gorm:"not null"`
}

func (user User) CheckPasswd(passwd string) bool {
	return user.Passwd == user.EncryptPasswd(passwd)
}

func (user User) validPasswd(passswd string) bool {
	if passswd == "" {
		return false
	}
	return true
}

// password md5 加密
func (user User) EncryptPasswd(passwd string) (hashPasswd string) {
	if !user.validPasswd(passwd) {
		dbg.Dbg("password is not valid")
	}

	salt := config.AllConfig.Server.Salt
	p := salt + passwd
	hashPasswd = fmt.Sprintf("%x", md5.Sum([]byte(p)))
	return hashPasswd
}

// user session token
func (user User) GetSessionToken() (string, error) {
	salt := config.AllConfig.Server.Salt
	//str := fmt.Sprintf("%s user %d %s %d", salt, user.ID, user.Name, time.Now().Unix())

	str := fmt.Sprintf("%s user %d %s", salt, user.ID, user.Name)
	token := fmt.Sprintf("%x", md5.Sum([]byte(str)))
	return token, nil
}

// token: userId to redis
func SaveTokenToRedis(token string, userId uint) error {
	key := fmt.Sprintf("token:%s", token)

	rds := RedisPool.Get()
	defer rds.Close()

	if _, err := rds.Do("SET", key, userId, "EX", UserActiveDuration); err != nil {
		log.Println(err)
		return err
	}

	return nil
}

// token: userId from redis
func GetUserIdByToken(token string) (uint, error) {
	key := fmt.Sprintf("token:%s", token)

	rds := RedisPool.Get()
	defer rds.Close()

	userId, err := redis.Uint64(rds.Do("GET", key))
	if err != nil {
		log.Println(err)
		return 0, err
	}

	return uint(userId), nil
}



// user info to redis
func SaveUserToRedis(user User) error {
	userKey := fmt.Sprintf("user:%d", user.ID)
	userJson, err := json.Marshal(&user)
	if err != nil {
		log.Println(err)
		return err
	}

	rds := RedisPool.Get()
	defer rds.Close()

	if _, err := rds.Do("SET", userKey, userJson, "EX", UserActiveDuration); err != nil {
		log.Println("save user ", user.ID, " to redis error: ", err)
		return err
	}

	return nil
}

func GetUserFromRedis(userId uint) (User, error) {
	userKey := fmt.Sprintf("user:%d", userId)
	rds := RedisPool.Get()
	defer rds.Close()

	info, err := redis.Bytes(rds.Do("GET", userKey))
	if err != nil {
		log.Println("get user info from redis error, id: ", userId)
		return User{}, errors.New("not login")
	}

	var user User
	if err = json.Unmarshal(info, &user); err != nil {
		log.Println(err)
		return User{}, errors.New("not login")
	}

	return user, nil
}

const (
	UserRoleAdmin  = 1
	UserRoleNormal = 2
)

const (
	UserStatusActive = 1
	UserStatusDelete = 2
)

const (
	//UserActiveDuration = 24 * 60 * 60
	UserActiveDuration = 10 * 60
)

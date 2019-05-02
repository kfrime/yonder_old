package middleware

import (
	"backend/api"
	"backend/config"
	"backend/model"
	"errors"
	"github.com/gin-gonic/gin"
	"log"
)

func getUser(c *gin.Context) (model.User, error)  {
	var user model.User
	token := c.GetHeader("token")
	if token == "" {
		log.Println("token err")
		return user, errors.New("token err")
	}

	userId, err := model.GetUserIdByToken(token)
	if err != nil {
		log.Println(err)
		return user, err
	}

	user, err = model.GetUserFromRedis(userId)
	if err != nil {
		log.Println(err)
		return user, err
	}
	
	return user, nil
}

func LoginRequired(c *gin.Context) {
	// todo: 后续可以通过 jwt 验证
	user, err := getUser(c)
	if err != nil {
		api.SendErrResp(c, "not login")
		return
	}

	c.Set("user", user)
	c.Next()
}

func AdminRequired(c *gin.Context) {
	user, err := getUser(c)
	if err != nil {
		api.SendErrResp(c, "not login")
		return
	}

	adminName := config.AllConfig.Admin.Name
	if user.Role != model.UserRoleAdmin && user.Name == adminName {
		api.SendErrResp(c, "permission denied")
		return
	}

	c.Set("user", user)
	c.Set("admin", user)
	c.Next()
}

// blog server main 

package main

import (
	"backend/model"
	"backend/router"
	"github.com/gin-gonic/gin"
)

func testUser()  {
	db := model.DB

	db.AutoMigrate(&model.User{})

	// 创建
	db.Create(&model.User{Name: "jack"})

	// 读取
	var user model.User
	db.First(&user, 1)
	db.First(&user, "name = ?", "jack")

	// 更新
	db.Model(&user).Update("Name", "bingo")

	// 删除
	db.Delete(&user)
}

func main() {
	//testUser()

	// Creates a router without any middleware by default
	app := gin.New()

	// Global middleware
	// Logger middleware will write the logs to gin.DefaultWriter even if you set with GIN_MODE=release.
	// By default gin.DefaultWriter = os.Stdout
	app.Use(gin.Logger())

	// Recovery middleware recovers from any panics and writes a 500 if there was one.
	app.Use(gin.Recovery())

	router.Route(app)

	app.Run(":6060")
}


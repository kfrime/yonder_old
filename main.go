// blog server main 

package main

import (
	"backend/model"
	"backend/router"
	"github.com/gin-gonic/gin"
)

func migrate()  {
	db := model.DB

	db.AutoMigrate(&model.User{})
	db.AutoMigrate(&model.Category{})
	db.AutoMigrate(&model.Article{})
}

func main() {
	// create table
	migrate()

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


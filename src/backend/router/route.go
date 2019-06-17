package router

import (
	"backend/api"
	"backend/middleware"
	"github.com/gin-gonic/gin"
)

func Route(router *gin.Engine)  {
	apiGrp := router.Group("/api")

	// 用户
	apiGrp.GET("/user/info", middleware.LoginRequired, api.UserInfo)
	apiGrp.GET("/user/signout", middleware.LoginRequired, api.SignOut)
	apiGrp.POST("/user/signup", api.Signup)
	apiGrp.POST("/user/login", api.Login)
	apiGrp.POST("/user/password/update", middleware.LoginRequired, api.ResetPasswd)

	// 分类
	apiGrp.POST("/category", middleware.AdminRequired, api.CateCreate)
	apiGrp.PUT("/category/:cateId", middleware.AdminRequired, api.CateUpdate)
	apiGrp.DELETE("/category/:cateId", middleware.AdminRequired, api.CateDestroy)
	apiGrp.GET("/category/:cateId", api.CateRetrieve)
	apiGrp.GET("/categories", api.CateList)

	// 文章
	apiGrp.POST("/article", middleware.AdminRequired, api.ArticleCreate)
	apiGrp.PUT("/article/:id", middleware.AdminRequired, api.ArticleUpdate)
	apiGrp.DELETE("/article/:id", middleware.AdminRequired, api.ArticleDestroy)
	apiGrp.GET("/article/:id", api.ArticleRetrieve)
	apiGrp.GET("/articles", api.ArticleList)

	// 搜索
	apiGrp.GET("/search", api.SearchArticle)
}

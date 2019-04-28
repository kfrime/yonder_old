package api

import (
	"backend/model"
	"github.com/gin-gonic/gin"
)

func ArticleList(c *gin.Context)  {
	// todo: page and limit
	// todo: filter by cateId
	type ArticleSerialize struct {
		model.Article
		UserId 		uint
		UserName 	uint
	}

	//val, _ := c.Get("user")		// interface{}
	//user := val.(model.User)


	//sql := `
	//SELECT * FROM articles a INNER JOIN users u ON a.userId = u.id `


}

func ArticleRetrieve(c *gin.Context)  {

}

func ArticleCreate(c *gin.Context)  {
	val, _ := c.Get("user")		// interface{}
	user := val.(model.User)



	SendResp(c, gin.H{
		"user": user,
	})
}

func ArticleUpdate(c *gin.Context)  {

}

func ArticleDestroy(c *gin.Context)  {

}

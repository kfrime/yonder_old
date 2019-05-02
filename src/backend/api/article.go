package api

import (
	"backend/model"
	"github.com/gin-gonic/gin"
	"log"
	"strconv"
)

type ArticleDetail struct {
	model.Article
	User model.User
}

func ArticleList(c *gin.Context)  {
	// todo: page and limit
	// todo: filter by cateId

	//val, _ := c.Get("user")		// interface{}
	//user := val.(model.User)

	//sql := `
	//SELECT * FROM articles a INNER JOIN users u ON a.userId = u.id `
}

func ArticleRetrieve(c *gin.Context)  {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		log.Println(err)
		SendErrResp(c, "invalid article id")
		return
	}

	//var ac model.Article
	var ad ArticleDetail

	err = model.DB.Where("id = ?", id).Find(&ad.Article).Error
	if err != nil {
		log.Println(err)
		SendErrResp(c, "article not existed")
		return
	}

	err = model.DB.Where("id = ?", ad.Article.UserId).Find(&ad.User).Error
	if err != nil {
		log.Println(err)
		SendErrResp(c, "article author not existed")
		return
	}

	SendResp(c, gin.H{
		"ad": ad,
	})
}

func ArticleCreate(c *gin.Context)  {
	val, _ := c.Get("user")		// interface{}
	user := val.(model.User)

	var ac model.Article
	if err := c.ShouldBindJSON(&ac); err != nil {
		log.Println(err)
		SendErrResp(c, "输入有误，请检查")
		return
	}
	ac.UserId = user.ID

	if err := ac.Create(); err != nil {
		SendErrResp(c, err.Error())
		return
	}

	SendResp(c, gin.H{})
}

func ArticleUpdate(c *gin.Context)  {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		log.Println(err)
		SendErrResp(c, "invalid article id")
		return
	}

	val, _ := c.Get("user")		// interface{}
	user := val.(model.User)

	var ac model.Article
	if err := c.ShouldBindJSON(&ac); err != nil {
		log.Println(err)
		SendErrResp(c, "输入有误，请检查")
		return
	}
	ac.UserId = user.ID

	if err := ac.Update(id); err != nil {
		SendErrResp(c, err.Error())
		return
	}

	// todo: 获取文章详情，是否可以优化
	ArticleRetrieve(c)
	//SendResp(c, gin.H{
	//	"ac": ac,
	//})
}

func ArticleDestroy(c *gin.Context)  {

}

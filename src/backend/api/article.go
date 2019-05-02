package api

import (
	"backend/model"
	"github.com/gin-gonic/gin"
	"log"
	"strconv"
	"time"
)

// for article list
type SimpleArticle struct {
	ID        uint
	CreatedAt time.Time
	UpdatedAt time.Time
	Title 	  string
	UserId 	  uint
	Username  string
	CateId 	  uint
	CateName  string
}

// for article retrieve
type ArticleDetail struct {
	model.Article
	User model.User
}

func ArticleList(c *gin.Context)  {
	// todo: page and limit
	// todo: filter by cateId

	var al []SimpleArticle

	var sql = `
	SELECT a.id, a.title, a.created_at, a.updated_at, a.user_id, b.name as username, a.cate_id, c.name
	FROM articles a INNER JOIN users b ON a.user_id = b.id 
	INNER JOIN categories c ON a.cate_id = c.id
	WHERE a.deleted_at IS NULL AND b.deleted_at IS NULL AND c.deleted_at IS NULL;`

	if err := model.DB.Raw(sql).Scan(&al).Error; err != nil {
		log.Println(err)
		SendErrResp(c, "can not get article list")
		return
	}

	SendResp(c, gin.H{
		"al": al,
	})
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
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		log.Println(err)
		SendErrResp(c, "invalid article id")
		return
	}

	var ac model.Article
	err = model.DB.First(&ac, "id = ?", id).Error
	if err != nil {
		log.Println(err)
		SendErrResp(c, "article not existed")
		return
	}

	if err := model.DB.Delete(&ac).Error; err != nil {
		log.Println(err)
		SendErrResp(c, "delete article error")
		return
	}

	SendResp(c, gin.H{})
}

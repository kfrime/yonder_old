package api

import (
	"backend/model"
	"errors"
	"fmt"
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
	Username  string		// sql field: username
	CateId 	  uint			// sql field: cate_id
	CateName  string 		// sql field: cate_name
}

// for article retrieve
type ArticleDetail struct {
	model.Article
	User model.User
	Category model.Category
}

func GetArticleDetail(id uint) (ArticleDetail, error) {
	//var ac model.Article
	var err error
	var ad ArticleDetail

	err = model.DB.Where("id = ?", id).Find(&ad.Article).Error
	if err != nil {
		log.Println(err)
		return ad, errors.New("article not existed")
	}

	// 作者
	err = model.DB.Where("id = ?", ad.Article.UserId).Find(&ad.User).Error
	if err != nil {
		log.Println(err)
		return ad, errors.New("article author not existed")
	}

	// 分类
	err = model.DB.Where("id = ?", ad.Article.CateId).Find(&ad.Category).Error
	if err != nil {
		log.Println(err)
		return ad, errors.New("article category not existed")
	}

	return ad, nil
}

func ArticleList(c *gin.Context)  {
	// todo: page and limit
	// todo: filter by cateId

	var cateId int
	var err error
	var al []SimpleArticle

	cateIdStr := c.Query("cateId")
	if cateIdStr == "" {
		cateId = 0
	} else if cateId, err = strconv.Atoi(cateIdStr); err != nil {
		log.Println(err)
		SendErrResp(c, "cate id is not valid")
		return
	}

	var cate model.Category
	if cateId != 0 && model.DB.First(&cate, cateId).Error != nil {
		SendErrResp(c, "cate id is not valid")
		return
	}

	// 不传cateId参数呢？

	var sql = `
	SELECT a.id, a.title, a.created_at, a.updated_at, a.user_id, b.name as username, 
	a.cate_id, c.name as cate_name
	FROM articles a 
	INNER JOIN users b ON a.user_id = b.id 
	INNER JOIN categories c ON a.cate_id = c.id
	WHERE a.deleted_at IS NULL AND b.deleted_at IS NULL AND c.deleted_at IS NULL`

	if cateId != 0 {
		sql += fmt.Sprintf(` AND c.id = %d`, cateId)
	}

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

	ad, err := GetArticleDetail(uint(id))
	if err != nil {
		SendErrResp(c, err.Error())
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

	//SendResp(c, gin.H{})
	ad, err := GetArticleDetail(ac.ID)
	if err != nil {
		SendErrResp(c, err.Error())
		return
	}

	SendResp(c, gin.H{
		"ad": ad,
	})
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
	//ArticleRetrieve(c)
	ad, err := GetArticleDetail(uint(id))
	if err != nil {
		SendErrResp(c, err.Error())
		return
	}

	SendResp(c, gin.H{
		"ad": ad,
	})
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

package api

import (
	"backend/model"
	"fmt"
	"github.com/gin-gonic/gin"
	"log"
)

func SearchArticle(c *gin.Context)  {
	q := c.Query("q")
	// add % to q
	fq := fmt.Sprintf("%%%s%%", q)
	var al []SimpleArticle

	var sql = `
	SELECT a.id, a.title, a.created_at, a.updated_at, a.user_id, b.name as username, 
	a.cate_id, c.name as cate_name
	FROM articles a 
	INNER JOIN users b ON a.user_id = b.id 
	INNER JOIN categories c ON a.cate_id = c.id
	WHERE a.deleted_at IS NULL AND b.deleted_at IS NULL AND c.deleted_at IS NULL
	AND a.title like ?`

	if err := model.DB.Raw(sql, fq).Scan(&al).Error; err != nil {
		log.Println(err)
		SendErrResp(c, "can not get article list")
		return
	}

	SendResp(c, gin.H{
		"al": al,
	})
}

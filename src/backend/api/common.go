package api

import (
	"github.com/gin-gonic/gin"
	"github.com/microcosm-cc/bluemonday"

	"net/http"
)

type errCode struct {
	SUCCESS int
	ERROR 	int
}

var ErrCode = errCode{
	SUCCESS: 0,
	ERROR: 	 1,
}


func SendErrResp(c *gin.Context, msg string, args ...interface{})  {

	var errNo = ErrCode.ERROR
	if len(args) != 0 {
		errNum, ok := args[0].(int)
		if !ok {
			panic("errNo error!")
		}
		errNo = errNum
	}

	c.JSON(http.StatusOK, gin.H{
		"errNo": errNo,
		"msg": msg,
		"data": gin.H{},
	})

	c.Abort()
}

// It protects sites from XSS attacks
func preventXSS(input string) string {
	return bluemonday.UGCPolicy().Sanitize(input)
}

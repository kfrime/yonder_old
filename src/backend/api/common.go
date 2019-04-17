package api

import (
	"bytes"
	"encoding/gob"
	"github.com/gin-gonic/gin"
	"github.com/microcosm-cc/bluemonday"
	"log"

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

func SendResp(c *gin.Context, data gin.H) {
	c.JSON(http.StatusOK, gin.H{
		"code": ErrCode.SUCCESS,
		"msg": "success",
		"data": data,
	})
}


// args: errNo, ...
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
		"code": errNo,
		"msg": msg,
		"data": gin.H{},
	})

	c.Abort()
}

// It protects sites from XSS attacks
func preventXSS(input string) string {
	return bluemonday.UGCPolicy().Sanitize(input)
}

// Clone deep-copies src to dst
// src, dst must be pointer
func Deepcopy(src, dst interface{}) error {

	//buff := new(bytes.Buffer)
	var buff bytes.Buffer
	enc := gob.NewEncoder(&buff)
	dec := gob.NewDecoder(&buff)
	if err := enc.Encode(src); err != nil {
		log.Print(err)
		return err
	}
	if err := dec.Decode(dst); err != nil {
		log.Print(err)
		return err
	}
	return nil
}

package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"github.com/julienschmidt/httprouter"
	"net/http"
)

type Topic struct {
	Id 		int 	`json:"id"`
	Title 	string 	`json:"title"`
}

var Db *sql.DB

func addTopic(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
	len := r.ContentLength
	body := make([]byte, len)
	r.Body.Read(body)
	defer r.Body.Close()

	var topic Topic
	json.Unmarshal(body, &topic)

	//fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
	fmt.Fprintf(w, "%q", topic)
}

func getTopicList(w http.ResponseWriter, r *http.Request, p httprouter.Params)  {

}

func initRoutes() *httprouter.Router {
	mux := httprouter.New()

	mux.GET("/topic", getTopicList)
	mux.POST("/topic", addTopic)

	return mux
}

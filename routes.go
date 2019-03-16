package main

import (
	"net/http"
	"fmt"
	"github.com/julienschmidt/httprouter"
)

func index(w http.ResponseWriter, r *http.Request, p httprouter.Params)  {
	fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
}

func hello(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
	fmt.Fprintf(w, "hello, %s!\n", p.ByName("name"))
}

func initRoutes() *httprouter.Router {
	mux := httprouter.New()

	mux.GET("/", index)
	mux.GET("/hello/:name", hello)

	return mux
}

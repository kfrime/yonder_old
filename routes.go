package main

import (
	"fmt"
	"github.com/julienschmidt/httprouter"
	"net/http"
)

func index(w http.ResponseWriter, r *http.Request, p httprouter.Params)  {
	fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
}

func hello(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
	fmt.Fprintf(w, "hello, %s!\n", p.ByName("name"))
}

func redirect(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
	w.Header().Set("Location", "http://www.google.com")
	w.WriteHeader(302)
}

func setCookie(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
	c := http.Cookie{
		Name: "first",
		Value: "hello world",
		HttpOnly: true,
	}
	w.Header().Add("Set-Cookie", c.String())
	fmt.Fprintf(w, "hello cookie")
}

func initRoutes() *httprouter.Router {
	mux := httprouter.New()

	mux.GET("/", index)
	mux.GET("/hello/:name", hello)
	mux.GET("/redirect", redirect)
	mux.GET("/cookie", setCookie)

	return mux
}

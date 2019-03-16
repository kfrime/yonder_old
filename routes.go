package main

import (
	"net/http"
	"fmt"
)

func index(w http.ResponseWriter, r *http.Request)  {
	fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
}

func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "hello world")
}

func initRoutes() *http.ServeMux {
	mux := http.NewServeMux()

	mux.HandleFunc("/", index)
	mux.HandleFunc("/hello", hello)

	return mux
}

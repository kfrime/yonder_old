package main

import (
	"net/http"
	"fmt"
)

func index(w http.ResponseWriter, r *http.Request)  {
	fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
}

func initRoutes() *http.ServeMux {
	mux := http.NewServeMux()

	mux.HandleFunc("/", index)

	return mux
}

// blog server main 

package main

import (
	"net/http"
	"fmt"
	"log"
)

func index(w http.ResponseWriter, r *http.Request)  {
	fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
}

func main()  {
	http.HandleFunc("/", index)
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}

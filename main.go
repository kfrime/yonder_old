// blog server main 

package main

import (
	"backend/config"
	"backend/model"
	"fmt"
	"github.com/julienschmidt/httprouter"
	"net/http"
)

func serverStart(mux *httprouter.Router)  {
	srv := &http.Server{
		Addr: "localhost:8080",
		Handler: mux,
	}

	fmt.Println("server start at: ", srv.Addr)
	srv.ListenAndServe()
}

func main()  {
	config.InitConf()
	model.MigrateModels()
	//mux := route.InitRoutes()
	//serverStart(mux)
}

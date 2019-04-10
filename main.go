// blog server main 

package main

import (
	"backend/config"
	"backend/debug"
	"backend/model"
	"backend/route"
	"fmt"
	"github.com/julienschmidt/httprouter"
	"net/http"
)

func serverStart(mux *httprouter.Router)  {
	srv := &http.Server{
		Addr: "localhost:8080",
		Handler: mux,
	}

	fmt.Println("\nserver start at: ", srv.Addr)
	srv.ListenAndServe()
}

func testCreateModel()  {
	model.DB.AutoMigrate(&model.User{})
}

func testOptModel()  {
	user := model.User{Name:"jack"}
	dbg.Dbg(user)
	model.DB.Create(&user)
	dbg.Dbg(user)
}

func main() {
	//testCreateModel()
	testOptModel()
}

func _main()  {
	config.InitConf()
	//model.MigrateModels()
	//model.TestModelData()
	mux := route.InitRoutes()
	serverStart(mux)
}

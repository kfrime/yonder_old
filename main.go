// blog server main 

package main

import (
	"backend/config"
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

func testUser()  {
	db := model.DB

	db.AutoMigrate(&model.User{})

	// 创建
	db.Create(&model.User{Name: "jack"})

	// 读取
	var user model.User
	db.First(&user, 1)
	db.First(&user, "name = ?", "jack")

	// 更新
	db.Model(&user).Update("Name", "bingo")

	// 删除
	db.Delete(&user)
}

func main() {
	testUser()
}

func _main()  {
	config.InitConf()
	//model.MigrateModels()
	//model.TestModelData()
	mux := route.InitRoutes()
	serverStart(mux)
}

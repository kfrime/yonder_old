package api

import (
	"backend/model"
	"encoding/json"
	"fmt"
	"github.com/julienschmidt/httprouter"
	"net/http"
	"strconv"
)

func GetUser(w http.ResponseWriter, r *http.Request, p httprouter.Params)  {
	var none = []byte("{}")
	id, err := strconv.Atoi(p.ByName("id"))
	if err != nil {
		fmt.Println(err.Error())
		w.Write(none)
		return
	}
	user, err := model.Retrieve(id)
	if err != nil {
		fmt.Println(err.Error())
		w.Write(none)
		return
	}
	output, err := json.MarshalIndent(&user, "", "\t\t")
	if err != nil {
		w.Write(none)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(output)
	return
}


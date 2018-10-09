package main

import (
	"encoding/json"
	"net/http"
)

type Response struct {
	Code int         `json:"code"`
	Type string      `json:"type"`
	Data interface{} `json:"data"`
}

func createResponse(_writer http.ResponseWriter, _code int, _type string, _content interface{}) {
	Response := Response{_code, _type, _content}

	json, err := json.Marshal(Response)
	if err != nil {
		http.Error(_writer, err.Error(), http.StatusInternalServerError)
		return
	}

	_writer.Header().Set("Content-Type", "application/json")
	_writer.WriteHeader(_code)
	_writer.Write(json)
}

func createErrorResponse(w http.ResponseWriter, code int, content interface{}) {
	createResponse(w, code, "error", content)
}

func createSuccessResponse(w http.ResponseWriter, code int, content interface{}) {
	createResponse(w, code, "success", content)
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	var file string = "./" + r.URL.Path[1:]
	http.ServeFile(w, r, file)
}

func getHandler(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query()["name"][0]

	if len(name) < 1 {
		createErrorResponse(w, http.StatusBadRequest, "'Name' parameter was not informed")
		return
	}

	createSuccessResponse(w, http.StatusOK, "Hello "+name)
}

func postHandler(w http.ResponseWriter, r *http.Request) {
	name := r.FormValue("name")

	if len(name) < 1 {
		createErrorResponse(w, http.StatusBadRequest, "'Name' parameter was not informed")
		return
	}

	createSuccessResponse(w, http.StatusOK, "Hello "+name)
}

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/get", getHandler)
	http.HandleFunc("/post", postHandler)
	http.ListenAndServe(":8080", nil)
}

package main

//char* get_msg(){
//  return "Hello, GO!";
//}
import "C"
import "fmt"

func main() {
    var msg = C.get_msg()
    fmt.Println(C.GoString(msg))
}

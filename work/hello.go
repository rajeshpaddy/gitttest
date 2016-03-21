package main
import(
"bufio"
"os"
"fmt"
)

func main(){
	h:=os.Args[1]
	f,_ := os.Open(h)
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)
	for scanner.Scan(){
		line:=scanner.Text()
		fmt.Println(line)
	}
fmt.Printf("%s \n",h)
}

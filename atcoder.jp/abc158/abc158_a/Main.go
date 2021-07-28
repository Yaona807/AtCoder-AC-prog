package main

import (
	"fmt"
	"strings"
)

func main() {
	var s, ans string
	fmt.Scan(&s)

	if strings.Contains(s, "A") && strings.Contains(s, "B") {
		ans = "Yes"
	} else {
		ans = "No"
	}

	fmt.Printf(ans)
}

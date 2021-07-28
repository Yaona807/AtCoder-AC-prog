package main

import (
	"fmt"
)

func main() {
	var n, r, ans int
	fmt.Scan(&n, &r)
	ans = r
	if n < 10 {
		ans += 100 * (10 - n)
	}

	fmt.Print(ans)

}

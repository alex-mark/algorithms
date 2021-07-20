package main

import "fmt"

func main() {
	fmt.Println("hello")

	var x int = 2
	// y  := 3
	// var sum = x + y

	if x > 6 {
		fmt.Println("More than 6")
	} else {
		fmt.Println("Less than 6")
	}

	a := [5]int{5, 4, 3, 2, 1} // array
	b := []int{5, 4, 3, 2, 1} // slice
	b = append(b, 13)

	a[2] = 7
	fmt.Println(a, b)

	vertices := make( map[string]int )

	vertices["triangle"] = 2
	vertices["square"] = 3

	fmt.Println(vertices)

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	for index, value := range a {
		fmt.Println(index, value)
	}

	res := sum(2, 5)
	fmt.Println(res)

	// p := person{name: "John", age: 25}

}

func sum(x int, y int) int {
	return x + y
}

type person struct {
	name string
	age int
}
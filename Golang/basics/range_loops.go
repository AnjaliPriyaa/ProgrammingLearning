package basics

import "fmt"

/*
RANGE LOOPS: Iterate over collections (arrays, slices, maps, strings)
- for...range: Special loop syntax for iterating
- Arrays/Slices: Returns index and value
- Maps: Returns key and value
- Strings: Returns index and rune (character)
- Use _ to ignore index/key if not needed
*/

// DemoRangeLoops shows how to iterate over collections using range
func DemoRangeLoops() {
	fmt.Println("\n--- Range Loops ---")

	// Range over slice
	fmt.Println("Range over slice:")
	numbers := []int{10, 20, 30, 40, 50}
	for index, value := range numbers {
		fmt.Printf("Index: %d, Value: %d\n", index, value)
	}

	// Range with only values (ignore index)
	fmt.Println("\nRange with only values:")
	for _, value := range numbers {
		fmt.Printf("Value: %d\n", value)
	}

	// Range over array
	fmt.Println("\nRange over array:")
	intArr := [5]int{1, 2, 3, 4, 5}
	for i, val := range intArr {
		fmt.Printf("Index: %d, Value: %d\n", i, val)
	}

	// Range over map
	fmt.Println("\nRange over map:")
	myMap := map[string]int{"one": 1, "two": 2, "three": 3}
	for key, value := range myMap {
		fmt.Printf("Key: %s, Value: %d\n", key, value)
	}

	// Range over string (iterates by rune/character)
	fmt.Println("\nRange over string:")
	str := "Go!"
	for i, char := range str {
		fmt.Printf("Index: %d, Character: %c\n", i, char)
	}
}

package collections

import "fmt"

/*
ARRAYS: Fixed-size collection of elements of the same type.
- Size is part of the type [5]int vs [10]int are different types
- Cannot change size after creation

SLICES: Dynamic-size, flexible view into arrays.
- More common than arrays in Go
- Can grow/shrink using append()
- len(): current number of elements
- cap(): underlying capacity
*/

// DemoArrays shows how to work with fixed-size arrays
func DemoArrays() {
	fmt.Println("\n=== 3. COLLECTIONS: Arrays ===")

	// Fixed-size array
	intArr := [5]int{1, 2, 3, 4, 5}
	fmt.Println("Array:", intArr)

	// Dynamic size array (compiler counts elements)
	intarrrr := [...]int32{10, 20, 30, 40, 50}
	fmt.Println("Dynamic array:", intarrrr)
}

// DemoSlices shows how to work with dynamic slices
func DemoSlices() {
	fmt.Println("\n=== 4. COLLECTIONS: Slices ===")

	var slice1 []int = []int{100, 200, 300}
	fmt.Println("Slice:", slice1)
	fmt.Println("Length of slice1:", len(slice1))
	fmt.Println("Capacity of slice1:", cap(slice1))

	// Appending elements
	slice1 = append(slice1, 400, 500)
	fmt.Println("After append:", slice1)
	fmt.Println("Length of slice1:", len(slice1))
	fmt.Println("Capacity of slice1:", cap(slice1))

	// Slicing
	fmt.Println("Slice from index 1 to 3:", slice1[1:4])
	// fmt.Println(slice1[5]) // Would cause panic: index out of range
}

package basics

import "fmt"

/*
GENERICS: Write ONE function that works with MANY types.

Real-life example:
- A box that can hold ANYTHING (toys, books, clothes)
- You don't need a separate box for each item type!

Syntax:
- [T any] means "T can be any type"
- Think of T as a placeholder that gets replaced

Without Generics:
func PrintInt(x int)       { fmt.Println(x) }
func PrintString(x string) { fmt.Println(x) }
func PrintFloat(x float64) { fmt.Println(x) }

With Generics:
func Print[T any](x T)     { fmt.Println(x) }  // ONE function!
*/

// DemoGenerics demonstrates generics with simple examples
func DemoGenerics() {
	fmt.Println("\n--- GENERICS (One Code, Many Types) ---")

	// Example 1: ONE function works with ANY type
	fmt.Println("\n--- Example 1: Generic Print ---")

	Print(42)      // Works with int
	Print("Hello") // Works with string
	Print(3.14)    // Works with float
	Print(true)    // Works with bool

	// Example 2: Generic function returns first element
	fmt.Println("\n--- Example 2: Get First Element ---")

	numbers := []int{10, 20, 30}
	words := []string{"Go", "is", "fun"}

	fmt.Println("First number:", First(numbers)) // 10
	fmt.Println("First word:", First(words))     // Go

	// Example 3: Generic "box" that holds any type
	fmt.Println("\n--- Example 3: Generic Box ---")

	// Box for integer
	intBox := Box[int]{Value: 100}
	fmt.Println("Int box contains:", intBox.Value)

	// Box for string (same Box code!)
	stringBox := Box[string]{Value: "treasure"}
	fmt.Println("String box contains:", stringBox.Value)

	// Example 4: Swap any two values
	fmt.Println("\n--- Example 4: Swap Values ---")

	a, b := 5, 10
	fmt.Printf("Before: a=%d, b=%d\n", a, b)
	a, b = Swap(a, b)
	fmt.Printf("After: a=%d, b=%d\n", a, b)

	x, y := "cat", "dog"
	fmt.Printf("Before: x=%s, y=%s\n", x, y)
	x, y = Swap(x, y)
	fmt.Printf("After: x=%s, y=%s\n", x, y)

	fmt.Println("\nGenerics completed!")
}

// Print prints any value
// [T any] means "T can be any type"
func Print[T any](value T) {
	fmt.Printf("  %v\n", value)
}

// First returns first element from any slice
func First[T any](slice []T) T {
	if len(slice) == 0 {
		var empty T // Return empty value if slice is empty
		return empty
	}
	return slice[0]
}

// Box can hold any type of value
// Like a container that works for anything
type Box[T any] struct {
	Value T
}

// Swap exchanges two values (works with any type)
func Swap[T any](a, b T) (T, T) {
	return b, a
}

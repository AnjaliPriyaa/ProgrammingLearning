package basics

import (
	"fmt"
	"unicode/utf8"
)

/*
VARIABLES: Named storage for data that can change during program execution.
TYPES: Define what kind of data a variable can hold (int, float64, string, bool, etc.)
- var keyword: explicit variable declaration with type
- := shorthand: declares and initializes variable (type inferred)
*/

// DemoVariablesAndTypes shows basic variable declarations and primitive types
func DemoVariablesAndTypes() {
	fmt.Println("\n=== 1. BASICS: Variables and Types ===")

	// Integer types
	var intNUM int = 32767
	intNUM = 32767 + 1
	fmt.Println("Integer after overflow:", intNUM)

	// Float types
	var floatNum float64 = 3.14
	fmt.Println("Float:", floatNum)

	// String types
	var mystring string = "Hello, Go!"
	fmt.Println("String:", mystring)
	fmt.Println("String length (rune count):", utf8.RuneCountInString("y"))

	// Boolean types
	var myBoolean bool = true
	fmt.Println("Boolean:", myBoolean)

	// Short declaration (type inference)
	mystr := "Short declaration"
	fmt.Println("Short declaration:", mystr)

	// Multiple variable declaration
	var1, var2, var3 := 1, 2, "three"
	fmt.Println("Multiple variables:", var1, var2, var3)
}

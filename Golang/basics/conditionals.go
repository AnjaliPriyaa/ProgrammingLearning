package basics

import "fmt"

/*
CONDITIONALS: Control flow statements that execute code based on conditions.
- if/else: Execute code if condition is true, otherwise execute else block
- switch: Compare a value against multiple cases
- Conditions evaluate to boolean (true/false)
*/

// DemoConditionals demonstrates if-else statements and switch cases in Go
func DemoConditionals() {

	// Basic if-else
	age := 20
	if age >= 18 {
		fmt.Println("You are an adult")
	} else {
		fmt.Println("You are a minor")
	}

	// If with initialization statement
	if score := 85; score >= 90 {
		fmt.Println("Grade: A")
	} else if score >= 80 {
		fmt.Println("Grade: B")
	} else if score >= 70 {
		fmt.Println("Grade: C")
	} else {
		fmt.Println("Grade: D")
	}

	// Switch statement
	day := 3
	switch day {
	case 1:
		fmt.Println("Monday")
	case 2:
		fmt.Println("Tuesday")
	case 3:
		fmt.Println("Wednesday")
	case 4:
		fmt.Println("Thursday")
	case 5:
		fmt.Println("Friday")
	case 6, 7:
		fmt.Println("Weekend")
	default:
		fmt.Println("Invalid day")
	}

	// Switch with no condition (like if-else chain)
	temperature := 25
	switch {
	case temperature < 0:
		fmt.Println("Freezing!")
	case temperature < 15:
		fmt.Println("Cold")
	case temperature < 25:
		fmt.Println("Moderate")
	default:
		fmt.Println("Hot")
	}
}

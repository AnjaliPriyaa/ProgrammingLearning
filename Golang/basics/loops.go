package basics

import "fmt"

/*
FOR LOOPS: Basic loop constructs in Go
- for: Standard C-style loop with initialization, condition, increment
- while-style: Just condition (no init/increment)
- infinite: No condition (use break to exit)
- break: Exit loop early
- continue: Skip to next iteration
*/

// DemoLoops demonstrates basic for and while-style loops
func DemoLoops() {
	fmt.Println("\n--- For & While Loops ---")

	// Standard for loop
	fmt.Println("Standard for loop:")
	for i := 0; i < 5; i++ {
		fmt.Printf("Iteration %d\n", i)
	}

	// While-style loop (Go has no while keyword, use for)
	fmt.Println("\nWhile-style loop:")
	count := 0
	for count < 3 {
		fmt.Printf("Count: %d\n", count)
		count++
	}

	// Infinite loop with break
	fmt.Println("\nInfinite loop with break:")
	n := 0
	for {
		if n >= 3 {
			break
		}
		fmt.Printf("n = %d\n", n)
		n++
	}

	// Loop with continue
	fmt.Println("\nLoop with continue (skip even numbers):")
	for i := 0; i < 6; i++ {
		if i%2 == 0 {
			continue
		}
		fmt.Printf("Odd number: %d\n", i)
	}
}

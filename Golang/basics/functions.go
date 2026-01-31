package basics

import "fmt"

/*
FUNCTIONS: Reusable blocks of code that perform specific tasks.
- func keyword: Declare a function
- Parameters: Input values passed to function
- Return values: Output from function (can return multiple values)
- Variadic: Accept variable number of arguments (...type)
*/

// DemoFunctions demonstrates different types of functions in Go
func DemoFunctions() {
	fmt.Println("\n--- Functions ---")

	// Simple function call
	greet()

	// Function with parameters
	greetPerson("Alice")

	// Function with return value
	sum := add(5, 3)
	fmt.Printf("Sum: %d\n", sum)

	// Function with multiple return values
	result, err := divide(10, 2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Printf("Division result: %.2f\n", result)
	}

	// Function with named return values
	area, perimeter := rectangleMeasurements(5, 3)
	fmt.Printf("Area: %d, Perimeter: %d\n", area, perimeter)

	// Variadic function
	total := sumAll(1, 2, 3, 4, 5)
	fmt.Printf("Total sum: %d\n", total)

	// Anonymous function
	multiply := func(a, b int) int {
		return a * b
	}
	fmt.Printf("Multiplication: %d\n", multiply(4, 5))

	// Function as parameter (callback)
	processNumbers([]int{1, 2, 3, 4, 5}, func(n int) int {
		return n * n
	})
}

// greet prints a simple greeting
func greet() {
	fmt.Println("Hello, Go!")
}

// greetPerson greets a specific person
func greetPerson(name string) {
	fmt.Printf("Hello, %s!\n", name)
}

// add returns the sum of two integers
func add(a, b int) int {
	return a + b
}

// divide returns the result of division and an error if division by zero
func divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, fmt.Errorf("cannot divide by zero")
	}
	return a / b, nil
}

// rectangleMeasurements uses named return values
func rectangleMeasurements(length, width int) (area int, perimeter int) {
	area = length * width
	perimeter = 2 * (length + width)
	return // naked return
}

// sumAll is a variadic function that sums all numbers
func sumAll(numbers ...int) int {
	total := 0
	for _, num := range numbers {
		total += num
	}
	return total
}

// processNumbers applies a function to each number in a slice
func processNumbers(nums []int, operation func(int) int) {
	fmt.Print("Processed numbers: ")
	for _, num := range nums {
		fmt.Printf("%d ", operation(num))
	}
	fmt.Println()
}

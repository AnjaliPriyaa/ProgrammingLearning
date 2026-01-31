package basics

import "fmt"

/*
CONSTANTS: Values that cannot be changed after declaration.
- Use 'const' keyword to declare
- Must be assigned at declaration time
- Evaluated at compile time, not runtime
*/

// DemoConstants shows how to work with constants
func DemoConstants() {
	const myConstant = "I am constant"
	// myConstant = "Try to change" // This would cause a compile error
	fmt.Println("Constant value:", myConstant)
	fmt.Println("Constants cannot be changed after declaration")
}

package pointers

import "fmt"

/*
POINTERS: Variable that stores memory address of another variable.
- & operator: Get address of variable (&val)
- * operator: Dereference (get value at address) (*ptr)
- *Type: Pointer type declaration
- Allows functions to modify original values
- nil: Zero value for pointers (no address)
*/

// DemoPointers shows how to work with pointers
func DemoPointers() {
	fmt.Println("\n=== 11. POINTERS: Memory Addresses ===")

	var po *int32
	var val int32 = 42
	po = &val
	fmt.Println("Value of val:", val)
	fmt.Println("Address of val (pointer):", po)
	fmt.Println("Value at address po (dereference):", *po)

	// Modifying value through pointer
	*po = 100
	fmt.Println("After modifying via pointer:")
	fmt.Println("Value of val:", val)
	fmt.Println("Value at address po:", *po)
}

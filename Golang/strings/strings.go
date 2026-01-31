package strings

import (
	"fmt"
	"strings"
)

/*
STRINGS: Sequence of characters (immutable in Go).
- Indexing [i] gives byte value (not character)
- rune: Represents a Unicode character (int32)
- range over string: Iterates by rune, not byte
- strings.Builder: Efficient way to concatenate strings
*/

// DemoStringBasics shows string indexing and iteration
func DemoStringBasics() {
	fmt.Println("\n=== 7. STRINGS: Basics ===")

	var mystring2 = "resume"
	var indexed = mystring2[0]
	fmt.Println("Character at index 0 (byte):", indexed, string(indexed))

	fmt.Println("\nIterating over string (rune by rune):")
	for i, ch := range mystring2 {
		fmt.Printf("  Character %c at index %d\n", ch, i)
	}

	// Using rune slice for proper character access
	var mystring3 = []rune("resume")
	var indexed1 = mystring3[1]
	fmt.Println("\nCharacter at index 1 (rune):", indexed1, string(indexed1))
	for i, ch := range mystring3 {
		fmt.Printf("  Character %c at index %d\n", ch, i)
	}
}

// DemoStringConcatenation shows efficient string concatenation
func DemoStringConcatenation() {
	fmt.Println("\n=== 8. STRINGS: Concatenation ===")

	// Inefficient way (creates new string each iteration)
	var strSlice = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
	var catStr string = ""
	for i := 0; i < len(strSlice); i++ {
		catStr += strSlice[i]
	}
	fmt.Println("Concatenated (inefficient):", catStr)

	// Efficient way using strings.Builder
	var strSlice2 = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
	var strBuilder strings.Builder
	for i := 0; i < len(strSlice2); i++ {
		strBuilder.WriteString(strSlice2[i])
	}
	var catStr2 string = strBuilder.String()
	fmt.Println("Concatenated (efficient):", catStr2)
}

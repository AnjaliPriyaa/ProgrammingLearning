package collections

import "fmt"

/*
MAPS: Collection of key-value pairs (like dictionary/hash table).
- map[KeyType]ValueType syntax
- Keys must be unique
- Use delete() to remove entries
- Check existence: value, exists := myMap[key]
- Unordered collection
*/

// DemoMaps shows how to work with maps (key-value pairs)
func DemoMaps() {
	fmt.Println("\n=== 5. COLLECTIONS: Maps ===")

	var myMap map[string]int = map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
	}
	fmt.Println("Map:", myMap)
	fmt.Println("Value for key 'two':", myMap["two"])

	// Deleting from map
	delete(myMap, "three")
	fmt.Println("Map after deleting key 'three':", myMap)

	// Iterating over map
	fmt.Println("Iterating over map:")
	for name := range myMap {
		fmt.Println("  Key:", name, "Value:", myMap[name])
	}
}

package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {
	// fmt.Println("Hello, World!")
	var intNUM int = 32767
	intNUM = 32767 + 1
	fmt.Println(intNUM)

	var floatNum float64 = 3.14
	fmt.Println(floatNum)

	var mystring string = "Hello, Go!"
	fmt.Println(mystring)

	fmt.Println(utf8.RuneCountInString("y"))

	var myBoolean bool = true
	fmt.Println(myBoolean)

	mystr := "Short declaration"
	fmt.Println(mystr)

	var1, var2, var3 := 1, 2, "three"
	fmt.Println(var1, var2, var3)

	const myConstant = "I am constant"
	// myConstant = "Try to change" -----> can't change constant value
	fmt.Println(myConstant)

	// Function struture
	fmt.Println("Function structure in Go")
	printme()

	intArr := [5]int{1, 2, 3, 4, 5}
	fmt.Println(intArr)

	intarrrr := [...]int32{10, 20, 30, 40, 50} //dynamic array declaration
	fmt.Println(intarrrr)

	var slice1 []int = []int{100, 200, 300}
	fmt.Println(slice1)
	fmt.Println("Length of slice1:", len(slice1))
	fmt.Println("Capacity of slice1:", cap(slice1))
	slice1 = append(slice1, 400, 500)
	fmt.Println(slice1)
	fmt.Println("Length of slice1:", len(slice1))
	fmt.Println("Capacity of slice1:", cap(slice1))
	fmt.Println("Slice from index 1 to 3:", slice1[1:4])
	// fmt.Println(slice1[5]) // Accessing the 6th element (index 5) -> will cause runtime error if not enough elements -> panic: runtime error: index out of range [5] with length 5

	var myMap map[string]int = map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
	}
	fmt.Println(myMap)
	fmt.Println("Value for key 'two':", myMap["two"])
	delete(myMap, "three")
	fmt.Println("Map after deleting key 'three':", myMap)

	for name := range myMap {
		fmt.Println("Key:", name, "Value:", myMap[name])
	}

	for i := 0; i < 5; i++ {
		fmt.Println("Iteration:", i)
	}

	for i, val := range intArr {
		fmt.Println("Index:", i, "Value:", val)
	}

	var mystring2 = "resume"
	var indexed = mystring[0]
	fmt.Println("The character at index 2 is:", indexed, indexed)
	for i, ch := range mystring2 {
		fmt.Printf("Character %c at index %d\n", i, ch)
	}

	var mystring3 = []rune("resume")
	var indexed1 = mystring[1]
	fmt.Println("The character at index 2 is:", indexed1, indexed1)
	for i, ch := range mystring3 {
		fmt.Printf("Character %c at index %d\n", i, ch)
	}

	var strSlice = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
	var catStr string = ""
	for i := 0; i < len(strSlice); i++ {
		catStr += strSlice[i]
	}
	fmt.Println("Concatenated string:", catStr)

	//Uisng Inbuild STrings features to concatenate strings efficiently
	var strSlice2 = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
	var strBuilder strings.Builder
	for i := 0; i < len(strSlice2); i++ {
		strBuilder.WriteString(strSlice2[i])
	}
	var catStr2 string = strBuilder.String()
	fmt.Println("Concatenated string:", catStr2)

	var person1 Person = Person{name: "Alice", age: 30, habit: "Cycling"}
	fmt.Println("Person Name:", person1.name)
	fmt.Println("Person Age:", person1.age)

	var person2 Person = Person{name: "Bob", age: 25, habit: "Reading"}
	fmt.Println("Person Name:", person2.name, person2.habit)
	fmt.Println("Person Age:", person2.age)

	var animal1 Animal = Animal{species: "Dog", age: 5, noise: "Bark"}
	fmt.Println("Animal Species:", animal1.species, animal1.noise)
	fmt.Println("Animal Age:", animal1.age)
	var animal2 Animal = Animal{species: "Cat", age: 3, noise: "Meow"}
	fmt.Println("Animal Species:", animal2.species, animal2.noise)
	fmt.Println("Animal Age:", animal2.age, animal2.noise)

	p := Person{
		name:  "Tom",
		age:   5,
		habit: "drawing",
	}

	a := Animal{
		species: "Dog",
		age:     3,
		noise:   "Woof!",
	}

	makeItSpeak(p)
	makeItSpeak(a)
}

// structs and interfaces
type Person struct {
	name  string
	age   int
	habit string
}

type Animal struct {
	species string
	age     int
	noise   string
}

type Speaker interface {
	Speak() string
}

func (p Person) Speak() string {
	return "Hi, my name is " + p.name
}

func (a Animal) Speak() string {
	return a.noise
}
func makeItSpeak(s Speaker) {
	fmt.Println(s.Speak())
}
func printme() {
	fmt.Println("This is a function")
}

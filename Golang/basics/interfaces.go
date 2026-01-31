package basics

import "fmt"

/*
STRUCTS: Custom types that group related data fields.
INTERFACES: Define behavior (methods) without implementation.
- Any type that implements all interface methods satisfies that interface
- Polymorphism: Different types can be used through same interface
- Empty interface{}: Can hold any type
*/

// Person represents a person with name, age, and habit
type Person struct {
	Name  string
	Age   int
	Habit string
}

// Animal represents an animal with species, age, and noise
type Animal struct {
	Species string
	Age     int
	Noise   string
}

// Speaker interface defines the Speak method
type Speaker interface {
	Speak() string
}

// Speak method for Person (implements Speaker interface)
func (p Person) Speak() string {
	return "Hi, my name is " + p.Name
}

// Speak method for Animal (implements Speaker interface)
func (a Animal) Speak() string {
	return a.Noise
}

// MakeItSpeak takes any Speaker and prints what it says
func MakeItSpeak(s Speaker) {
	fmt.Println(s.Speak())
}

// DemoStructs shows how to create and use structs
func DemoStructs() {
	fmt.Println("\n=== 9. STRUCTS: Creating and Using Structs ===")

	var person1 Person = Person{Name: "Alice", Age: 30, Habit: "Cycling"}
	fmt.Println("Person Name:", person1.Name)
	fmt.Println("Person Age:", person1.Age)

	var person2 Person = Person{Name: "Bob", Age: 25, Habit: "Reading"}
	fmt.Println("Person Name:", person2.Name, person2.Habit)
	fmt.Println("Person Age:", person2.Age)

	var animal1 Animal = Animal{Species: "Dog", Age: 5, Noise: "Bark"}
	fmt.Println("Animal Species:", animal1.Species, animal1.Noise)
	fmt.Println("Animal Age:", animal1.Age)

	var animal2 Animal = Animal{Species: "Cat", Age: 3, Noise: "Meow"}
	fmt.Println("Animal Species:", animal2.Species, animal2.Noise)
	fmt.Println("Animal Age:", animal2.Age, animal2.Noise)
}

// DemoInterfaces shows how to use interfaces for polymorphism
func DemoInterfaces() {
	fmt.Println("\n=== 10. INTERFACES: Polymorphism ===")

	p := Person{
		Name:  "Tom",
		Age:   5,
		Habit: "drawing",
	}

	a := Animal{
		Species: "Dog",
		Age:     3,
		Noise:   "Woof!",
	}

	fmt.Println("Making different types speak:")
	MakeItSpeak(p)
	MakeItSpeak(a)
}

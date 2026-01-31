package main

import (
	"fmt"

	"github.com/AnjaliPriyaa/GolangLearning/basics"
	"github.com/AnjaliPriyaa/GolangLearning/collections"
	"github.com/AnjaliPriyaa/GolangLearning/concurrency"
	"github.com/AnjaliPriyaa/GolangLearning/pointers"
	"github.com/AnjaliPriyaa/GolangLearning/strings"
)

/*
Go Programming Tutorial - From Basics to Advanced

Simple folder structure for easy revision:
- basics/      : Variables, constants, conditionals, loops, functions, structs, interfaces
- collections/ : Arrays, slices, maps
- strings/     : String operations
- pointers/    : Pointers and memory
- concurrency/ : Goroutines, WaitGroup, Mutex, RWMutex
*/

func main() {
	fmt.Println("   Go Programming Tutorial")

	// BASICS
	basics.DemoVariablesAndTypes()
	basics.DemoConstants()
	basics.DemoConditionals()
	basics.DemoLoops()
	basics.DemoRangeLoops()
	basics.DemoFunctions()
	basics.DemoStructs()
	basics.DemoInterfaces()
	basics.DemoGenerics()

	// COLLECTIONS
	collections.DemoArrays()
	collections.DemoSlices()
	collections.DemoMaps()

	// STRINGS
	strings.DemoStringBasics()
	strings.DemoStringConcatenation()

	// POINTERS
	pointers.DemoPointers()

	// CONCURRENCY
	concurrency.DemoConcurrency()
	concurrency.DemoChannels()

	fmt.Println("   Tutorial Complete!")
}

package concurrency

import (
	"fmt"
	"sync"
	"time"
)

/*
GOROUTINE: A lightweight thread managed by Go runtime.
Goroutines allow functions to run concurrently (at the same time) without blocking the main program.
Use 'go' keyword before a function call to run it as a goroutine.

SYNC.WAITGROUP: A counter that waits for a collection of goroutines to finish.
- Add(n): Increments the counter by n
- Done(): Decrements the counter by 1
- Wait(): Blocks until counter becomes 0

MUTEX (LOCK/UNLOCK): Prevents race conditions by ensuring only one goroutine accesses shared data at a time.
- Lock(): Acquires the lock - blocks if another goroutine already has it
- Unlock(): Releases the lock - allows other goroutines to acquire it
- Used to protect shared variables from concurrent access (race conditions)

RWMUTEX (READ-WRITE MUTEX): Allows multiple readers OR one writer (not both).
- RLock(): Acquires read lock - multiple goroutines can read simultaneously
- RUnlock(): Releases read lock
- Lock(): Acquires write lock - exclusive access (no readers or writers)
- Unlock(): Releases write lock
- Use when reads are frequent and writes are rare
*/

// PrintMessage prints a message (used with goroutines)
func PrintMessage(msg string) {
	fmt.Println(msg)
}

// PrintMessageWithWG prints a message and signals completion to WaitGroup
func PrintMessageWithWG(msg string, wg *sync.WaitGroup) {
	defer wg.Done() // Decrement counter when function completes
	fmt.Println(msg)
}

// DemoConcurrency shows how to use goroutines
func DemoConcurrency() {
	fmt.Println("\n=== 12. CONCURRENCY: Goroutines ===")

	// Example 1: Basic goroutines with time.Sleep
	fmt.Println("\nExample 1: Basic goroutines")
	go PrintMessage("Hello")
	go PrintMessage("World")
	time.Sleep(1 * time.Second)
	fmt.Println("Goroutines completed")

	// Example 2: Using sync.WaitGroup (proper way)
	fmt.Println("\nExample 2: Goroutines with WaitGroup")
	var wg sync.WaitGroup

	wg.Add(1) // Increment counter
	go PrintMessageWithWG("First goroutine", &wg)

	wg.Add(1) // Increment counter
	go PrintMessageWithWG("Second goroutine", &wg)

	wg.Add(1) // Increment counter
	go PrintMessageWithWG("Third goroutine", &wg)

	wg.Wait() // Wait for all goroutines to complete
	fmt.Println("All goroutines with WaitGroup completed")

	// Example 3: Race condition WITHOUT mutex (unsafe)
	fmt.Println("\nExample 3: Race condition WITHOUT mutex (unsafe)")
	counter := 0
	var wg2 sync.WaitGroup

	for i := 0; i < 5; i++ {
		wg2.Add(1)
		go func() {
			defer wg2.Done()
			counter++ // Multiple goroutines modifying the same variable - RACE CONDITION!
		}()
	}
	wg2.Wait()
	fmt.Printf("Counter without mutex (may be wrong): %d\n", counter)

	// Example 4: Using Mutex to prevent race condition (safe)
	fmt.Println("\nExample 4: Using Mutex to prevent race condition (safe)")
	safeCounter := 0
	var mutex sync.Mutex
	var wg3 sync.WaitGroup

	for i := 0; i < 5; i++ {
		wg3.Add(1)
		go func() {
			defer wg3.Done()
			mutex.Lock()   // Acquire lock - only one goroutine can enter
			safeCounter++  // Safe: only one goroutine at a time
			mutex.Unlock() // Release lock - allow others to enter
		}()
	}
	wg3.Wait()
	fmt.Printf("Counter with mutex (always correct): %d\n", safeCounter)

	// Example 5: Using RWMutex for read-heavy operations
	fmt.Println("\nExample 5: RWMutex (multiple readers, one writer)")
	data := "initial value"
	var rwMutex sync.RWMutex
	var wg4 sync.WaitGroup

	// Multiple readers can read simultaneously
	for i := 1; i <= 3; i++ {
		wg4.Add(1)
		go func(id int) {
			defer wg4.Done()
			rwMutex.RLock() // Read lock - multiple goroutines can hold this
			fmt.Printf("Reader %d: Reading data = '%s'\n", id, data)
			time.Sleep(100 * time.Millisecond)
			rwMutex.RUnlock() // Release read lock
		}(i)
	}

	// Writer gets exclusive access
	wg4.Add(1)
	go func() {
		defer wg4.Done()
		time.Sleep(50 * time.Millisecond)
		rwMutex.Lock() // Write lock - exclusive (waits for all readers to finish)
		fmt.Println("Writer: Modifying data...")
		data = "modified value"
		rwMutex.Unlock() // Release write lock
	}()

	// Another reader after writer
	wg4.Add(1)
	go func() {
		defer wg4.Done()
		time.Sleep(200 * time.Millisecond)
		rwMutex.RLock() // Read lock
		fmt.Printf("Reader 4: Reading data = '%s'\n", data)
		rwMutex.RUnlock() // Release read lock
	}()

	wg4.Wait()
	fmt.Println("RWMutex example completed")
}

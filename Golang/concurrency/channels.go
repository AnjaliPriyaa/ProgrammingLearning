package concurrency

import "fmt"

/*
CHANNELS: A way for goroutines to talk to each other (like passing notes).

Think of it as a PIPE:
- One goroutine puts data IN one end
- Another goroutine takes data OUT the other end

Basic Syntax:
- ch := make(chan int)     // Create a pipe for integers
- ch <- 42                 // Put 42 INTO the pipe
- value := <-ch            // Take value OUT of the pipe

Why use channels?
- Safe way to share data between goroutines
- No need for locks (no race conditions!)
*/

// DemoChannels demonstrates channel usage with simple examples
func DemoChannels() {
	// Example 1: Simple send and receive
	fmt.Println("\n--- Example 1: Basic Channel ---")
	fmt.Println("Like passing a note between two people")

	messagePipe := make(chan string) // Create pipe

	// Person 1: Write note and put in pipe (in goroutine)
	go func() {
		messagePipe <- "Hello!" // Send (put IN)
	}()

	// Person 2: Take note from pipe
	note := <-messagePipe // Receive (take OUT)
	fmt.Println("Got message:", note)

	// Example 2: Sending multiple values
	fmt.Println("\n--- Example 2: Multiple Messages ---")
	fmt.Println("Sending 1, 2, 3 through the pipe")

	numberPipe := make(chan int)

	// Sender goroutine
	go func() {
		numberPipe <- 1
		numberPipe <- 2
		numberPipe <- 3
	}()

	// Receiver: Get all 3 numbers
	fmt.Println("Received:", <-numberPipe) // 1
	fmt.Println("Received:", <-numberPipe) // 2
	fmt.Println("Received:", <-numberPipe) // 3

	// Example 3: Close and range (receiving unknown amount)
	fmt.Println("\n--- Example 3: Close & Range ---")
	fmt.Println("Sender will close pipe when done")

	dataPipe := make(chan int)

	go func() {
		for i := 1; i <= 5; i++ {
			dataPipe <- i // Send numbers
		}
		close(dataPipe) // IMPORTANT: Tell receiver "no more data"
	}()

	// Receive until channel is closed
	for num := range dataPipe {
		fmt.Printf("Got: %d\n", num)
	}
	fmt.Println("Pipe closed, done receiving")

	// Example 4: Buffered channel (pipe with storage)
	fmt.Println("\n--- Example 4: Buffered Channel ---")
	fmt.Println("Like a mailbox that holds 2 letters")

	mailbox := make(chan string, 2) // Buffer size 2

	// Can put 2 items WITHOUT anyone receiving yet
	mailbox <- "Letter 1" // Doesn't wait
	mailbox <- "Letter 2" // Doesn't wait
	// mailbox <- "Letter 3" // Would BLOCK (mailbox full)

	// Take them out later
	fmt.Println(<-mailbox) // Letter 1
	fmt.Println(<-mailbox) // Letter 2

	// Example 5: Function returning result via channel
	fmt.Println("\n--- Example 5: Function with Channel ---")
	fmt.Println("Calculate 10 + 20 in background")

	resultPipe := make(chan int)

	go addNumbers(10, 20, resultPipe) // Do math in goroutine

	answer := <-resultPipe // Wait for answer
	fmt.Println("Answer:", answer)

	fmt.Println("\nChannels completed!")
}

// addNumbers calculates sum and sends result through channel
func addNumbers(a, b int, result chan int) {
	sum := a + b
	result <- sum // Send answer back
}

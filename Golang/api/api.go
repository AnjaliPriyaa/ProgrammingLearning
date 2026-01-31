package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

/*
SIMPLE REST API IN GO

What this does:
- Creates a web server
- Listens on http://localhost:8080
- Has 4 endpoints (URLs you can visit)

Run: go run api.go
Test: Open browser to http://localhost:8080
*/

// User represents a simple user
type User struct {
	ID   int
	Name string
	Age  int
}

// Simple in-memory storage (just for demo)
var users = []User{
	{ID: 1, Name: "Alice", Age: 25},
	{ID: 2, Name: "Bob", Age: 30},
}

func main() {
	fmt.Println("Starting API Server")
	fmt.Println("📍 Server running at http://localhost:8080")
	fmt.Println("\nAvailable endpoints:")
	fmt.Println("  GET  /           - Welcome message")
	fmt.Println("  GET  /users      - Get all users")
	fmt.Println("  GET  /user?id=1  - Get user by ID")
	fmt.Println("  POST /user       - Create new user")
	fmt.Println("Press Ctrl+C to stop")

	// Register routes (URLs)
	http.HandleFunc("/", homeHandler)
	http.HandleFunc("/users", getUsersHandler)
	http.HandleFunc("/user", userHandler)

	// Start server on port 8080
	http.ListenAndServe(":8080", nil)
}

// homeHandler - Welcome page
// Visit: http://localhost:8080
func homeHandler(w http.ResponseWriter, r *http.Request) {
	response := map[string]string{
		"message": "Welcome to Simple Go API!",
		"status":  "running",
	}
	json.NewEncoder(w).Encode(response)
}

// getUsersHandler - Get all users
// Visit: http://localhost:8080/users
func getUsersHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(users)
}

// userHandler - Get or Create user
// GET:  http://localhost:8080/user?id=1
// POST: http://localhost:8080/user (with JSON body)
func userHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == "GET" {
		// Get user by ID
		id := r.URL.Query().Get("id")

		if id == "" {
			json.NewEncoder(w).Encode(map[string]string{
				"error": "Please provide id parameter: /user?id=1",
			})
			return
		}

		// Find user (simple search)
		for _, user := range users {
			if fmt.Sprintf("%d", user.ID) == id {
				json.NewEncoder(w).Encode(user)
				return
			}
		}

		json.NewEncoder(w).Encode(map[string]string{
			"error": "User not found",
		})

	} else if r.Method == "POST" {
		// Create new user
		var newUser User

		// Read JSON from request body
		err := json.NewDecoder(r.Body).Decode(&newUser)
		if err != nil {
			json.NewEncoder(w).Encode(map[string]string{
				"error": "Invalid JSON",
			})
			return
		}

		// Add to users list
		newUser.ID = len(users) + 1
		users = append(users, newUser)

		json.NewEncoder(w).Encode(map[string]string{
			"message": "User created successfully",
			"id":      fmt.Sprintf("%d", newUser.ID),
		})
	}
}

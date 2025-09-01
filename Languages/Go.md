# **Go (Golang)**

### **1. Language Basics**

* **Type System:** Statically typed, strong typing. Variables require explicit or inferred types.
* **Paradigm:** Procedural with limited object-oriented features (structs, interfaces). No traditional inheritance; composition is favored.
* **Syntax Overview:**

  * Variables:

    ```go
    var x int = 10
    y := 5  // shorthand
    ```
  * Functions:

    ```go
    func add(a int, b int) int {
        return a + b
    }
    ```
  * Structs:

    ```go
    type Node struct {
        val int
        next *Node
    }
    ```
  * Loops: Only `for` exists (acts like for/while).
  * Conditionals: `if`, `else if`, `else`

---

### **2. Data Structures**

* **Built-in:** Arrays, slices, maps, structs, channels.
* **Custom Structures:** Trees, linked lists, and graphs via structs and pointers.
* **Immutability:** No immutability by default; constants via `const`.
* **Syntax Differences:**

  * Array: `var arr = [3]int{1,2,3}`
  * Slice: `arr := []int{1,2,3}`
  * Map: `m := map[string]int{"a":1, "b":2}`

---

### **3. Algorithms & Language Support**

* **Standard Library:** `fmt`, `math`, `sort`, `container/heap`, `strings`.
* **Recursion:** Supported; no tail recursion optimization.
* **Iteration Constructs:** Single `for` loop in multiple forms. Range iteration:

  ```go
  for i, v := range arr {
      fmt.Println(i, v)
  }
  ```
* **Built-in Helpers:**

  * Sorting: `sort.Ints(arr)`, custom sorting with `sort.Slice()`
  * Searching: Manual or via `sort.Search()`
  * Math: `math.Max`, `math.Min`, `math.Pow`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Compiled to native code; performance close to C/C++ in many cases.
* **Memory Usage:** Efficient; garbage collected.
* **Concurrency Support:** Excellent; goroutines and channels provide lightweight concurrency.
* **Compiler/Interpreter Optimizations:** Compiled language; efficient runtime.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Usually `func (this *Solution) FunctionName(args) returnType`.
* **Class vs Static Functions:** No classes; use `struct` and methods with receivers.
* **Input/Output Handling:** Arrays, slices, strings, maps. Trees and linked lists via structs and pointers.
* **Edge Case Handling:** Nil pointers must be checked; integer overflow can occur.

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Arrays, hash maps, dynamic programming, concurrency-heavy problems (if custom testing).
* **Strengths:** Concise syntax, high performance, built-in concurrency model.
* **Weaknesses:** Verbose for data structure implementations (e.g., no built-in set), lacks generics in older versions (Go 1.18+ supports them).

---

### **7. Language Idioms & Best Practices**

* Use slices instead of arrays for flexibility.
* Use `map[T]bool` as a set equivalent.
* Defer cleanup with `defer` keyword.
* Prefer composition over inheritance with structs.

Example idiomatic loop:

```go
for _, v := range arr {
    fmt.Println(v)
}
```

---

### **8. Error Handling & Debugging**

* **Error Handling:** No exceptions; explicit error returns.

  ```go
  val, err := someFunc()
  if err != nil {
      fmt.Println("Error:", err)
  }
  ```
* **Common Pitfalls:** Nil dereference, forgetting to check errors, confusing arrays vs slices.
* **Debugging Support:** `fmt.Println`, GoLand/VSCode debuggers, `delve` debugger.

---

### **9. Community & Resources**

* **Documentation:** [Go Official Docs](https://golang.org/doc/)
* **LeetCode Tips:** Go is less common but solid for concise, performant solutions. Lacks STL-equivalents, so sometimes more verbose than C++/Java.
* **Third-party Libraries:** Restricted on LeetCode; standard library is usually enough.

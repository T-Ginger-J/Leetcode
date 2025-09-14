
# **Swift**

### **1. Language Basics**

* **Type System:** Statically typed, strong typing with type inference.
* **Paradigm:** Multi-paradigm — object-oriented, functional, and protocol-oriented.
* **Syntax Overview:**

  * Variables:

    ```swift
    var x = 10         // mutable
    let y = 5          // immutable
    ```
  * Functions:

    ```swift
    func add(_ a: Int, _ b: Int) -> Int {
        return a + b
    }
    ```
  * Classes & Structs:

    ```swift
    class Node {
        var val: Int
        var next: Node?
        init(_ val: Int, _ next: Node? = nil) {
            self.val = val
            self.next = next
        }
    }
    ```
  * Loops: `for`, `while`, `repeat-while`
  * Conditionals: `if`, `else if`, `else`, `switch`

---

### **2. Data Structures**

* **Built-in:** Arrays, `Set`, `Dictionary`, `Queue`/`Stack` via arrays, Strings.
* **Custom Structures:** Trees and linked lists via classes or structs.
* **Immutability:** `let` for constants; arrays, dictionaries, and sets can be immutable if declared with `let`.
* **Syntax Differences:**

  * Array: `var arr = [1,2,3]`
  * Dictionary: `var dict = ["a":1, "b":2]`
  * Set: `var s: Set<Int> = [1,2,3]`

---

### **3. Algorithms & Language Support**

* **Standard Library:** `Swift Standard Library`, `Foundation` for additional utilities.
* **Recursion:** Fully supported; tail recursion optimization is not guaranteed.
* **Iteration Constructs:** `for-in`, `while`, `repeat-while`, `forEach`, functional methods (`map`, `filter`, `reduce`).
* **Built-in Helpers:**

  * Sorting: `arr.sort()`, `arr.sorted(by:)`
  * Searching: `arr.contains(x)`, `arr.firstIndex(of: x)`
  * Math: `max(a,b)`, `min(a,b)`, `pow(Double(a), Double(b))`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Compiled to native code; generally very performant, close to C++/Java.
* **Memory Usage:** Managed by ARC (Automatic Reference Counting).
* **Concurrency Support:** Threads, `DispatchQueue`, async/await in Swift 5.5+.
* **Compiler/Interpreter Optimizations:** Compiled to LLVM; aggressive optimizations possible.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Often top-level function or method inside `class Solution`.
* **Class vs Static Functions:** Both supported; instance methods are common on LeetCode.
* **Input/Output Handling:** Arrays, strings, sets, dictionaries; trees and linked lists via classes.
* **Edge Case Handling:** Optional types enforce null safety (`?`); integer overflow possible only with fixed-size types.

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Arrays, strings, hash maps, dynamic programming, recursion, trees.
* **Strengths:** Clear syntax, optionals enforce safety, modern language features, performant.
* **Weaknesses:** Verbose for some data structures like linked lists; optional unwrapping can be tricky for beginners.

---

### **7. Language Idioms & Best Practices**

* Use `let` for constants and immutable collections.
* Use optionals safely with `?` and `guard let`:

  ```swift
  if let node = node {
      print(node.val)
  }
  ```
* Prefer functional collection methods:

  ```swift
  let squares = arr.map { $0 * $0 }
  ```
* Use `switch` with pattern matching instead of long if-else chains.

---

### **8. Error Handling & Debugging**

* **Error Handling:**

  ```swift
  do {
      try someFunction()
  } catch {
      print(error)
  }
  ```
* **Common Pitfalls:** Forced unwrapping of optionals (`!`), off-by-one errors, recursion depth.
* **Debugging Support:** `print()`, Xcode debugger, LLDB.

---

### **9. Community & Resources**

* **Documentation:** [Swift Official Docs](https://developer.apple.com/swift/)
* **LeetCode Tips:** Swift is safe, concise, and fast for array/string problems; use optionals and functional constructs for clean solutions.
* **Third-party Libraries:** Not allowed on LeetCode; standard library is sufficient.


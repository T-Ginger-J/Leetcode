# **Kotlin**

### **1. Language Basics**

* **Type System:** Statically typed, strong typing, with type inference.
* **Paradigm:** Object-oriented and functional. Fully interoperable with Java.
* **Syntax Overview:**

  * Variables:

    ```kotlin
    val x: Int = 10   // immutable
    var y: Int = 5    // mutable
    ```
  * Functions:

    ```kotlin
    fun add(a: Int, b: Int): Int {
        return a + b
    }
    ```
  * Classes:

    ```kotlin
    class Node(var value: Int, var next: Node? = null)
    ```
  * Loops: `for`, `while`, `do-while`
  * Conditionals: `if`, `else if`, `else`, `when` (like switch)

---

### **2. Data Structures**

* **Built-in:** Arrays, `List`, `MutableList`, `Set`, `Map`, `MutableMap`, `Queue`, `Stack`.
* **Custom Structures:** Trees, linked lists, graphs via classes.
* **Immutability:** Immutable by default (`val`); mutable via `var`. Collections have immutable and mutable variants.
* **Syntax Differences:**

  * Array: `val arr = arrayOf(1,2,3)`
  * List: `val list = listOf(1,2,3)` or `val mutableList = mutableListOf(1,2,3)`
  * Map: `val map = mapOf("a" to 1, "b" to 2)`
  * Set: `val set = setOf(1,2,3)`

---

### **3. Algorithms & Language Support**

* **Standard Library:** Rich collection API, `kotlin.math`, `kotlin.collections`.
* **Recursion:** Fully supported; tail recursion optimized with `tailrec`.
* **Iteration Constructs:** `for`, `while`, `forEach`, functional operations (`map`, `filter`, `fold`, `reduce`).
* **Built-in Helpers:**

  * Sorting: `arr.sort()`, `list.sorted()`, `list.sortedBy { ... }`
  * Searching: `list.indexOf(x)`, `list.contains(x)`
  * Math: `max(a,b)`, `min(a,b)`, `pow(a,b)`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Runs on JVM; similar performance to Java. Functional operations add minor overhead.
* **Memory Usage:** Managed via JVM garbage collection.
* **Concurrency Support:** JVM threads, `async`/`await` with coroutines.
* **Compiler/Interpreter Optimizations:** Compiled to JVM bytecode; JIT optimizations applied at runtime.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Usually `fun functionName(args): ReturnType`; can also be methods inside `class Solution`.
* **Class vs Static Functions:** Use `companion object` for static-like methods; instance methods are common.
* **Input/Output Handling:** Arrays, lists, maps, and strings are standard; trees and linked lists via classes.
* **Edge Case Handling:** Null safety enforced with `?` and `!!`; integer overflow is rare (64-bit integers).

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Arrays, strings, hash maps, recursion, dynamic programming, functional-style problems.
* **Strengths:** Null safety, concise syntax, interoperable with Java libraries, strong functional programming support.
* **Weaknesses:** Verbose for simple problems if not using functional constructs, JVM overhead for small inputs.

---

### **7. Language Idioms & Best Practices**

* Use immutable variables (`val`) and immutable collections where possible.
* Prefer functional operations over loops:

  ```kotlin
  val squares = list.map { it * it }
  ```
* Use `when` instead of long `if-else` chains:

  ```kotlin
  when(value) {
      0 -> "zero"
      else -> "non-zero"
  }
  ```
* Handle nulls safely:

  ```kotlin
  val node: Node? = null
  println(node?.value)
  ```

---

### **8. Error Handling & Debugging**

* **Exception Handling:**

  ```kotlin
  try {
      val result = 10 / 0
  } catch(e: ArithmeticException) {
      println(e.message)
  }
  ```
* **Common Pitfalls:** Null pointer exceptions (if using `!!`), off-by-one errors, recursion depth.
* **Debugging Support:** `println()`, IDE debuggers (IntelliJ IDEA, Android Studio).

---

### **9. Community & Resources**

* **Documentation:** [Kotlin Official Docs](https://kotlinlang.org/docs/home.html)
* **LeetCode Tips:** Kotlin is great for array, string, and functional programming problems; concise syntax helps write readable solutions.
* **Third-party Libraries:** Not allowed on LeetCode; standard library is sufficient.

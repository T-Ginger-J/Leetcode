Here’s a detailed Scala entry for your LeetCode language comparison document:

---

# **Scala**

### **1. Language Basics**

* **Type System:** Statically typed, strong typing, with type inference.
* **Paradigm:** Multi-paradigm — object-oriented and functional programming first-class.
* **Syntax Overview:**

  * Variables:

    ```scala
    val x: Int = 10   // immutable
    var y: Int = 5    // mutable
    ```
  * Functions:

    ```scala
    def add(a: Int, b: Int): Int = a + b
    ```
  * Classes:

    ```scala
    class Node(var value: Int, var next: Node = null)
    ```
  * Loops: `for`, `while`, `do-while`
  * Conditionals: `if`, `else if`, `else`, `match` (pattern matching)

---

### **2. Data Structures**

* **Built-in:** Arrays, `List`, `Vector`, `Set`, `Map`, `Queue`, `Stack`.
* **Custom Structures:** Trees, linked lists, graphs via classes and case classes.
* **Immutability:** Collections are immutable by default (`List`, `Map`); mutable versions (`ArrayBuffer`, `HashMap`) are available.
* **Syntax Differences:**

  * Array: `val arr = Array(1,2,3)`
  * List: `val list = List(1,2,3)`
  * Map: `val map = Map("a" -> 1, "b" -> 2)`
  * Set: `val set = Set(1,2,3)`

---

### **3. Algorithms & Language Support**

* **Standard Library:** `scala.collection`, `scala.math`, rich functional methods on collections.
* **Recursion:** Fully supported; tail recursion optimized with `@tailrec`.
* **Iteration Constructs:** `for`, `while`, `foreach`, and functional operations like `map`, `filter`, `foldLeft`, `reduce`.
* **Built-in Helpers:**

  * Sorting: `arr.sorted`, `list.sortBy(_ * -1)`
  * Searching: `arr.indexOf(x)`, `list.contains(x)`
  * Math: `math.max(a,b)`, `math.min(a,b)`, `math.pow(a,b)`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Compiled to JVM bytecode; similar performance to Java. Functional constructs may have minor overhead.
* **Memory Usage:** Managed via JVM garbage collection.
* **Concurrency Support:** JVM threads, Futures, `scala.concurrent`, and Akka for actor-based concurrency.
* **Compiler/Interpreter Optimizations:** Compiled to JVM bytecode; JIT optimization at runtime.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Often standalone `def` functions; can also be methods in `object Solution`.
* **Class vs Static Functions:** `object` used for static methods; classes used for custom data structures.
* **Input/Output Handling:** Arrays, lists, maps, and strings are straightforward; trees and linked lists require classes or case classes.
* **Edge Case Handling:** Null values (`null`) rarely used; `Option[T]` preferred for optional values. Integer overflow possible for large numbers — use `Long`.

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Arrays, strings, hash maps, recursion, dynamic programming, functional-style problems.
* **Strengths:** Concise syntax, functional programming paradigms, immutable collections, JVM performance.
* **Weaknesses:** Verbose for simple problems if not using functional constructs, JVM startup overhead for small inputs.

---

### **7. Language Idioms & Best Practices**

* Prefer immutable collections: `List`, `Map`.
* Use functional operations over loops:

  ```scala
  val squares = list.map(x => x * x)
  ```
* Pattern matching instead of multiple if-else:

  ```scala
  value match {
    case 0 => "zero"
    case _ => "non-zero"
  }
  ```
* Use `Option` instead of nulls:

  ```scala
  val maybeVal: Option[Int] = Some(5)
  maybeVal.foreach(println)
  ```

---

### **8. Error Handling & Debugging**

* **Exception Handling:**

  ```scala
  try {
    val result = 10 / 0
  } catch {
    case e: ArithmeticException => println(e.getMessage)
  }
  ```
* **Common Pitfalls:** Null references, off-by-one errors, performance overhead from non-tail recursion.
* **Debugging Support:** `println`, IDE debuggers, JVM stack traces.

---

### **9. Community & Resources**

* **Documentation:** [Scala Official Docs](https://docs.scala-lang.org/)
* **LeetCode Tips:** Scala is great for functional programming problems, array/string manipulation, and problems requiring immutable data structures.
* **Third-party Libraries:** Not allowed on LeetCode; standard library is sufficient.

---

The remaining commonly supported LeetCode languages could include **Swift**, **Kotlin**, or **Dart**.

Do you want me to do **Swift next**?

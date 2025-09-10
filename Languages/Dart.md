# **Dart**

### **1. Language Basics**

* **Type System:** Statically typed with optional type inference; supports strong typing.
* **Paradigm:** Object-oriented, with functional programming features.
* **Syntax Overview:**

  * Variables:

    ```dart
    int x = 10;
    var y = 5;      // type inferred
    final z = 20;   // immutable
    ```
  * Functions:

    ```dart
    int add(int a, int b) {
      return a + b;
    }
    ```
  * Classes:

    ```dart
    class Node {
      int val;
      Node? next;
      Node(this.val, [this.next]);
    }
    ```
  * Loops: `for`, `while`, `do-while`, `for-in`
  * Conditionals: `if`, `else if`, `else`, `switch`, ternary operator

---

### **2. Data Structures**

* **Built-in:** Arrays (`List`), `Map`, `Set`, `Queue`, `Stack` (via `List`), `String`.
* **Custom Structures:** Trees and linked lists via classes.
* **Immutability:** `final` and `const` for immutable variables. Collections can also be made unmodifiable.
* **Syntax Differences:**

  * List: `List<int> arr = [1,2,3];`
  * Map: `Map<String,int> map = {"a":1, "b":2};`
  * Set: `Set<int> s = {1,2,3};`

---

### **3. Algorithms & Language Support**

* **Standard Library:** `dart:core`, `dart:collection`, `dart:math`.
* **Recursion:** Fully supported; no tail recursion optimization.
* **Iteration Constructs:** `for`, `for-in`, `while`, `do-while`, `forEach`, functional operations like `map`, `where`, `reduce`.
* **Built-in Helpers:**

  * Sorting: `arr.sort()`, `arr.sort((a,b)=>b-a)`
  * Searching: `arr.indexOf(x)`, `arr.contains(x)`
  * Math: `max(a,b)`, `min(a,b)`, `pow(a,b)`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Dart is compiled to native code (AOT) for performance or to JavaScript (JIT) for web; generally fast enough for LeetCode.
* **Memory Usage:** Managed via garbage collection.
* **Concurrency Support:** `Future` and `async/await` for asynchronous operations.
* **Compiler/Interpreter Optimizations:** Ahead-of-time (AOT) and just-in-time (JIT) compilation optimize runtime speed.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Usually a top-level function, or a method inside `class Solution`.
* **Class vs Static Functions:** Both supported; LeetCode often uses instance methods in `class Solution`.
* **Input/Output Handling:** Lists, strings, maps; trees and linked lists via classes.
* **Edge Case Handling:** Null safety enforced (`?` and `!`), integer overflow is rare (uses 64-bit ints).

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Arrays, strings, hash maps, dynamic programming, basic graph problems.
* **Strengths:** Clear syntax, null safety, functional operations, modern OOP features.
* **Weaknesses:** Less common on LeetCode, fewer built-in algorithm utilities than Java/C++ STL.

---

### **7. Language Idioms & Best Practices**

* Use `List` for arrays and dynamic collections.
* Prefer `final` for variables that don’t change.
* Use null safety features to avoid runtime errors:

  ```dart
  Node? node;
  print(node?.val);
  ```
* Functional operations for concise collection manipulation:

  ```dart
  var squares = arr.map((x) => x*x).toList();
  ```

---

### **8. Error Handling & Debugging**

* **Exception Handling:**

  ```dart
  try {
    int result = 10 ~/ 0;
  } catch (e) {
    print(e);
  }
  ```
* **Common Pitfalls:** Forgetting null safety, off-by-one errors, misunderstanding list references vs copies.
* **Debugging Support:** `print()`, Dart DevTools, IDE debuggers (VSCode, IntelliJ).

---

### **9. Community & Resources**

* **Documentation:** [Dart Docs](https://dart.dev/guides)
* **LeetCode Tips:** Dart works well for array, string, and map problems; null safety reduces runtime errors.
* **Third-party Libraries:** Not allowed on LeetCode; standard library is sufficient.


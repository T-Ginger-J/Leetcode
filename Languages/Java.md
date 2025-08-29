
# **Java**

### **1. Language Basics**

* **Type System:** Statically typed, strong typing. Variables must be declared with their type.
* **Paradigm:** Object-oriented primarily, supports procedural and limited functional programming (lambdas, streams).
* **Syntax Overview:**

  * Variables: `int x = 10;`
  * Functions (methods):

    ```java
    public int add(int a, int b) {
        return a + b;
    }
    ```
  * Classes:

    ```java
    class Node {
        int val;
        Node next;
        Node(int val) { this.val = val; this.next = null; }
    }
    ```
  * Loops: `for (int i = 0; i < n; i++)` and `while (condition)`
  * Conditionals: `if`, `else if`, `else`

---

### **2. Data Structures**

* **Built-in:** Arrays, `ArrayList`, `LinkedList`, `HashSet`, `HashMap`, `PriorityQueue`.
* **Custom Structures:** Classes make implementing trees, linked lists, graphs straightforward.
* **Immutability:** Strings are immutable; most collection classes are mutable.
* **Syntax Differences:**

  * Array: `int[] arr = {1,2,3};`
  * List: `List<Integer> list = new ArrayList<>();`
  * Map: `Map<String, Integer> map = new HashMap<>();`
  * Queue: `Queue<Integer> q = new LinkedList<>();`

---

### **3. Algorithms & Language Support**

* **Standard Library:** `Collections`, `Arrays`, `Math`, `Queue`, `Stack`, `PriorityQueue`.
* **Recursion:** Fully supported; no built-in tail recursion optimization.
* **Iteration Constructs:** `for`, enhanced `for-each`, `while`, streams for functional-style operations.
* **Built-in Helpers:**

  * Sorting: `Arrays.sort(arr)` or `Collections.sort(list)`
  * Searching: `Arrays.binarySearch(arr, key)`
  * Math: `Math.max`, `Math.min`, `Math.pow`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Faster than Python for most cases due to static typing and compilation.
* **Memory Usage:** Moderate; overhead depends on object creation and garbage collection.
* **Concurrency Support:** Threads, `ExecutorService`, `synchronized` blocks, `CompletableFuture` for async tasks.
* **Compiler/Interpreter Optimizations:** Runs on JVM; JIT compiler improves runtime performance.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Usually provided inside `class Solution`; method may be `public` and static if needed.
* **Class vs Static Functions:** `class Solution` methods are commonly instance methods (`this` required) but static methods can also be used.
* **Input/Output Handling:** Arrays, lists, trees, and linked lists are handled with classes and objects.
* **Edge Case Handling:** Null references need explicit checks; integer overflows can occur (use `long` if necessary).

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Graphs, dynamic programming, trees, linked lists, sorting/searching.
* **Strengths:** Strong type safety, better performance than scripting languages, mature libraries.
* **Weaknesses:** Verbose syntax, slower to write than Python, boilerplate code for common tasks.

---

### **7. Language Idioms & Best Practices**

* Prefer `ArrayList` over arrays for dynamic size.
* Use `HashMap` or `HashSet` for fast lookups.
* Stream API for concise functional operations:

  ```java
  list.stream().filter(x -> x > 0).collect(Collectors.toList());
  ```
* Always check for `null` to avoid `NullPointerException`.

---

### **8. Error Handling & Debugging**

* **Exception Handling:**

  ```java
  try {
      // code
  } catch (Exception e) {
      e.printStackTrace();
  }
  ```
* **Common Pitfalls:** NullPointerException, ArrayIndexOutOfBounds, integer overflow.
* **Debugging Support:** `System.out.println`, IDE debuggers (IntelliJ, Eclipse), stack traces.

---

### **9. Community & Resources**

* **Documentation:** [Java Official Docs](https://docs.oracle.com/en/java/)
* **LeetCode Tips:** Java is widely used for performance-sensitive problems, especially involving OOP and complex data structures.
* **Third-party Libraries:** Limited on LeetCode; standard Java Collections Framework is usually sufficient.


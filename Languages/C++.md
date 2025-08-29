
# **C++**

### **1. Language Basics**

* **Type System:** Statically typed, strong typing. Variables must declare their type.
* **Paradigm:** Multi-paradigm — procedural, object-oriented, and supports functional programming (lambdas).
* **Syntax Overview:**

  * Variables: `int x = 10;`
  * Functions:

    ```cpp
    int add(int a, int b) {
        return a + b;
    }
    ```
  * Classes:

    ```cpp
    class Node {
    public:
        int val;
        Node* next;
        Node(int v) : val(v), next(nullptr) {}
    };
    ```
  * Loops: `for (int i=0; i<n; i++)`, `while (condition)`
  * Conditionals: `if`, `else if`, `else`

---

### **2. Data Structures**

* **Built-in:** Arrays, `vector`, `list`, `set`, `unordered_set`, `map`, `unordered_map`, `queue`, `stack`, `priority_queue`.
* **Custom Structures:** Classes and structs for linked lists, trees, graphs. Pointers allow direct memory manipulation.
* **Immutability:** No built-in immutability; `const` can make variables read-only.
* **Syntax Differences:**

  * Array: `int arr[] = {1,2,3};`
  * Vector: `vector<int> v = {1,2,3};`
  * Map: `map<string,int> m;`
  * Set: `set<int> s;`
  * Queue: `queue<int> q;`

---

### **3. Algorithms & Language Support**

* **Standard Library:** STL (`algorithm`, `numeric`, `queue`, `stack`, `set`, `map`).
* **Recursion:** Fully supported; no recursion depth limit imposed by language itself.
* **Iteration Constructs:** `for`, `while`, `range-based for`, STL iterators.
* **Built-in Helpers:**

  * Sorting: `sort(arr, arr+n)` or `sort(v.begin(), v.end())`
  * Searching: `binary_search`, `lower_bound`, `upper_bound`
  * Math: `abs`, `pow`, `max`, `min`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Highly efficient; low-level control allows optimization for runtime-critical problems.
* **Memory Usage:** Low overhead; fine-grained control with pointers and references.
* **Concurrency Support:** Threads (`<thread>`), mutexes (`<mutex>`), async tasks (`<future>`).
* **Compiler/Interpreter Optimizations:** Compiled language; aggressive optimizations via GCC/Clang/MSVC.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Usually provided; may be standalone or inside `class Solution`.
* **Class vs Static Functions:** Instance or static methods supported; most LeetCode C++ solutions use instance methods.
* **Input/Output Handling:** Arrays, vectors, strings, and STL containers. Trees and linked lists via pointers.
* **Edge Case Handling:** Null pointers (`nullptr`) must be handled; integer overflow possible — use `long long` when needed.

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Graphs, dynamic programming, trees, linked lists, bit manipulation, advanced data structures.
* **Strengths:** Maximum control over memory and runtime; STL provides powerful tools.
* **Weaknesses:** Verbose syntax for simple tasks; manual memory handling can lead to bugs.

---

### **7. Language Idioms & Best Practices**

* Use STL containers like `vector`, `unordered_map` for efficiency.
* Prefer range-based for loops for clarity:

  ```cpp
  for(int x : v) { cout << x; }
  ```
* Use `auto` to simplify iterator declarations.
* Use references (`&`) to avoid unnecessary copies.

---

### **8. Error Handling & Debugging**

* **Exception Handling:**

  ```cpp
  try {
      // code
  } catch (exception& e) {
      cout << e.what() << endl;
  }
  ```
* **Common Pitfalls:** Null pointers, off-by-one errors, memory leaks, integer overflow.
* **Debugging Support:** `cout`, `cerr`, gdb/IDE debuggers, memory analysis tools like Valgrind.

---

### **9. Community & Resources**

* **Documentation:** [cppreference.com](https://en.cppreference.com/)
* **LeetCode Tips:** C++ is preferred for performance-critical problems, large input sizes, and problems requiring advanced data structures.
* **Third-party Libraries:** Only STL is allowed on LeetCode; sufficient for most problems.

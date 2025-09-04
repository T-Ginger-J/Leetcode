
# **PHP**

### **1. Language Basics**

* **Type System:** Dynamically typed, weakly typed. Types are inferred at runtime; implicit type coercion occurs.
* **Paradigm:** Primarily procedural and object-oriented; supports functional programming.
* **Syntax Overview:**

  * Variables: `$x = 10;`
  * Functions:

    ```php
    function add($a, $b) {
        return $a + $b;
    }
    ```
  * Classes:

    ```php
    class Node {
        public $val;
        public $next;
        public function __construct($val) {
            $this->val = $val;
            $this->next = null;
        }
    }
    ```
  * Loops: `for`, `foreach`, `while`, `do-while`
  * Conditionals: `if`, `elseif`, `else`

---

### **2. Data Structures**

* **Built-in:** Arrays (used as lists or hash maps), objects, `SplStack`, `SplQueue`, `SplHeap`.
* **Custom Structures:** Trees and linked lists via classes.
* **Immutability:** Strings are mutable; variables are mutable by default.
* **Syntax Differences:**

  * Array: `$arr = [1,2,3];`
  * Associative array (hash map): `$map = ["a" => 1, "b" => 2];`
  * Stack: `$stack = new SplStack();`
  * Queue: `$queue = new SplQueue();`

---

### **3. Algorithms & Language Support**

* **Standard Library:** Extensive support for arrays, strings, math, and SPL (Standard PHP Library) classes.
* **Recursion:** Fully supported; PHP allows deep recursion but stack size limits apply.
* **Iteration Constructs:** `for`, `foreach`, `while`, `array_map`, `array_filter`, `array_reduce`.
* **Built-in Helpers:**

  * Sorting: `sort($arr)`, `rsort($arr)`, `asort($map)`
  * Searching: `in_array($x, $arr)`, `array_search($x, $arr)`
  * Math: `max()`, `min()`, `pow()`, `abs()`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Slower than C++/Java/Python for large inputs; array operations may have additional overhead.
* **Memory Usage:** Moderate; managed via garbage collection.
* **Concurrency Support:** Limited in standard PHP; can use multi-process or extensions (e.g., pthreads) but not typical on LeetCode.
* **Compiler/Interpreter Optimizations:** Interpreted; opcode caching with OPcache improves performance.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Usually simple function: `function functionName($arg1, $arg2)`; no wrapping class required unless specified.
* **Class vs Static Functions:** Both supported; most LeetCode problems are solved with standalone functions.
* **Input/Output Handling:** Arrays and strings are straightforward; linked lists and trees require classes/objects.
* **Edge Case Handling:** Null values (`null`) must be checked; automatic type coercion may introduce subtle bugs.

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Arrays, strings, hash maps, simple recursion.
* **Strengths:** Concise syntax, fast prototyping, flexible dynamic typing.
* **Weaknesses:** Slower runtime, manual object handling for trees/linked lists, limited concurrency.

---

### **7. Language Idioms & Best Practices**

* Use `foreach` for iteration:

  ```php
  foreach ($arr as $value) { echo $value; }
  ```
* Use associative arrays as hash maps: `$map[$key] = $value;`
* Avoid implicit type coercion issues by using strict comparisons (`===`).
* Use SPL classes (`SplStack`, `SplQueue`) for standard data structures.

---

### **8. Error Handling & Debugging**

* **Exception Handling:**

  ```php
  try {
      // code
  } catch (Exception $e) {
      echo $e->getMessage();
  }
  ```
* **Common Pitfalls:** Implicit type coercion, null pointer errors (`null` access), off-by-one in arrays.
* **Debugging Support:** `var_dump()`, `print_r()`, Xdebug debugger.

---

### **9. Community & Resources**

* **Documentation:** [PHP Manual](https://www.php.net/manual/en/)
* **LeetCode Tips:** PHP is rarely used on LeetCode; best suited for quick prototyping of array/string problems.
* **Third-party Libraries:** Not allowed on LeetCode; standard PHP library sufficient.

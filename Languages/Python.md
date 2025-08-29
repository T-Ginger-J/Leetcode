
# **Python**

### **1. Language Basics**

* **Type System:** Dynamically typed, strong typing. No need to declare variable types explicitly.
* **Paradigm:** Multi-paradigm — procedural, object-oriented, and functional programming supported.
* **Syntax Overview:**

  * Variables: `x = 10`
  * Functions:

    ```python
    def add(a, b):
        return a + b
    ```
  * Classes:

    ```python
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
    ```
  * Loops: `for i in range(n):` and `while condition:`
  * Conditionals: `if`, `elif`, `else`

---

### **2. Data Structures**

* **Built-in:** List, tuple, set, dict, deque (from `collections`), heap (from `heapq`).
* **Custom Structures:** Easy to implement linked lists, trees, graphs. Classes and dictionaries are often used.
* **Immutability:** Tuples and strings are immutable; lists, dicts, sets are mutable.
* **Syntax Differences:**

  * List: `arr = [1,2,3]`
  * Dict: `d = {'a': 1, 'b': 2}`
  * Set: `s = {1,2,3}`
  * Queue: `from collections import deque; q = deque()`

---

### **3. Algorithms & Language Support**

* **Standard Library:** `math`, `heapq`, `itertools`, `collections`, `bisect`.
* **Recursion:** Supported, limited by default recursion depth (\~1000). `sys.setrecursionlimit()` can adjust.
* **Iteration Constructs:** For-loops, `map`, `filter`, `reduce`, comprehensions `[x*x for x in arr]`.
* **Built-in Helpers:**

  * Sorting: `sorted(arr)` or `arr.sort()`
  * Searching: `bisect.bisect_left(arr, x)`
  * Counting: `collections.Counter(arr)`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Python is slower than compiled languages like C++ or Java due to interpretation and dynamic typing.
* **Memory Usage:** Higher memory overhead compared to C++ or Java.
* **Concurrency Support:** `threading` (GIL-limited), `multiprocessing`, `asyncio`.
* **Compiler/Interpreter Optimizations:** CPython standard interpreter; PyPy can be faster with JIT compilation.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Usually provided in problem; compatible with Python 3.
* **Class vs Static Functions:** Typically, `class Solution:` with method `def functionName(self, params)`.
* **Input/Output Handling:** Lists, integers, strings, and nested lists are directly usable. Trees and linked lists are given as objects.
* **Edge Case Handling:** Python handles large integers natively; `None` used for null values.

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Strings, arrays, dictionaries, dynamic programming, graph traversal.
* **Strengths:** Quick prototyping, concise syntax, rich standard library.
* **Weaknesses:** Slower execution for time-critical problems, high memory usage in large datasets.

---

### **7. Language Idioms & Best Practices**

* List comprehensions: `[x*2 for x in arr]`
* Dictionary & `Counter` usage: `counts = Counter(arr)`
* Use of slicing: `arr[1:5]`
* Default argument values in functions: `def func(a, b=0):`

---

### **8. Error Handling & Debugging**

* **Exception Handling:**

  ```python
  try:
      # code
  except Exception as e:
      print(e)
  ```
* **Common Pitfalls:** Index errors, off-by-one, mutable default arguments.
* **Debugging Support:** `print` statements, `pdb` debugger, online IDE support.

---

### **9. Community & Resources**

* **Documentation:** [Python Official Docs](https://docs.python.org/3/)
* **LeetCode Tips:** Python is often preferred for concise, readable solutions. Commonly used in array/string/DP problems.
* **Third-party Libraries:** Generally restricted on LeetCode; standard library is sufficient for most problems.


# **Ruby**

### **1. Language Basics**

* **Type System:** Dynamically typed, strong typing (types are enforced at runtime).
* **Paradigm:** Purely object-oriented (everything is an object), with strong support for functional and procedural styles.
* **Syntax Overview:**

  * Variables:

    ```ruby
    x = 10
    y = "hello"
    ```
  * Functions (methods):

    ```ruby
    def add(a, b)
      a + b
    end
    ```
  * Classes:

    ```ruby
    class Node
      attr_accessor :val, :next
      def initialize(val)
        @val = val
        @next = nil
      end
    end
    ```
  * Loops: `for`, `while`, `until`, `each`, ranges.
  * Conditionals: `if`, `elsif`, `else`, `unless`.

---

### **2. Data Structures**

* **Built-in:** Array, Hash, Set (via `require 'set'`), Range, String, Symbol.
* **Custom Structures:** Trees, linked lists via `class` definitions.
* **Immutability:** Most objects mutable except Symbols and some literals.
* **Syntax Differences:**

  * Array: `arr = [1, 2, 3]`
  * Hash: `h = { "a" => 1, "b" => 2 }` or `{ a: 1, b: 2 }`
  * Set:

    ```ruby
    require 'set'
    s = Set.new([1,2,3])
    ```

---

### **3. Algorithms & Language Support**

* **Standard Library:** Rich support for collections, enumerables, math, and string manipulation.
* **Recursion:** Fully supported (but slower compared to iterative solutions).
* **Iteration Constructs:** `for`, `while`, `arr.each`, `arr.map`, `arr.select`, `arr.reduce`.
* **Built-in Helpers:**

  * Sorting: `arr.sort`, `arr.sort_by { |x| ... }`
  * Searching: `arr.find`, `arr.index`, `arr.bsearch`.
  * Math: `Math.sqrt`, `Math.log`, etc.

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Ruby is slow compared to C++/Java/Python. Not ideal for problems with large input sizes.
* **Memory Usage:** Moderate; managed by garbage collection.
* **Concurrency Support:** Threads supported, but MRI Ruby has a global interpreter lock (GIL). JRuby or Rubinius overcome this.
* **Compiler/Interpreter Optimizations:** Interpreted; not JIT-compiled in most environments (though Ruby 3+ adds MJIT).

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Usually just a function; LeetCode may wrap in `def self.function_name(...)`.
* **Class vs Static Functions:** Static functions via `self.method_name`.
* **Input/Output Handling:** Arrays and strings are straightforward; trees and linked lists require class definitions.
* **Edge Case Handling:** `nil` is Ruby’s null; must check for `nil` to avoid `NoMethodError`.

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Arrays, strings, hash maps, combinatorics.
* **Strengths:** Extremely concise and expressive, easy to prototype, great built-in enumerable helpers.
* **Weaknesses:** Slower execution time, not always accepted for high-performance problems, verbose for data structures like trees.

---

### **7. Language Idioms & Best Practices**

* Use iterators/enumerables instead of manual loops:

  ```ruby
  arr.map { |x| x * x }
  ```
* Use ranges for iteration:

  ```ruby
  (1..5).each { |i| puts i }
  ```
* Use `nil` checks with safe navigation:

  ```ruby
  node&.next
  ```
* Hash default values:

  ```ruby
  h = Hash.new(0)
  h["a"] += 1
  ```

---

### **8. Error Handling & Debugging**

* **Error Handling:** Exceptions with `begin ... rescue ... end`.

  ```ruby
  begin
    result = 10 / 0
  rescue ZeroDivisionError => e
    puts "Error: #{e.message}"
  end
  ```
* **Common Pitfalls:** Forgetting `nil` checks, slower recursion, GIL limits concurrency.
* **Debugging Support:** `puts`, `p`, `pp` for pretty print, debuggers (`byebug`, `pry`).

---

### **9. Community & Resources**

* **Documentation:** [Ruby Docs](https://ruby-doc.org/core-3.1.2/)
* **LeetCode Tips:** Ruby’s expressiveness makes it concise for string/array/hash problems, but runtime speed may cause TLE on large test cases.
* **Third-party Libraries:** Not allowed on LeetCode; stick to core library and `Set`.


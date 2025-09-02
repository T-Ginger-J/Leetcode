# **Rust**

### **1. Language Basics**

* **Type System:** Statically typed, very strong typing. Compiler enforces strict ownership, borrowing, and lifetimes.
* **Paradigm:** Multi-paradigm — systems-level, functional, and object-oriented patterns via traits.
* **Syntax Overview:**

  * Variables:

    ```rust
    let x = 10;        // immutable by default
    let mut y = 5;     // mutable
    ```
  * Functions:

    ```rust
    fn add(a: i32, b: i32) -> i32 {
        a + b
    }
    ```
  * Structs:

    ```rust
    struct Node {
        val: i32,
        next: Option<Box<Node>>,
    }
    ```
  * Loops: `for i in 0..n`, `while condition`, `loop { ... }`
  * Conditionals: `if`, `else if`, `else`, `match` (pattern matching)

---

### **2. Data Structures**

* **Built-in:** Arrays, slices, tuples, `Vec`, `HashMap`, `HashSet`, `String`, `Option`, `Result`.
* **Custom Structures:** Trees, linked lists, and graphs via `struct` and enums (`Option`, `Rc`, `RefCell`).
* **Immutability:** Immutable by default; must use `mut` for mutability.
* **Syntax Differences:**

  * Array: `let arr = [1, 2, 3];`
  * Vector: `let v = vec![1,2,3];`
  * HashMap:

    ```rust
    use std::collections::HashMap;
    let mut m = HashMap::new();
    m.insert("a", 1);
    ```

---

### **3. Algorithms & Language Support**

* **Standard Library:** `std::collections` (Vec, HashMap, HashSet, BinaryHeap), `std::cmp`, `std::iter`.
* **Recursion:** Supported, but often replaced with iteration to avoid borrow checker complexity.
* **Iteration Constructs:** `for`, iterators (`map`, `filter`, `collect`, etc.), `while let`.
* **Built-in Helpers:**

  * Sorting: `v.sort()` or `v.sort_by(...)`
  * Searching: `v.binary_search(&x)`
  * Math: `num::traits` or `std::cmp::max/min`

---

### **4. Performance & Complexity**

* **Time Complexity Notes:** Comparable to C++ — zero-cost abstractions and fine control over memory.
* **Memory Usage:** Very efficient; ownership and borrowing system ensures no leaks without garbage collection.
* **Concurrency Support:** Safe concurrency via threads, channels, async/await.
* **Compiler/Interpreter Optimizations:** Compiled with LLVM backend; very optimized but slower compile times.

---

### **5. Syntax Specifics for LeetCode**

* **Function Signature:** Often requires `impl Solution { pub fn ... }` as LeetCode wraps methods in `struct Solution;`.
* **Class vs Static Functions:** No classes; methods are attached to `impl` blocks.
* **Input/Output Handling:** Uses `Vec`, `String`, and `Option`; trees and linked lists require explicit pointer-like constructs (`Box`, `Rc`, `RefCell`).
* **Edge Case Handling:** Compiler forces handling of `Option` and `Result`, reducing runtime null/exception bugs. Integer overflow panics in debug builds, wraps in release.

---

### **6. Use Cases / Problem Type Suitability**

* **Commonly Solved Problems:** Arrays, strings, hash maps, bit manipulation, graph algorithms, concurrency problems.
* **Strengths:** Performance on par with C++, strict compiler catches errors early, safe concurrency.
* **Weaknesses:** Verbose for tree/linked list problems due to ownership rules, steep learning curve.

---

### **7. Language Idioms & Best Practices**

* Use iterators instead of manual loops when possible:

  ```rust
  let squares: Vec<i32> = arr.iter().map(|x| x*x).collect();
  ```
* Handle null-like cases with `Option`:

  ```rust
  let maybe_val: Option<i32> = Some(5);
  if let Some(v) = maybe_val { println!("{}", v); }
  ```
* Use pattern matching with `match` for branching logic.
* Prefer borrowing (`&`) over cloning to avoid extra allocations.

---

### **8. Error Handling & Debugging**

* **Error Handling:** No exceptions; explicit `Result<T,E>` type.

  ```rust
  fn divide(a: i32, b: i32) -> Result<i32, String> {
      if b == 0 { Err("Divide by zero".to_string()) } else { Ok(a / b) }
  }
  ```
* **Common Pitfalls:** Borrow checker errors, lifetime annotations, verbose pointer management with `Box`/`Rc`.
* **Debugging Support:** `println!("{:?}", var)` for debugging; IDE debuggers (VSCode, CLion).

---

### **9. Community & Resources**

* **Documentation:** [Rust Standard Library](https://doc.rust-lang.org/std/)
* **LeetCode Tips:** Rust ensures memory safety and correctness but is verbose for pointer-heavy structures like linked lists and binary trees. Great for DP, array, string, and graph problems.
* **Third-party Libraries:** Not allowed on LeetCode; only standard Rust library available.

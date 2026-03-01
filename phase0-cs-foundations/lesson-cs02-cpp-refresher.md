# Lesson CS-02: C++ Refresher — Memory, Pointers, and the STL

[← Python Refresher](lesson-cs01-python-refresher.md) | [Back to TOC](../README.md) | [Next: OOP →](lesson-cs03-oop.md)

---

> **Why this lesson exists:** C++ forces you to think about what the computer is actually doing — memory layout, pointers, stack vs heap. This low-level awareness makes you a better programmer in *any* language and connects directly to understanding how neural networks use memory (GPU tensors, memory-bound vs compute-bound operations). Plus, many competitive programming solutions and systems-level ML tools (CUDA kernels, ONNX runtime) are C++.

## 🎯 Core Skills

### Basics — Syntax You Need to Remember

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    // Variables and types
    int x = 5;
    double pi = 3.14159;
    string name = "Claude";
    bool flag = true;

    // I/O
    cout << "Hello " << name << endl;
    cin >> x;  // read from stdin

    // Strings
    string s = "hello";
    s.length();         // 5
    s.substr(1, 3);     // "ell"
    s.find("ll");       // 2 (or string::npos if not found)
    s += " world";      // concatenation
    
    return 0;
}
```

### Pointers and References

- **Pointer:** `int* p = &x;` — p holds the *address* of x. `*p` dereferences (gets the value).
- **Reference:** `int& r = x;` — r is an alias for x. No new memory, just another name.
- **When to use which:** pass by reference (`void func(vector<int>& v)`) to avoid copying large objects. Use pointers for linked data structures (nodes pointing to next nodes) and when you need nullable (`nullptr`).
- **`new`/`delete`:** heap allocation. `int* p = new int(5);` ... `delete p;`. In practice, prefer smart pointers or STL containers.

### Stack vs Heap

- **Stack:** local variables, function call frames. Fast, automatic cleanup. Fixed size.
- **Heap:** `new`/`malloc`. Manual management (or smart pointers). Slower, but flexible size.
- **Why this matters:** understanding stack vs heap is understanding how a computer actually runs your program. When a function calls another function, a new frame goes on the stack. When it returns, the frame is popped. Recursion = deep stack.

### The STL — Your Toolbox

```cpp
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <algorithm>

// Vector (dynamic array)
vector<int> v = {1, 2, 3};
v.push_back(4);
v.pop_back();
v.size();
v[0];               // no bounds check
v.at(0);            // bounds check (throws)

// Unordered map (hash map)
unordered_map<string, int> m;
m["key"] = 42;
m.count("key");     // 1 if exists, 0 if not
m.find("key");      // iterator (or m.end())

// Unordered set (hash set)
unordered_set<int> s = {1, 2, 3};
s.insert(4);
s.count(3);         // 1 or 0

// Stack and Queue
stack<int> stk;
stk.push(1); stk.top(); stk.pop();

queue<int> q;
q.push(1); q.front(); q.pop();

// Priority queue (max-heap by default)
priority_queue<int> pq;
priority_queue<int, vector<int>, greater<int>> min_pq; // min-heap

// Sorting
sort(v.begin(), v.end());
sort(v.begin(), v.end(), [](int a, int b) { return a > b; }); // descending
```

### Iteration Patterns

```cpp
// Range-based for (modern C++)
for (int x : v) { cout << x; }
for (auto& [key, val] : m) { cout << key << val; }

// Iterator-based
for (auto it = v.begin(); it != v.end(); ++it) { ... }
```

## 📺 Watch

1. **NeetCode — "C++ for Coding Interviews"**
   - Search NeetCode's channel for C++ specific tips

## 🔨 Practice Problems

Solve each in C++. Focus on getting comfortable with STL containers.

1. **Two Sum** (LeetCode #1) — solve again, but in C++ using `unordered_map`.
2. **Valid Parentheses** (LeetCode #20) — use `stack<char>`.
3. **Reverse a string in-place** (LeetCode #344) — two-pointer approach on a `vector<char>`.
4. **Implement a linked list from scratch** — `struct ListNode { int val; ListNode* next; };`. Insert, delete, print.
5. **Merge two sorted arrays** (LeetCode #88) — practice pointer/index manipulation.
6. **Group Anagrams** (LeetCode #49) — use `unordered_map<string, vector<string>>` with sorted keys.

## 🔗 ML Connection

CUDA kernels (the code that actually runs on GPUs) are C++. Understanding memory layout — contiguous arrays, cache lines, pointer chasing — explains why matrix multiplication is fast (contiguous memory access) and why linked lists are slow (scattered memory, cache misses). When you later learn about tensor memory layout in PyTorch, this foundation pays off.

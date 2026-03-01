# Lesson CS-03: Object-Oriented Programming — Classes in Python & C++

[← C++ Refresher](lesson-cs02-cpp-refresher.md) | [Back to TOC](../README.md) | [Next: Arrays & Hashing →](lesson-cs04-arrays-hashing.md)

---

> **Why this lesson exists:** Every ML framework is built on classes — `torch.nn.Module`, `torch.Tensor`, `Dataset`, `DataLoader`. If you can't read and write classes fluently, you can't read ML code. This lesson rebuilds that fluency in both Python and C++.

## 🎯 Core Concepts

### Python Classes

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name          # instance attribute
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __repr__(self):           # how it prints
        return f"Animal({self.name!r})"

class Dog(Animal):                # inheritance
    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self, item):        # new method
        return f"{self.name} fetches {item}"

rex = Dog("Rex")
rex.speak()       # "Rex says Woof"
rex.fetch("ball") # "Rex fetches ball"
isinstance(rex, Animal)  # True
```

**Key patterns:**
- `__init__` = constructor
- `self` = reference to the instance (explicit in Python, implicit `this` in C++)
- `super()` = call parent class
- **Dunder methods:** `__repr__`, `__str__`, `__len__`, `__eq__`, `__lt__` (for sorting), `__add__` (operator overloading)
- **`@property`:** make a method look like an attribute. Used everywhere in PyTorch.

### C++ Classes

```cpp
class Animal {
protected:                        // accessible by subclasses
    string name;
    string sound;
public:
    Animal(string n, string s) : name(n), sound(s) {}  // constructor + initializer list
    virtual string speak() {      // virtual = can be overridden
        return name + " says " + sound;
    }
    virtual ~Animal() {}          // virtual destructor
};

class Dog : public Animal {
public:
    Dog(string n) : Animal(n, "Woof") {}
    string fetch(string item) {
        return name + " fetches " + item;
    }
};
```

**Key differences from Python:**
- `public/private/protected` access specifiers
- `virtual` keyword for polymorphism
- Initializer lists (`: name(n), sound(s)`)
- Destructors (`~Animal()`) for cleanup
- No `self` — `this` is implicit

### The Four Pillars (What Interviewers Ask)

1. **Encapsulation:** bundle data + methods, hide internals. Private attributes, public interface.
2. **Inheritance:** `Dog` IS-A `Animal`. Reuse + specialize.
3. **Polymorphism:** call `animal.speak()` and the *right* version runs based on actual type. In C++, requires `virtual`.
4. **Abstraction:** expose what matters, hide how it works. Like `model.forward(x)` — you don't need to know the internals to use it.

### PyTorch Example — Why This Matters

```python
import torch.nn as nn

class SimpleNet(nn.Module):       # inheritance from Module
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()        # init parent
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):         # polymorphism — Module calls this
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return x
```

Every neural network you'll build follows this exact pattern.

## 🔨 Practice Problems

1. **Implement a Stack class** (Python) with `push`, `pop`, `peek`, `is_empty`, `__len__`, `__repr__`. Use a list internally.
2. **Implement a MinStack** (LeetCode #155) — stack that also returns the minimum in O(1). Hint: store (value, current_min) pairs.
3. **Implement a Binary Search Tree class** (Python or C++) — `insert`, `search`, `inorder_traversal`. Node is a nested class.
4. **Design a HashMap** (LeetCode #706) — implement `put`, `get`, `remove` using an array of linked lists (chaining).
5. **Port your Stack class to C++** — practice translating between the two languages.

## 🔗 ML Connection

The entire PyTorch ecosystem is class hierarchies: `nn.Module` → `nn.Linear`, `nn.Conv2d`, etc. TransformerLens (which you'll use for interpretability) subclasses these. Understanding OOP means you can read any model's source code, modify architectures, and build custom layers — essential for alignment research where you need to inspect and intervene on model internals.

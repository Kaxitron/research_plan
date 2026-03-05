# Lesson CS-10: Computer Organization — How Code Actually Runs

[← Discrete Math](lesson-cs09-discrete-math.md) | [Back to TOC](../README.md) | [Next: Python & NumPy →](../phase0-setup/lesson-00-python-numpy.md)

---

> **Why this lesson exists:** When you run `model.forward(x)`, billions of floating-point multiplications happen on physical hardware. Understanding the layers between your Python code and the transistors — binary representation, memory hierarchy, instruction execution — explains *why* matrix multiplication is fast, why GPU training works, and why certain model architectures are more hardware-efficient than others.

## 🎯 Core Concepts

### Binary and Number Representation

- **Binary:** base-2. Each digit (bit) is 0 or 1. `13 = 1101₂ = 8+4+0+1`.
- **Converting:** decimal → binary (repeated division by 2). Binary → decimal (sum of powers of 2).
- **Hexadecimal:** base-16 (0-9, A-F). Each hex digit = 4 bits. `0xFF = 11111111₂ = 255`.
- **Two's complement (signed integers):** flip all bits, add 1 to get the negative. For 8 bits: range is −128 to 127. The leftmost bit is the sign bit.
- **Floating point (IEEE 754):** sign bit + exponent + mantissa. `float32` has ~7 decimal digits of precision. `float16` has ~3. This is why ML uses mixed precision — `float16` is faster but loses precision.
- **Overflow/underflow:** numbers too large or too small for the representation. In ML, gradient underflow in `float16` is why loss scaling exists.

### Bitwise Operations

```python
a & b     # AND — both bits 1
a | b     # OR — either bit 1
a ^ b     # XOR — bits differ
~a        # NOT — flip all bits
a << n    # left shift (multiply by 2^n)
a >> n    # right shift (divide by 2^n)
```

Used in hashing, masking, and low-level optimization. LeetCode loves these.

### Memory Hierarchy

```
                Speed       Size        Cost
Registers       < 1 ns      ~1 KB       $$$$$
L1 Cache        ~1 ns       ~64 KB      $$$$
L2 Cache        ~5 ns       ~256 KB     $$$
L3 Cache        ~10 ns      ~8 MB       $$
RAM (DRAM)      ~100 ns     ~16 GB      $
SSD             ~100 μs     ~1 TB       ¢
HDD             ~10 ms      ~4 TB       ¢
```

**The key insight:** accessing RAM is ~100× slower than L1 cache. Programs that access memory *sequentially* (arrays, matrices) are fast because the cache pre-fetches nearby data. Programs that jump around (linked lists, pointer chasing) are slow because every access is a cache miss. **This is why matrix multiplication is fast and graph traversal is slow — it's about memory access patterns.**

### How a Program Executes

1. **Source code** (Python/C++) → **compiler/interpreter** → **machine instructions**
2. **CPU fetch-decode-execute cycle:** fetch instruction from memory → decode what it means → execute it → repeat
3. **Registers:** tiny, ultra-fast storage inside the CPU. Operations happen register-to-register.
4. **The stack:** function calls push frames (local variables, return address). Returns pop them.
5. **The heap:** dynamically allocated memory (`new`, `malloc`, Python objects). Slower, managed by garbage collector (Python) or manually (C++).

### Assembly — A Taste

You don't need to write assembly, but reading a few lines demystifies what the CPU does:

```asm
mov eax, 5      ; put 5 in register eax
add eax, 3      ; eax = eax + 3 = 8
mov [0x100], eax ; store 8 at memory address 0x100
cmp eax, 10     ; compare eax with 10
jl loop_start   ; jump to loop_start if eax < 10
```

Every line of Python eventually becomes something like this. A `for` loop is a `cmp` + conditional `jump`. A function call is a `push` (save registers) + `jump` + `pop` (restore registers) + `return`.

### CPU vs GPU — Why ML Uses GPUs

- **CPU:** few cores (4–16), very fast, good at complex sequential logic.
- **GPU:** thousands of cores, each slower, good at doing the *same simple operation on lots of data simultaneously*.
- **Matrix multiplication is embarrassingly parallel:** each output element is an independent dot product. This maps perfectly to GPU architecture.
- **Memory bandwidth** is often the bottleneck, not compute. Moving data between CPU RAM ↔ GPU memory is slow. This is why batching matters — amortize the transfer cost over many examples.

## 📺 Watch

1. **Crash Course Computer Science — "How Computers Calculate" (#5)** and **"Registers and RAM" (#6)**
   - Quick, visual overview of how hardware works
2. **Ben Eater — "Building an 8-bit breadboard computer"** (optional, fascinating)
   - Watch the first few videos to see a CPU built from scratch with logic gates

## 🔨 Practice

1. **Binary conversions:** convert 42, 255, and −7 (8-bit two's complement) to binary by hand. Convert `10110011₂` to decimal.
2. **Floating point exploration:** in Python, compute `0.1 + 0.2`. Why isn't it exactly 0.3? Compute `1e16 + 1 - 1e16`. Why is the result 0?
3. **Cache experiment:** write a program that accesses a large array sequentially vs randomly. Time both. Observe the cache effect.
4. **Stack trace:** write a recursive function and deliberately cause a stack overflow. Read the error message — it tells you the call depth.

### Bit Manipulation (NeetCode 150)

| # | Problem | Category | Pattern | Difficulty |
|---|---------|----------|---------|------------|
| 1 | [Single Number](https://leetcode.com/problems/single-number/) | Bit Manipulation | XOR all elements | Easy |
| 2 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Bit Manipulation | Bit counting (n & n-1) | Easy |
| 3 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Bit Manipulation | DP + bit manipulation | Easy |
| 4 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Bit Manipulation | Bit shifting | Easy |
| 5 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Bit Manipulation | Bit-level addition (carry + XOR) | Medium |
| 6 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Bit Manipulation | Modular arithmetic + overflow | Medium |

## 🔗 ML Connection

Understanding hardware explains *why* ML works the way it does. Transformers are popular partly because attention is a matrix multiplication (GPU-friendly), unlike RNNs which are sequential (GPU-unfriendly). Mixed precision training (float16) doubles throughput because GPUs have specialized float16 units. Memory hierarchy explains why batch size matters, why gradient accumulation works, and why model parallelism splits layers across GPUs. The hardware isn't incidental to ML — it shapes what architectures succeed.

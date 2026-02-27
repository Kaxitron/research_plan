# Lesson 1: PyTorch — The Language of Alignment Research

[← Python & NumPy](lesson-00-python-numpy.md) | [Back to TOC](../README.md) | [Next: Vectors →](../phase1-linear-algebra/lesson-02-vectors.md)

---

> **Why this lesson exists:** Every alignment research tool — TransformerLens, ARENA exercises, SAE training, activation patching — runs on PyTorch. NumPy teaches you to think in arrays; PyTorch adds autograd (automatic differentiation), GPU acceleration, and the ecosystem that all modern ML research lives in. The jump from NumPy to PyTorch is smaller than you think syntactically, but the conceptual additions (tensors on devices, computation graphs, gradient tracking) are essential. You cannot do ARENA Chapter 1 or use TransformerLens without this.

## 🎯 Core Concepts

### Tensors — NumPy Arrays with Superpowers

- **A PyTorch tensor is a NumPy array that knows how to compute its own gradients.** The syntax is nearly identical: `torch.zeros(3, 4)` instead of `np.zeros((3, 4))`, `A @ v` works the same way, `.T` transposes.
- **Device management:** tensors live on CPU or GPU. `x = x.to('cuda')` moves data to GPU. Operations must happen on the same device. This is the main new friction point compared to NumPy.
- **dtype matters:** `torch.float32` is the default (not float64 like NumPy). Half precision (`float16`, `bfloat16`) is used for large models. Mixed precision training is standard practice.
- **Converting between frameworks:** `torch.from_numpy(arr)` and `tensor.numpy()` share memory (zero-copy). But gradients and device placement don't survive the conversion.

### Autograd — The Key Difference from NumPy

- **`requires_grad=True`** tells PyTorch to track operations on this tensor. Every operation builds a computation graph behind the scenes.
- **`loss.backward()`** walks backward through the computation graph and fills in `.grad` for every tensor that had `requires_grad=True`. This IS backpropagation (Lesson 15), happening automatically.
- **`torch.no_grad()`** context manager disables gradient tracking. Use during inference, evaluation, and when manually updating weights. Forgetting this is a common bug that causes memory leaks.
- **`detach()`** creates a tensor that shares data but is disconnected from the computation graph. Essential for interpretability work where you want to examine intermediate values without affecting gradients.
- **The mental model:** every PyTorch operation is a node in a directed graph. Forward pass builds the graph. `backward()` flows gradients through it. The graph is then destroyed (by default) — PyTorch uses dynamic graphs, rebuilt every forward pass.

### The Training Loop Pattern

Every neural network training in PyTorch follows the same skeleton:

```python
model = MyModel()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for batch in dataloader:
    optimizer.zero_grad()       # Reset gradients from last step
    output = model(batch)       # Forward pass (builds graph)
    loss = loss_fn(output, target)
    loss.backward()             # Backward pass (computes gradients)
    optimizer.step()            # Update weights using gradients
```

- **`zero_grad()`** is necessary because PyTorch *accumulates* gradients by default (useful for gradient accumulation across mini-batches, confusing if you forget).
- **`model.parameters()`** returns all learnable tensors. The optimizer only sees these.
- **`model.eval()` vs `model.train()`** toggles behaviors like dropout and batchnorm. Always switch to eval mode for inference.

### Modules and Models

- **`nn.Module`** is the base class for all neural network components. You define `__init__` (create layers) and `forward` (define computation).
- **`nn.Linear(in, out)`** is a single matrix multiplication + bias: y = Wx + b. This IS the linear transformation from Lesson 4, packaged as a reusable component.
- **`nn.Sequential`** chains layers: `nn.Sequential(nn.Linear(768, 256), nn.ReLU(), nn.Linear(256, 10))`.
- **Hooks** are the critical tool for interpretability. `module.register_forward_hook(fn)` lets you intercept and inspect (or modify) intermediate activations as they flow through the network. TransformerLens is essentially a sophisticated hook management system.

### Einops and Einsum — Tensor Manipulation for Research

- **`einops.rearrange`** reshapes tensors with named dimensions: `rearrange(x, 'batch seq d_model -> batch seq heads d_head', heads=12)`. Far more readable than chains of `.view()`, `.permute()`, `.transpose()`.
- **`torch.einsum`** computes arbitrary tensor contractions: `torch.einsum('ij,jk->ik', A, B)` is matrix multiplication. `torch.einsum('bsh,bth->bst', Q, K)` computes attention scores. Once you learn the notation, it replaces dozens of specialized functions.
- **These are ARENA prerequisites.** The first ARENA exercise set drills einops and einsum heavily.

### DataLoaders and Batching

- **`Dataset`** wraps your data. **`DataLoader`** handles batching, shuffling, and parallel loading.
- **Batching** is why you need to think in terms of tensor dimensions: a single image is `(C, H, W)`, a batch is `(B, C, H, W)`. A single token sequence is `(seq_len, d_model)`, a batch is `(batch, seq_len, d_model)`.
- **Collate functions** handle variable-length sequences (padding, attention masks). This is the practical side of why transformers need attention masks.

## 📺 Watch — Primary

1. **PyTorch in 100 Seconds (Fireship)**
   - Quick orientation to what PyTorch is
2. **Andrej Karpathy — "Building micrograd"** (first 30 min)
   - https://www.youtube.com/watch?v=VMj-3S1tku0
   - *You'll do this fully in Lesson 16, but the autograd concept preview is useful here.*

## 📺 Watch — Secondary

3. **Patrick Loeber — "PyTorch Tutorial" (Complete Course)**
   - Search YouTube — covers tensors, autograd, training loops, datasets
4. **ARENA Prerequisites — Einops & Einsum tutorial**
   - https://arena-ch0-fundamentals.streamlit.app/ (Section 0.0)

## 📖 Read — Primary

- **PyTorch 60-Minute Blitz**
  - https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
  - *The official tutorial. Covers tensors, autograd, neural networks, training.*
- **ARENA Chapter 0.0 — Prerequisites**
  - https://arena-ch0-fundamentals.streamlit.app/
  - *Work through the einops and einsum exercises. These are the exact prerequisites ARENA expects.*

## 📖 Read — Secondary

- **Tim Rocktäschel — "Einsum is All You Need"**
  - https://rockt.github.io/2018/04/30/einsum
- **Neel Nanda — TransformerLens documentation**
  - https://neelnanda-io.github.io/TransformerLens/
  - *Skim the API overview to see what hooks look like in practice.*

## 🔨 Do

- **Port your NumPy exercises to PyTorch:** take any matrix operation from Phase 1 (SVD, eigendecomposition, projection) and redo it in PyTorch. Verify identical results.
- **Autograd experiment:** create tensors `W` and `x` with `requires_grad=True`. Compute `y = W @ x`, then `loss = y.sum()`. Call `loss.backward()`. Inspect `W.grad` and `x.grad`. Verify they match what you'd compute by hand.
- **Build a minimal training loop:** train a 2-layer MLP on a toy dataset (e.g., classifying points inside vs. outside a circle). Use `nn.Linear`, `nn.ReLU`, `nn.CrossEntropyLoss`, and `torch.optim.Adam`.
- **Hook exercise:** load any pre-trained model (even a tiny one). Register a forward hook on an intermediate layer. Pass input through and inspect the activations captured by the hook. This is the atomic operation of all interpretability research.
- **Einsum drills:** implement matrix multiplication, batch matrix multiplication, trace, outer product, and attention score computation all using `torch.einsum`.

## 🔗 ML Connection

PyTorch is not just a tool — it shapes how you think about models. When interpretability researchers say "patch the residual stream at layer 5," they mean: register a hook at layer 5 that replaces the activation tensor with a modified one, then observe how downstream computations change. When they say "compute the OV circuit," they mean: extract weight matrices using `model.W_O[layer, head]` and multiply them. The entire workflow of mechanistic interpretability is PyTorch operations on model internals.

## 🧠 Alignment Connection

TransformerLens exists because PyTorch's hook system allows researchers to surgically intervene on model computations. Every technique in ARENA's interpretability chapters — activation patching, direct logit attribution, probing, steering vectors — is a PyTorch operation. The bridge from "understanding the math" to "doing alignment research" runs through PyTorch fluency.

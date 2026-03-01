# Lesson 41: The Forward Pass as Matrix Multiplications

[← Single Neuron](lesson-40-single-neuron.md) | [Back to TOC](../README.md) | [Next: Backpropagation →](lesson-42-backprop.md)

---

## 🎯 Core Learning

- A layer of neurons = single matrix multiplication + bias + activation
- The forward pass: input → layer 1 → layer 2 → ... → output
- This is just composition of functions! f₃(f₂(f₁(x)))
- Batch processing: multiple inputs simultaneously (wider matrices)
- Every matrix IS a linear transformation — Lessons 2-9 apply directly
- Softmax: turning raw scores into probabilities
- **The geometric view:** each ReLU "folds" space; layers compose these folds into rich, piecewise-linear decision boundaries

## 📺 Watch — Primary

1. **Welch Labs — "The Misconception that Almost Stopped AI [How Models Learn Part 1]"**
   - https://www.youtube.com/watch?v=PFDMhdDR_1M
   - *📖 Book: Welch Labs, "The Illustrated Guide to AI," Ch. 2: Gradient Descent + Ch. 4: Deep Learning*
   - *22 minutes. The Belgium/Netherlands map example is PERFECT for your geometric intuition style. Each neuron folds a plane; stacking layers composes folds. You'll see WHY deep networks work. This is the single best visual for understanding what a forward pass actually does to data.*

2. **Karpathy — "Building makemore" (Lecture 2)**
   - https://www.youtube.com/watch?v=PaCmpygFfXo
3. **Karpathy — "Building makemore Part 2: MLP" (Lecture 3)**
   - https://www.youtube.com/watch?v=TCH_1BHY58I

## 📺 Watch — Secondary

4. **Welch Labs — "Why Deep Learning Works Unreasonably Well" (Ch. 4: Deep Learning)**
   - https://www.youtube.com/watch?v=qx7hirqgfuU
   - *Shows why depth matters more than width, with the Belgium/Netherlands example extended to multi-layer networks.*

4. **Nelson Elhage — "Transformers for Software Engineers"** (blog/talk)
   - https://blog.nelhage.com/post/transformers-for-software-engineers/

## 📺 Watch — Optional

5. **Andrej Karpathy — "Building a WaveNet"**
   - https://www.youtube.com/watch?v=t3YJ5hKiMQ0
   - *Extends the makemore series with a more advanced architecture. Optional but deepens understanding of how network depth processes information.*

## 📖 Read

- **Nelson Elhage — "Transformers for Software Engineers"**
  - https://blog.nelhage.com/post/transformers-for-software-engineers/

## 🔨 Do

- Implement a 2-layer MLP from scratch in NumPy (no PyTorch)
- Train on MNIST digit classification
- Visualize weight matrices as images — what patterns do they learn?
- **Key geometric exercise:** For a 2D classification problem, visualize the decision boundary at each layer. Watch the folds happen.

## 🔗 ML & Alignment Connection

The **residual stream** — the running sum that each layer reads from and writes to — is the central object of mechanistic interpretability. When interpretability researchers say "the model moves information through the residual stream," they mean each matrix multiplication's output gets added back to this running total. Understanding the forward pass as composed matrix multiplications is THE prerequisite for reading Anthropic's papers.

The Welch Labs "folding" framing also explains why **depth matters more than width**: adding a layer adds another fold; adding width just makes each fold more complex. Alignment researchers trace how safety-relevant information (e.g., "this request is harmful") flows through the residual stream, which heads amplify or suppress it, and where the model "decides" to refuse or comply. The forward pass isn't just computation; it's a decision-making process you can reverse-engineer.

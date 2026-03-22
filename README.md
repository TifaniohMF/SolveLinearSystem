# 🎯️ SOLVE LINEAR SYSTEM

## 📃 Linear system solver (Ax = b)

A python-based library for solving system of equation linear using matrix decomposition techniques. This projects focuses on numerical stability and efficiency by implemting core algorithms from scratch. 

## 🚀️ Overview

This solver provides tools to decomposed matrix and find solutions for $x$ in the equation $Ax = b$. Instead of using generic inversion methods, it uses specific decomposition based on the properties matrix A.


## 🛠️ Features

The projects implements three decomposition methods:

- **LU decomposition**: Splites a square matrix into a lower triangular matrix ($\mathit{L}$) and upper triangular matrix ($\mathit{U}$). Ideal for general square matrix.
- **QR decomposition**: Decomposes matrix into an orthogonal matrix ($\mathit{O}$) and a upper triangular matrix ($\mathit{R}$). Highly stable and orks non-square matrix.
- **Cholesky decomposition**: An efficient $\mathit{L}\mathit{L}^{T}$ decomposed for **Symetric-Positive-Definite (SPD)** matrices. It is twices as fast as LU.

## 📘️ Support
If you are a few knowlegde, you can explore this document [resolution_system_linear.pdf](../SolveLinearSystem/docs/resolution_system_linear.pdf)


## 📁️ Project structure
```text
SolveLinearSystem/
├── decomposition
│   ├── cholesky.py
│   ├── lu.py
│   └── qr.py
├── docs
│   ├── example.pdf
│   ├── example.tex
│   ├── resolution_system_linear.pdf
│   └── resolution_system_linear.tex
├── LICENSE
├── main.py
├── README.md
├── requirement.txt
├── solver.py
└── test_decomposition.py

```

## 💻️ Usage

### Prerequisites
- Python 3.x
- Numpy (for matrix storage and operation)

## 📝️ Example
If you want solve a linear system, You can use the three decomposition.
Imagine we solve the linear system $Ax=b$.
You can see the step to use this repository, in this document [example.pdf](../SolveLinearSystem/docs/example.pdf)

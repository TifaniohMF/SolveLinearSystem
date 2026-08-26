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
└── test_solver.py

```

## 💻️ Usage

### Prerequisites
- Python 3.x
- Numpy (for matrix storage and operation)
- Git

### Install and use
1.Clone repository
```bash
git clone https://github.com/TifaniohMF/SolveLinearSystem.git
cd SolveLinearSystem
```
2.Use
You can see the use in example undermentioned.

## 💾 Save to data base
If you want to save the data in Systems linear as solution, systems, coefficient in a data base.
In file main.py, write your systems to solve with a method to use it.
Then, compile with command
```bash
python3 main.py
```
A file Linear_system.db is generated automaticaly with your data.
If you do a other system linear to solve and you compile the file the data is saving in data base Linear_system.db.

## 📝️ Example
If you want solve a linear system, You can use the three decomposition.
Imagine we solve the linear system $Ax=b$.
You can see the step to use this repository, in this document [example.pdf](../SolveLinearSystem/docs/example.pdf)

## 🧮 Test
If you are not sure that this program is unreliable.
Execute this command
```bash
cd SolveLinearSystem
```
```bash
pytest test_solver.py
```

## 🔎 Numerical certificate

`solve_linear_system` validates the matrix and right-hand side before solving.
Pass `return_certificate=True` to receive the solution together with a
machine-readable certificate containing the residual norm, backward error,
condition estimate, numerical rank, and reliability warnings:

```python
x, certificate = solve_linear_system(A, b, method="QR", return_certificate=True)
print(certificate["residual_norm_inf"])
```

The SQLite repository stores one solution per system and reconstructs
coefficients through `system_id`. Generated database files are local runtime
artifacts and should not be committed.
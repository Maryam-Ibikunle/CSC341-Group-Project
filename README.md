# CSC341 — Data Structures: Group 9 Projects

> Implementations of core data structures and algorithms in C and Python, developed as part of the CSC341 Data Structures course.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Projects](#projects)
  - [Project 1 — Array Insertion Operations (C)](#project-1--array-insertion-operations-c)
  - [Project 2 — AVL Tree (Python)](#project-2--avl-tree-python)
  - [Project 3 — B+ Tree (Python)](#project-3--b-tree-python)
  - [Project 4 — Binary Search Tree (Python)](#project-4--binary-search-tree-python)
  - [Project 5 — B-Tree (Python)](#project-5--b-tree-python)
  - [Project 6 — Graph Traversal (Python)](#project-6--graph-traversal-python)
- [Prerequisites](#prerequisites)
- [Contributors](#contributors)
- [License](#license)

---

## Overview

This repository contains six programs implementing foundational data structures and algorithms covered in CSC341. The projects span two languages — C for low-level memory and pointer work, and Python for higher-level tree and graph implementations.

| Topic                      | File             | Language |
| -------------------------- | ---------------- | -------- |
| Array Insertion Operations | `array_insert.c` | C        |
| AVL Tree                   | `avl.py`         | Python   |
| B+ Tree                    | `bplustree.py`   | Python   |
| Binary Search Tree         | `bst.py`         | Python   |
| B-Tree                     | `btree.py`       | Python   |
| Graph Traversal            | `graph.py`       | Python   |

---

## Repository Structure

```
CSC341-Group-Project/
├── array_insert.c     # Project 1 — Array insertion in C
├── avl.py             # Project 2 — AVL Tree
├── bplustree.py       # Project 3 — B+ Tree
├── bst.py             # Project 4 — Binary Search Tree
├── btree.py           # Project 5 — B-Tree
├── graph.py           # Project 6 — Graph Traversal
└── README.md
```

---

## Projects

---

### Project 1 — Array Insertion Operations (C)

**File:** `array_insert.c` | **Language:** C

Demonstrates pointer usage and dynamic array manipulation in C. Covers four insertion scenarios on a fixed-size array, plus a pointer demo using `doubleIt()`.

**Functions:**

| Function              | Description                                      |
| --------------------- | ------------------------------------------------ |
| `insertAtBeginning()` | Shifts all elements right and inserts at index 0 |
| `insertAtIndex()`     | Inserts at a specified position                  |
| `insertBeforeIndex()` | Inserts immediately before a given index         |
| `insertAfterIndex()`  | Inserts immediately after a given index          |
| `printArray()`        | Displays current array contents                  |
| `doubleIt()`          | Doubles a variable's value via pointer           |

**Compile and run:**

```bash
gcc array_insert.c -o array_insert
./array_insert
```

**Expected output:**

```
=== Pointer Demo ===
Before doubleIt: x = 5
After doubleIt: x = 10

The address of x is: 0x... (varies by machine)
The value at that address is: 10

=== Scenario 1: Insert at Beginning ===
Before: [10, 20, 30, 40, 50]
After:  [5, 10, 20, 30, 40, 50]
n is now: 6

=== Scenario 2: Insert at Index ===
Before: [10, 20, 30, 40, 50]
After:  [10, 20, 99, 30, 40, 50]
n is now: 6

=== Scenario 3: Insert Before Index ===
Before: [10, 20, 30, 40, 50]
After:  [10, 20, 30, 77, 40, 50]
n is now: 6

=== Scenario 4: Insert After Index ===
Before: [10, 20, 30, 40, 50]
After:  [10, 20, 55, 30, 40, 50]
n is now: 6
```

> **Note:** The memory address printed in the Pointer Demo will differ on every machine — that is expected.

---

### Project 2 — AVL Tree (Python)

**File:** `avl.py` | **Language:** Python 3

Implements a self-balancing AVL Tree. After every insertion, the tree checks balance factors and performs the appropriate rotation to keep the height-difference ≤ 1 across all nodes.

**Rotations supported:** Left, Right, Left-Right, Right-Left

**Run:**

```bash
python avl.py
```

**Expected output:**

```
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[40, 20, 10, 30, 80, 60, 50, 70, 90, 100]
[10, 30, 20, 50, 70, 60, 100, 90, 80, 40]
10
```

The four lines are: **Inorder** (sorted ascending), **Preorder** (root first), **Postorder** (root last), and the **minimum value** in the tree.

---

### Project 3 — B+ Tree (Python)

**File:** `bplustree.py` | **Language:** Python 3

Implements a B+ Tree (order 4). All values are stored in leaf nodes, which are linked together to support efficient range queries. Internal nodes only store routing keys.

**Operations:**

| Method                    | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `insert(key)`             | Adds a key; splits nodes automatically when full |
| `search(key)`             | Returns `True` if key exists, `False` otherwise  |
| `range_query(start, end)` | Returns all keys in the inclusive range          |

**Run:**

```bash
python bplustree.py
```

**Expected output:**

```
B+ Tree Demo
Inserted: [5, 15, 25, 35, 45, 10, 20, 30]
Search 15: True
Search 99: False
Range query 10-30: [10, 15, 20, 25, 30]
Range query 1-50: [5, 10, 15, 20, 25, 30, 35, 45]
```

---

### Project 4 — Binary Search Tree (Python)

**File:** `bst.py` | **Language:** Python 3

Implements a standard BST with recursive insert, search, delete, and all three depth-first traversals. Demonstrates deletion by removing node 3 after the initial traversals.

**Run:**

```bash
python bst.py
```

**Expected output:**

```
1          ← Inorder (sorted)
2
3
4
5
6
7
8
9
5          ← Preorder (root-first)
3
1
2
4
7
6
8
9
2          ← Postorder (leaves-first)
1
4
3
6
9
8
7
5
True       ← search(4)
False      ← search(10)
1          ← Inorder after deleting node 3
2
4
5
6
7
8
9
```

---

### Project 5 — B-Tree (Python)

**File:** `btree.py` | **Language:** Python 3

Implements a B-Tree with minimum degree `t=2` (order 4). Unlike a B+ Tree, internal nodes also store keys. Supports balanced insertions with automatic node splitting.

**Run:**

```bash
python btree.py
```

**Expected output:**

```
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[40, 20, 10, 30, 60, 80, 50, 70, 90, 100]
[10, 30, 20, 50, 70, 90, 100, 60, 80, 40]
10
```

The four lines are: **Inorder** (sorted), **Preorder**, **Postorder**, and the **minimum value**.

---

### Project 6 — Graph Traversal (Python)

**File:** `graph.py` | **Language:** Python 3

Implements an undirected weighted graph using an adjacency list. Demonstrates BFS and DFS traversals, path checking, and edge removal.

**Graph structure used in the demo:**

```
A — B — D — E
|       |
C ——————
```

**Run:**

```bash
python graph.py
```

**Expected output:**

```
Graph Demo
A -> [B(w=1), C(w=1)]
B -> [A(w=1), D(w=1)]
C -> [A(w=1), D(w=1)]
D -> [B(w=1), C(w=1), E(w=1)]
E -> [D(w=1)]
BFS from A: ['A', 'B', 'C', 'D', 'E']
DFS from A: ['A', 'B', 'D', 'C', 'E']
Neighbors of D: ['B', 'C', 'E']
Has path A -> E: True
Has path E -> A: True
After removing D-E, has path A -> E: False
```

---

## Prerequisites

**For Project 1 (C):**

- GCC compiler
  - Ubuntu/Debian: `sudo apt install gcc`
  - macOS: `xcode-select --install`
  - Windows: Install [MinGW](https://www.mingw-w64.org/)

**For Projects 2–6 (Python):**

- Python 3.x — [Download here](https://www.python.org/downloads/)
- No external packages required; all implementations use the Python standard library only.

---

## Contributors

| Name                                   | Student ID |
| -------------------------------------- | ---------- |
| Mubarak Moyosore Mustapha (Group Lead) | 243464     |
| Okechukwu Jachike Edward               | 243750     |
| Enyimba Gabriel Chibuike               | 243452     |
| Ipeayeda Oluwadamilola Faith           | 244053     |
| Ibikunle Maryam Ibidoyin               | 243455     |
| Odunsanya Simisola Joy                 | 244206     |
| Aniakor Chidubem John Paul             | 243671     |
| Michael Chidera Olamide                | 243463     |

---

## License

This project was created for educational purposes as part of the CSC341 Data Structures course. Not intended for commercial use.

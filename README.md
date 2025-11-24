# Grey Wolf Optimizer (GWO) -- Python Implementation

This repository contains a clean and professional implementation of the
**Grey Wolf Optimizer (GWO)** algorithm using Python.\
GWO is a **nature‑inspired metaheuristic optimization algorithm** that
mimics the leadership hierarchy and hunting strategy of grey wolves in
nature.

------------------------------------------------------------------------

## 🐺 Overview

The Grey Wolf Optimizer (GWO) is widely used for solving continuous
optimization problems thanks to its simplicity, fast convergence, and
ability to escape local minima.\
This project includes:

-   Full implementation of the GWO algorithm\
-   Several benchmark functions (Sphere, Rastrigin, Rosenbrock)\
-   A demo script with command‑line arguments\
-   Automatic convergence curve plotting

------------------------------------------------------------------------

## 📁 Project Structure

    GWO_Project/
    ├── gwo.py        # Core GWO algorithm implementation
    ├── fitness.py    # Benchmark functions
    ├── demo.py       # Script to run GWO (CLI)
    ├── plot.py       # Optional plotting utilities
    ├── README.md     # Project documentation

------------------------------------------------------------------------

## ⚙️ Requirements

-   Python 3.x\
-   Libraries:
    -   `numpy`
    -   `matplotlib`

Install dependencies:

``` bash
pip install numpy matplotlib
```

------------------------------------------------------------------------

## 🚀 Usage

Run the optimizer from the terminal using:

``` bash
python demo.py --function FUNCTION --dim DIMENSIONS --wolves WOLVES --iter ITERATIONS
```

### Examples

``` bash
python demo.py --function sphere --dim 2 --wolves 30 --iter 200
python demo.py --function rastrigin --dim 5 --wolves 50 --iter 300
python demo.py --function rosenbrock --dim 10 --wolves 40 --iter 500
```

------------------------------------------------------------------------

## 📊 Output

The program displays:

-   **Best position** found\
-   **Best fitness score**\

------------------------------------------------------------------------

## 🧪 Benchmark Functions Included

-   **Sphere**\
-   **Rastrigin**\
-   **Rosenbrock**

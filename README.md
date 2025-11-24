Grey Wolf Optimizer (GWO) in Python
Project Description

This project implements the Grey Wolf Optimizer (GWO) algorithm in Python.
GWO is a nature-inspired metaheuristic algorithm based on the social hierarchy and hunting behavior of grey wolves.

The project allows you to optimize benchmark functions like Sphere, Rastrigin, and Rosenbrock.

Folder Structure
GWO_Project/
├── gwo.py       # GWO algorithm implementation
├── fitness.py   # Benchmark functions
├── demo.py      # Script to run GWO with command-line arguments
├── plot.py      # (optional) Plotting functions
├── README.md    # Project documentation

Requirements

Python 3.x

Libraries:

numpy

matplotlib

Install required libraries:

pip install numpy matplotlib

Usage

Run GWO for a specific function with:

python demo.py --function FUNCTION --dim DIMENSIONS --wolves WOLVES --iter ITERATIONS


Examples:

python demo.py --function sphere --dim 2 --wolves 30 --iter 200
python demo.py --function rastrigin --dim 5 --wolves 50 --iter 300
python demo.py --function rosenbrock --dim 10 --wolves 40 --iter 500


Outputs:

Best position → optimal solution found

Best score → function value at that solution

Convergence plot (automatically displayed)

Benchmark Functions

Sphere

Rastrigin

Rosenbrock

Author

Farah Abdelhedi – ENIS, Computer Science & Applied Mathematics
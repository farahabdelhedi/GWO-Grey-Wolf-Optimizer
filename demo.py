# demo.py
from gwo import GWO
from fitness import sphere, rastrigin, rosenbrock
from plot import plot_convergence
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--function", choices=["sphere","rastrigin","rosenbrock"], default="sphere")
parser.add_argument("--dim", type=int, default=2)
parser.add_argument("--wolves", type=int, default=30)
parser.add_argument("--iter", type=int, default=200)
args = parser.parse_args()

func_map = {"sphere": sphere, "rastrigin": rastrigin, "rosenbrock": rosenbrock}
f = func_map[args.function]

gwo = GWO(fitness_func=f, dim=args.dim, wolves=args.wolves, iterations=args.iter, lb=-5, ub=5)
best_pos, best_score = gwo.optimize()
print("Best position:", best_pos)
print("Best score:", best_score)
plot_convergence(gwo.best_history, title=f"GWO on {args.function}")

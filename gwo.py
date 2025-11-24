# gwo.py
import numpy as np

class GWO:
    def __init__(self, fitness_func, dim, wolves=30, iterations=200, lb=-10, ub=10, minimize=True):
        self.fitness = fitness_func
        self.dim = dim
        self.wolves = wolves
        self.iterations = iterations
        self.lb = lb
        self.ub = ub
        self.minimize = minimize

        # positions and history
        self.positions = np.random.uniform(low=self.lb, high=self.ub, size=(self.wolves, self.dim))
        self.best_history = []

    def _evaluate(self, positions):
        return np.array([self.fitness(pos) for pos in positions])

    def optimize(self):
        # initialize leaders
        fitness_vals = self._evaluate(self.positions)
        idx = fitness_vals.argsort()
        alpha = self.positions[idx[0]].copy()
        beta  = self.positions[idx[1]].copy()
        delta = self.positions[idx[2]].copy()

        best_score = fitness_vals[idx[0]]
        self.best_history = [best_score]

        for t in range(1, self.iterations+1):
            a = 2 - t * 2.0 / self.iterations  # a decreases linearly from 2 to 0

            for i in range(self.wolves):
                X = self.positions[i].copy()
                r1 = np.random.rand(self.dim)
                r2 = np.random.rand(self.dim)

                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = np.abs(C1 * alpha - X)
                X1 = alpha - A1 * D_alpha

                r1 = np.random.rand(self.dim); r2 = np.random.rand(self.dim)
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_beta = np.abs(C2 * beta - X)
                X2 = beta - A2 * D_beta

                r1 = np.random.rand(self.dim); r2 = np.random.rand(self.dim)
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_delta = np.abs(C3 * delta - X)
                X3 = delta - A3 * D_delta

                X_new = (X1 + X2 + X3) / 3.0
                # clip to bounds
                X_new = np.clip(X_new, self.lb, self.ub)
                self.positions[i] = X_new

            # evaluate
            fitness_vals = self._evaluate(self.positions)
            idx = fitness_vals.argsort()
            alpha = self.positions[idx[0]].copy()
            beta  = self.positions[idx[1]].copy()
            delta = self.positions[idx[2]].copy()
            best_score = fitness_vals[idx[0]]
            self.best_history.append(best_score)

        return alpha, best_score

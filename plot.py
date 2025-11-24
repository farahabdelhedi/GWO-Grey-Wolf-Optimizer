# plot.py
import matplotlib.pyplot as plt

def plot_convergence(history, title="GWO Convergence"):
    plt.figure(figsize=(8,4))
    plt.plot(history, linewidth=2)
    plt.xlabel("Iteration")
    plt.ylabel("Best Fitness")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

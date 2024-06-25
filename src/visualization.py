import matplotlib.pyplot as plt


def plot_metrics(metrics, filename="metrics.png"):
    plt.figure(figsize=(10, 5))
    for metric, values in metrics.items():
        plt.plot(values, label=metric)
    plt.xlabel("Iterations")
    plt.ylabel("Values")
    plt.legend()
    plt.savefig(filename)
    plt.close()


# Example usage
metrics = {
    "accuracy": [0.9, 0.91, 0.92],
    "precision": [0.88, 0.89, 0.9],
    "recall": [0.87, 0.88, 0.89],
    "f1_score": [0.88, 0.89, 0.9],
}
plot_metrics(metrics)

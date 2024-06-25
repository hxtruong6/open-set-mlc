import csv


class EvaluationBase:
    def evaluate(self):
        raise NotImplementedError

    def write_results_to_csv(self, results, filename, fieldnames):
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

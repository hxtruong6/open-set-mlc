import time
from evaluation_base import EvaluationBase


class ScalabilityTesting(EvaluationBase):
    def __init__(self, system, increasing_data):
        self.system = system
        self.increasing_data = increasing_data

    def evaluate(self):
        performance_metrics = []
        for data in self.increasing_data:
            start_time = time.time()
            self.system.process_streaming_data(data)
            end_time = time.time()
            total_time = end_time - start_time
            performance_metrics.append(
                {"Dataset Size": len(data), "Processing Time": total_time}
            )
        self.write_results_to_csv(
            performance_metrics,
            "scalability_results.csv",
            ["Dataset Size", "Processing Time"],
        )
        return performance_metrics

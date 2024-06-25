import time
from evaluation_base import EvaluationBase


class StreamingPerformanceMeasurement(EvaluationBase):
    def __init__(self, system, stream_data):
        self.system = system
        self.stream_data = stream_data

    def evaluate(self):
        start_time = time.time()
        for instance in self.stream_data:
            self.system.process_streaming_data()
        end_time = time.time()
        total_time = end_time - start_time
        throughput = len(self.stream_data) / total_time
        results = [{"Total Time": total_time, "Throughput": throughput}]
        self.write_results_to_csv(
            results, "streaming_performance.csv", ["Total Time", "Throughput"]
        )
        return total_time, throughput

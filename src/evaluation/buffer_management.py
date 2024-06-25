from evaluation_base import EvaluationBase


class BufferManagement(EvaluationBase):
    def __init__(self, buffer):
        self.buffer = buffer

    def evaluate(self):
        buffer_stats = {
            "Number of Instances": len(self.buffer.instances),
            "Buffer Full": self.buffer.is_threshold_reached(),
        }
        self.write_results_to_csv(
            [buffer_stats],
            "buffer_management_stats.csv",
            ["Number of Instances", "Buffer Full"],
        )
        return buffer_stats

import psutil
from evaluation_base import EvaluationBase


class ResourceUtilization(EvaluationBase):
    def evaluate(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_io = (
            psutil.disk_io_counters().read_bytes + psutil.disk_io_counters().write_bytes
        )
        results = [
            {"CPU Usage": cpu_usage, "Memory Usage": memory_usage, "Disk I/O": disk_io}
        ]
        self.write_results_to_csv(
            results,
            "resource_utilization.csv",
            ["CPU Usage", "Memory Usage", "Disk I/O"],
        )
        return cpu_usage, memory_usage, disk_io

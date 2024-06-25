from evaluation_base import EvaluationBase
from evaluate_model import ModelEvaluation


class StreamingPerformance(EvaluationBase):
    def __init__(self, system, stream_data):
        self.system = system
        self.stream_data = stream_data

    def evaluate(self):
        performance_metrics = {
            "accuracy": [],
            "precision": [],
            "recall": [],
            "f1_score": [],
        }

        for instance in self.stream_data:
            labels = self.system.mlc_model.predict_labels(instance)
            true_labels = instance[
                "labels"
            ]  # Assuming ground truth labels are available
            model_eval = ModelEvaluation(
                self.system.mlc_model.model, [instance["data"]], [true_labels]
            )
            results = model_eval.evaluate()[0]
            performance_metrics["accuracy"].append(results["Accuracy"])
            performance_metrics["precision"].append(results["Precision"])
            performance_metrics["recall"].append(results["Recall"])
            performance_metrics["f1_score"].append(results["F1 Score"])

        self.write_results_to_csv(
            [performance_metrics],
            "streaming_performance_results.csv",
            ["Accuracy", "Precision", "Recall", "F1 Score"],
        )
        return performance_metrics

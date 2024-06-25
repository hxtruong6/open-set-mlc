from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from evaluation_base import EvaluationBase


class ModelEvaluation(EvaluationBase):
    def __init__(self, model, X_val, y_val):
        self.model = model
        self.X_val = X_val
        self.y_val = y_val

    def evaluate(self):
        y_pred = self.model.predict(self.X_val)
        accuracy = accuracy_score(self.y_val, y_pred)
        precision = precision_score(self.y_val, y_pred, average="macro")
        recall = recall_score(self.y_val, y_pred, average="macro")
        f1 = f1_score(self.y_val, y_pred, average="macro")
        results = [
            {
                "Accuracy": accuracy,
                "Precision": precision,
                "Recall": recall,
                "F1 Score": f1,
            }
        ]
        self.write_results_to_csv(
            results,
            "model_evaluation_results.csv",
            ["Accuracy", "Precision", "Recall", "F1 Score"],
        )
        return results

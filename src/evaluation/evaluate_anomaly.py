from sklearn.metrics import confusion_matrix
from evaluation_base import EvaluationBase


class AnomalyDetectionEvaluation(EvaluationBase):
    def __init__(self, detector, X_test, y_test):
        self.detector = detector
        self.X_test = X_test
        self.y_test = y_test

    def evaluate(self):
        y_pred = [self.detector.detect_anomalies(x) for x in self.X_test]
        tn, fp, fn, tp = confusion_matrix(self.y_test, y_pred).ravel()
        sensitivity = tp / (tp + fn)  # True Positive Rate
        false_positive_rate = fp / (fp + tn)
        precision = tp / (tp + fp)
        results = [
            {
                "Sensitivity": sensitivity,
                "False Positive Rate": false_positive_rate,
                "Precision": precision,
            }
        ]
        self.write_results_to_csv(
            results,
            "anomaly_detection_results.csv",
            ["Sensitivity", "False Positive Rate", "Precision"],
        )
        return results

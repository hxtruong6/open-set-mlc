import time
from evaluation_base import EvaluationBase


class ExpertVerificationTime(EvaluationBase):
    def __init__(self, expert_verification, instances):
        self.expert_verification = expert_verification
        self.instances = instances

    def evaluate(self):
        start_time = time.time()
        confirmed = self.expert_verification.verify_new_label(self.instances)
        end_time = time.time()
        verification_time = end_time - start_time
        results = [{"Verification Time": verification_time, "Confirmed": confirmed}]
        self.write_results_to_csv(
            results, "expert_verification_time.csv", ["Verification Time", "Confirmed"]
        )
        return verification_time, confirmed

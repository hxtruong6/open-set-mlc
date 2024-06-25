class Buffer:
    def __init__(self, threshold):
        self.threshold = threshold
        self.instances = []

    def add_instance(self, instance):
        self.instances.append(instance)
        return len(self.instances) >= self.threshold

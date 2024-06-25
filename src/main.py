import logging
from src.data_loader import ImageDataLoader
from src.mlc_model import MLCModel
from src.anomaly_detector import AnomalyDetector
from src.buffer import Buffer
from src.expert_verification import ExpertVerification
from src.data_streamer import DataStreamer
from src.utils import create_directory
from src.utils.config_manager import ConfigManager
from src.utils.logger import setup_logger

# Setup logger
logger = setup_logger("mlc_system", "../logs/mlc_system.log")

# Load configuration
config_manager = ConfigManager("../config/config.yaml")
data_path = config_manager.get_config("data_path")
mlc_algorithm = config_manager.get_config("mlc_algorithm")
anomaly_threshold = config_manager.get_config("anomaly_threshold")
buffer_threshold = config_manager.get_config("buffer_threshold")


# Initialize preprocessing pipeline
# augmentation = DataAugmentation(flip=True, rotate=False)
# normalization = DataNormalization(mean=0.5, std=0.5)
# resizing = DataResizing(resize_shape=(224, 224))
# preprocessing_pipeline = PreprocessingPipeline(
#     steps=[augmentation, normalization, resizing]
# )


class MainSystem:
    def __init__(self, data_path, mlc_algorithm, anomaly_threshold, buffer_threshold):
        self.data_loader = ImageDataLoader(data_path)
        self.mlc_model = MLCModel(mlc_algorithm)
        self.anomaly_detector = AnomalyDetector(anomaly_threshold)
        self.buffer = Buffer(buffer_threshold)
        self.expert_verification = ExpertVerification()
        self.data_streamer = DataStreamer(self.data_loader)

    def initialize_training(self):
        logger.info("Loading initial data for training.")
        # TODO: Preprocess data before training
        data = self.data_loader.load_data()
        logger.info("Training initial MLC model.")
        self.mlc_model.train_model(data)

    def process_streaming_data(self):
        logger.info("Starting to process streaming data.")
        for instance in self.data_streamer.stream_data():
            labels = self.mlc_model.predict_labels(instance)
            is_anomalous = self.anomaly_detector.detect_anomalies(instance)
            if is_anomalous:
                buffer_full = self.buffer.add_instance(instance)
                if buffer_full:
                    self.handle_anomalous_buffer()

    def handle_anomalous_buffer(self):
        logger.info("Handling anomalous buffer.")
        new_label_detected = self.detect_new_label()
        if new_label_detected:
            confirmed = self.expert_verification.verify_new_label(self.buffer.instances)
            if confirmed:
                self.update_mlc_model()

    def detect_new_label(self):
        logger.info("Detecting new label from buffer.")
        # Implement logic to detect new label from the buffer
        pass

    def update_mlc_model(self):
        logger.info("Updating MLC model with new labels.")
        new_data, new_labels = self.prepare_new_data_and_labels()
        self.mlc_model.update_model(new_data, new_labels)
        self.buffer.instances.clear()

    def prepare_new_data_and_labels(self):
        logger.info("Preparing new data and labels for model update.")
        # Prepare the new data and labels for model update
        pass


if __name__ == "__main__":
    create_directory("../logs")
    system = MainSystem(data_path, mlc_algorithm, anomaly_threshold, buffer_threshold)
    system.initialize_training()
    system.process_streaming_data()

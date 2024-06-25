# from data_preprocessing.augmentation.py import DataAugmentation
# from data_preprocessing.normalization.py import DataNormalization


import cv2
from src.data_preprocessing.resizing import DataResizing


class PreprocessingPipeline:
    def __init__(self, steps):
        self.steps = steps

    def apply(self, image):
        for step in self.steps:
            image = step.apply(image)
        return image


if __name__ == "__main__":
    # Example usage
    # augmentation = DataAugmentation(flip=True, rotate=False)
    # normalization = DataNormalization(mean=0.5, std=0.5)
    resizing = DataResizing(resize_shape=(224, 224))

    # pipeline = PreprocessingPipeline(steps=[augmentation, normalization, resizing])
    pipeline = PreprocessingPipeline(steps=[resizing])
    preprocessed_image = pipeline.apply(cv2.imread("path/to/image.jpg"))

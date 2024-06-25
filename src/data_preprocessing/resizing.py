import cv2


class DataResizing:
    def __init__(self, resize_shape=(224, 224)):
        self.resize_shape = resize_shape

    def apply(self, image):
        return cv2.resize(image, self.resize_shape)

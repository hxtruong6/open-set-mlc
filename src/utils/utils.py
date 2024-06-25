import os


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def load_images_from_directory(directory_path):
    image_paths = [
        os.path.join(directory_path, f)
        for f in os.listdir(directory_path)
        if f.endswith(".jpg")
    ]
    return image_paths


# Example usage
create_directory("path/to/new_directory")
image_paths = load_images_from_directory("path/to/image_directory")

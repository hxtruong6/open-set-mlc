import yaml


class ConfigManager:
    def __init__(self, config_file):
        with open(config_file, "r") as file:
            self.config = yaml.safe_load(file)

    def get_config(self, key):
        return self.config.get(key)


# Example usage
config_manager = ConfigManager("../config/config.yaml")
mlc_algorithm = config_manager.get_config("mlc_algorithm")

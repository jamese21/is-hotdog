import yaml

config_path = '../config.yaml'

def load_config():
    with open(config_path, 'r') as file:
        loaded_config = yaml.safe_load(file)
    return loaded_config


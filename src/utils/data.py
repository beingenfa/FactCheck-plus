import json
import logging


def write_json(data,file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    logging.info(f"Data written to {file_path}")

def read_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    logging.info(f"Data loaded from {file_path}")
    return data
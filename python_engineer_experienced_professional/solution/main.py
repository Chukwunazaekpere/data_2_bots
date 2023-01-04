from reader import json_reader
import os


if __name__ == "__main__":
    file_index = 2
    file_path = os.path.join(os.path.dirname(__file__), f"../data/data_{file_index}.json")
    json_reader(file_path, file_index)
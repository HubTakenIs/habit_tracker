import os

class DataHelper():
    def __init__(self):
        self.setup_data_folder()
    
    def load_data():
        pass
    def write_data():
        pass

    def setup_data_folder(self):
        data_dir_path = os.path.abspath("./data/")
        if os.path.exists(data_dir_path) and os.path.isdir(data_dir_path):
            print(f"Data folder is already set up, {data_dir_path}")
        else:
            print(f"Data folder needs setting up.")
            print(f"Will create data folder")
            os.mkdir(data_dir_path)

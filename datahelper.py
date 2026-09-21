import os
import click

@click.command()
@click.option("--path", default="./data", help="path to data directory.")
def setup_data_folder(path):
    data_dir_path = os.path.abspath(path)
    if os.path.exists(data_dir_path) and os.path.isdir(data_dir_path):
        print(f"Data folder is already set up, {data_dir_path}")
    else:
        print(f"Data folder needs setting up.")
        print(f"Will create data folder")
        os.mkdir(data_dir_path)
    
def setup_data_file(self, file_name):
    data_dir_path = os.path.abspath("./data/")
    if os.path.exists(data_dir_path):
        f = open(file_name, "x")

if __name__ == "__main__":
    setup_data_folder(

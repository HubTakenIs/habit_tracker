import os
import click
import datetime

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

def list_of_dates():
    num_of_dates = 365
    start = datetime.datetime(2026,1,1)
    date_list = []
    for x in range(num_of_dates):
        date_list.append(start.date() + datetime.timedelta(days=x))
    print(date_list)
    return date_list



def setup_data_file(self, file_name):
    data_dir_path = os.path.abspath("./data/")
    if os.path.exists(data_dir_path):
        f = open(file_name, "x")
        f.close()
    f = open(file_name, "a")
    f.write("Date, Ticked")
    

if __name__ == "__main__":
    ml = list_of_dates()
    for item in ml:
        print(item)

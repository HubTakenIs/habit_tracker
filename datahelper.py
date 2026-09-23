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
    return date_list



def setup_data_file(file_name):
    data_dir_path = os.path.abspath("./data/")
    file_dir = os.path.join(data_dir_path, file_name)
    f = open(file_name, "a")
    f.write("Date, Ticked\n")
    date_list = list_of_dates()
    for date in date_list:
        f.write(f"{date},False\n")
    f.close()
    

if __name__ == "__main__":
    setup_data_file("programming")

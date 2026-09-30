import os
import click
import datetime
import calendar

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
    f = open(file_dir, "a")
    f.write("Date, Ticked\n")
    date_list = list_of_dates()
    for date in date_list:
        f.write(f"{date},False\n")
    f.close()
    

def tick_date(file_name, date):
    data_dir_path = os.path.abspath("./data/")
    file_dir = os.path.join(data_dir_path, file_name)
    f = open(file_dir, "r")
    file_lines = f.readlines()
    f.close()
    print("I have gotten the lines from file.")
    for i in range(len(file_lines)):
        line = file_lines[i]
        split = line.split(",")
        line_date = split[0]
        line_tick = split[1]
        # covert types and check
        if line_date == date:
            print(f"Date to be ticked found at index: {i}")
            new_line = f"{line_date},{True}\n"
            file_lines[i] = new_line
    f = open(file_dir, "w")
    f.writelines(file_lines)
    f.close()

def display_habit(file_name):
    
    data_dir_path = os.path.abspath("./data/")
    file_dir = os.path.join(data_dir_path, file_name)
    f = open(file_dir, "r")
    lines = f.readlines()
    f.close()
    top_line = ""
    month_names = list(calendar.month_name)
    for month in month_names:
        if month:
            top_line += f" {month} "
    print(top_line)
    count = 0
    months = []
    out = ""







if __name__ == "__main__":
    display_habit("programming.csv")

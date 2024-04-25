import csv

def write_dict_to_csv(filename: str, data: dict):
    with open(filename, "w", newline = "") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ";")
        csv_writer.writerow(f"data\n")

write_dict_to_csv("doodoo.txt", {"ding": 65})
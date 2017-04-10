"""This module describes how to work with csv files.

   Author: pivanchy.
"""

import csv

def write_csv(filename, data):
    with open(filename, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        map(writer.writerow, data)

def read_csv(filename):
    with open(filename, "rb") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        print("Data from CSV file:")
        for element in reader:
            print(element)


filename = '/tmp/temporary.csv'
data = ["first_name,last_name,city".split(","),
        "Tyrese,Hirthe,Strackeport".split(","),
        "Jules,Dicki,Lake Nickolasville".split(","),
        "Dedric,Medhurst,Stiedemannberg".split(",")
       ]

write_csv(filename, data)
read_csv(filename)

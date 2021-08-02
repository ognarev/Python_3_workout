# Open, read and write files 
import os
import csv
from typing import DefaultDict

data = [
  ("Buratino", "Strana Durakoff", 10), 
  ("Carabas", "Strana Durakoff", 54), 
  ("Chipolino", "Limon city", 7)
  ]
  
def write_to_file(data, file_name):
  "Writes data from list to CSV file"
  columns = 'name, address, age\n'
  with open(file_name, 'w') as fout:
    fout.write(columns)
    for item in data:
      text_row = []
      text_row = f"{item[0]}, {item[1]}, {item[2]}\n"
      fout.write(text_row)
      
def csv_interpreter(csv_file):
  "Return list of dictionaries. Convert csv file to list of dictionaries"
  list_of_dicts = []
  dict_keys = []
  with open(csv_file, 'r') as fin:
    csv_reader = csv.DictReader(fin)
    for row in csv_reader:
      n = 0
      pair = []  
      while n < len(csv_reader.fieldnames):
        pair.append(f"{csv_reader.fieldnames[n]}:{row[csv_reader.fieldnames[n]]}")
        if n + 1 < len(csv_reader.fieldnames): pair.append(",")
        n += 1
      d = {''.join(pair)}
      list_of_dicts.append(d)
  return list_of_dicts

#write_to_file(data, r"data/contacts.csv")
print(csv_interpreter(r"data/contacts.csv"))
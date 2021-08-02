# Open, read and write files 
import os

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
    for row in fin:
      #get keys from first row
      if ~len(list_of_dicts):
        n = 0
        while n < len(row):
          dict_keys.append(row[n])
          n += 1      
      #convert all rows to dictionaries
  return list_of_dicts

#write_to_file(data, r"data/contacts.csv")
list = csv_interpreter(r"data/contacts.csv")
print(list)
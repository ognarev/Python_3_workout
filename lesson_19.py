# Open, read and write files 

data = [
  ("Buratino", "Strana Durakoff", 10), 
  ("Carabas", "Strana Durakoff", 54), 
  ("Chipolino", "Limon city", 7)
  ]
  
def write_to_file(data, file_name):
  "Writes data from list to CSV file"
  with open(file_name, 'w') as fout:
    for item in data:
      text_row = []
      text_row = f"{data[0]}, {data[1]}, {data[2]}\n"
      fout.write(text_row)
      
write_to_file(data, r"data/contacts.csv")
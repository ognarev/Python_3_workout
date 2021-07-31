# Functions

def sort_bin(data, goal):
  "Returns goal's index if it is in data. Returns -1 if not"
  if goal in data:
    result = f"Your goal is {goal}. It's index in list is {data.index(goal)}"
  else:
    result = -1
  return result

def camel_to_snake(string_in, divider='_'):
  "Returns srting in snake_case"
  string_out = []
  for symbol_ in string_in:
    if symbol_.isupper():
      s = divider + symbol_.lower()
      string_out.append(s)
    else:
      string_out.append(symbol_)
  return ''.join(string_out)
  
  
#print(sort_bin([1, 2, 3], 2))
#print(camel_to_snake("thisIsCamelCaseName", '-'))
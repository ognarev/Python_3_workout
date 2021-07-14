# for cycle, else, break, continue

name_list = ['Jim', 'Jack', 'Rickie', 'Mothes', 'Daniels']

# Calculating average name length from the names list
def aver_name_lenght(name_list):
  names_l_sum = 0

  for name_ in name_list:
    name_l = len(name_)
    names_l_sum += name_l
    print(f"{name_} lenght is: {name_l}")

  aver_l = names_l_sum / len(name_list)
  print(f"\nAverage name lenght in this list is {aver_l}")
  

aver_name_lenght(name_list)
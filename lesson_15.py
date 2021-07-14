# for cycle, else, break, continue

name_list = ['Jim', 'Jack', 'Rickie', 'Mothes', 'Daniels']
friends_list = [('John', 'Mitchell', None),
                ('Philip', 'Sadkovsky', 23),
                ('Anatoliy', 'Bloh', 12),
                ('Viola', 'Strachey', 19),
                ('Yoshi', 'Toochke', 27),
                ('Vasil', 'Semenyuk', 30),
                ('Jacky', 'Sun', 84),
                ('Jim', 'Mortison', None),
                ('Rickie', 'Clacson', 15),
                ('Mothes', 'Rubenstein', 31)
                ]

# Manipulations with friends average age
def friends_info(friends_list):
  aver_age = 20;
  age_type = ("young", "old")
  sum_age = 0
  f_with_age = 0
  
  for friend_ in friends_list:
    if friend_[2] is None:
      continue
    sum_age += int(friend_[2])
    f_with_age += 1
  aver_age = sum_age / f_with_age
  print(f"Average age in the list is {aver_age} years.\n")

  for friend_ in friends_list:
    if friend_[2] is None:
      continue
    if friend_[2] < aver_age:
      f_type = age_type[0]
    else:
      f_type = age_type[1]
    print(f"{friend_[0]} is {f_type}, {friend_[2]}.")


# Calculating average name length from the names list
def aver_name_lenght(name_list):
  names_l_sum = 0
  for name_ in name_list:
    name_l = len(name_)
    names_l_sum += name_l
    print(f"{name_} lenght is: {name_l}")

  aver_l = names_l_sum / len(name_list)
  print(f"\nAverage name lenght in this list is {aver_l}")
  
# Searching for name in list
def is_name_here(name_list, s_name):
  name_is_in_list = False
  for name_ in name_list:
    if name_ is s_name:
      name_is_in_list = True
      break
  
  if name_is_in_list:
    print(f"Yeap, we have {s_name} in the list.")
  else:
    print(f"There's no name {s_name} in the list.")

#aver_name_lenght(name_list)
#is_name_here(name_list, "John")
#is_name_here(name_list, "Jack")
friends_info(friends_list)
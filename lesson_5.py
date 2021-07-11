# User input and output

# Get user name
def get_user_name():
  user_name = input("Write your name, please: ")
  return user_name

# Get user age
def get_user_age():
  user_age = input("How old are you? ")
  return user_age

# Welcoming user by name
def welcom_by_name():
    user_name = get_user_name()
    print(f"Hello, {user_name}")    

# Calculate next year age
def next_year_age():
    user_age = int(get_user_age())
    next_year_age = user_age + 1
    print(f"You will be {next_year_age} years old next year")    

welcom_by_name()
next_year_age()

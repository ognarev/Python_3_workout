# Get user name
def getUserName():
  userName = input("Write your name, please: ")
  return userName

# Get user age
def getUserAge():
  userAge = input("How old are you? ")
  return userAge

# Welcoming user by name
def welcomByName():
    userName = getUserName()
    print(f"Hello, {userName}")    

# Calculate next year age
def nextYearAge():
    userAge = int(getUserAge())
    nextYearAge = userAge + 1
    print(f"You will be, {nextYearAge} years old next year")    

welcomByName()
nextYearAge()
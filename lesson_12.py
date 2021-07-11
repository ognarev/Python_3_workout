# Comments, logical values, None type

def check_18():
	old = 18
	age = 45


	if age > old:
		print(f"You are more then {old} years old, cool.")
	elif age < old:
		print("You are too young")
	else:
		print("Something go wrong.")
		
def check_people(people=[]):
  if people:
    print("Someone present in class.")
  else:
    print("There nobody is in class.")
    
check_people(['James', 'Lilly'])
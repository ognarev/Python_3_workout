# if command, indents

# Check if year is leap
def check_leap_year(year):
  leap = (year % 4 == 0 and not \
         (year % 100 == 0)) or \
         (year % 400 == 0)
  if leap:
    t = f"Year {year} is leap."
  else:
    t = f"Year {year} isn't leap"
  print(t)

# Check if int number is odd or even
def check_odd(number_):
  even = (number_ % 2 and \
         number_ != 0)
  if even:
    t = f"Number {number_} is even."
  elif number_ == 0:
    t = f"Number {number_} isn't odd or even."
  else:
    t = f"Number {number_} is odd."
  print(t)

check_leap_year(1981)
check_leap_year(1600)
check_leap_year(1700)
check_odd(17)
check_odd(0)
check_odd(23578)

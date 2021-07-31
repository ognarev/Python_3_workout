#Index and slice in list, tuple

my_name = "Kottovian"
print(f"First symbol in {my_name} is {my_name[0]} and last is {my_name[-1]}")

f_name = 'somefile.txt'
print(f"In {f_name} extention is {f_name[(len(f_name) - 4):]}")

def is_palindrome(word_):
  "Returns True if word is palindrome and False if not"
  if word_ == word_[::-1]: return True
  else: return False
  
print(is_palindrome("cat"))
print(is_palindrome("pop"))
print(is_palindrome("131"))
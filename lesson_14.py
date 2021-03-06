# Containers. list, cortege, set

# Compare texts
def compare_texts():
  t1 = """Обратите внимание на порядок элементов результата: /
          на первый взгляд он кажется произвольным. Если для /
          вас важен порядок элементов, вместо множества лучше/ использовать другой тип данных."""
  t2 = """Операция объединения (|) возвращает множество,/  
          состоящее из всех элементов обоих множеств (с /
          исключением дубликатов)"""
  t1l = set(t1.split())
  t2l = set(t2.split())
  words_both = t1l & t2l
  words_unic = t1l ^ t2l
  print(f"Words in both texts: {words_both}\n")
  print(f"Unic words in both texts: {words_unic}\n")

# Find unic methods for list and cortage types
def compare_methods():
  li = set(dir([]))
  cort = set(dir((1,)))
  list_unic = li - cort
  cort_unic = cort - li
  text = (f"\
  This is unic metods for list:\n {list_unic}\n\n\
  This is unic methods for cortage:\n {cort_unic}")
  print(text)

compare_texts()
compare_methods()
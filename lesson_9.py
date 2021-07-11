# format method and f-type

# Name and age in formated string
def f_text_name_age(your_name, your_age):
  text_formated = 'Your name is {}. \nAnd you are {} years old.'.format(your_name, your_age)
  print(text_formated)

# Paragraph text
#paragraph = """\"Python is a great language!\", said Fred. \"I don't ever remember having this much fun before.\""""
#print(paragraph)

# Unicode symbols
def greece_symbols():
  ready_text = "\u0398"
  s_name = "\N{GREEK CAPITAL LETTER THETA}"
  print(f"Your symbol is: {ready_text} it's name: {s_name}")

f_text_name_age("Evgeniy", 554)
greece_symbols()

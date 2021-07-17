# Dictionaries 
# in, .get, .setdefault, collections.Counter, defaultdict, #del, 
# for, .keys, .values, .items

from collections import defaultdict

# in lesson samples
def names_to_bands():
  band1_names = [
      'John', 
      'George', 
      'Paul', 
      'Ringo'
  ]
  band2_names = ['Paul']
  names_to_bands = {}
  for name in band1_names:
    names_to_bands.setdefault(name, []).append('Beatles')
  for name in band2_names:
    names_to_bands.setdefault(name, []).append('Wings')
  print(names_to_bands)

# task 01
info = {
  'firstname': 'Torrino', 
  'lastname': 'Chipollino', 
  'age': 10
}

# task 02
def insert_info_in_dict():
  phone_dict = defaultdict(list)
  key_list = ['model', 'screen_size', 'memory', 'OS', 'provider']
  info_list = [
    'Stripsung. 9.10.1', 
    '480x120', 
    '2 GB', 
    'Tak OS', 
    'Phone Monopoly Unlimited Corp.'
  ]
  # for key_name in key_list:
  #     if key_name == 'model':
  #       info = 'Stripsung. 9.10.1'
  #     elif key_name == 'screen_size':
  #       info = '480x120'
  #     elif key_name == 'memory':
  #       info = '2 GB'
  #     elif key_name == 'OS':
  #       info = 'Tak OS'
  #     elif key_name == 'provider':
  #       info = 'Phone Monopoly Unlimited Corp.'
  for key_name in key_list:
    phone_dict[key_name] = info_list[key_list.index(key_name)]
      
  for key, value in phone_dict.items():
      print(f"{key}: {value}")

# task 03
def every_word_in_paragraph_counter():
  reader = open('data/text_Emerson.txt', 'rt')
  text_list = reader.read()
  reader.close()
  words_list = text_list.split()
  every_word_counter = defaultdict(list)
  num_word_dict = defaultdict(list)
  for word_ in words_list:
    every_word_counter.setdefault(word_, 0)
    every_word_counter[word_] += 1
  for key_, value_ in every_word_counter.items():
    num_word_dict.setdefault(value_, []).append(key_)
  dict_to_print = num_word_dict
  for w, n in sorted(dict_to_print.items(), reverse=True):
    print(f"{w}: {n}\n")

# task 04
def word_reuse_counter():
  pass

# task 05
def text_to_anagrams():
  reader = open('data/text_short.txt', 'rt')
  text_list = reader.read()
  reader.close()
  words_list = text_list.split()
  anagram_list = []
  anagram_text = ''
  anagram = []
  for word_ in words_list:
    #print(word_)
    anagram = word_[::-1]
    #print(anagram)
    anagram_list.append(anagram)
  for w in anagram_list:
    anagram_text += (w + ' ') 
  print(f"Source text is:\n{text_list}\n")
  print(f"Anagram text is:\n{anagram_text}\n")

# task 06
def page_rank_like():
  pairs_list = [
    ('a', 'b'), 
    ('a', 'c'), 
    ('d', 'c'),
    ('a', 'c'), 
    ('e', 'm'),
    ('e', 'c'), 
    ('f', 'm')
    ]
  def_rank = 1
  links_list = []
  page_rank_dict = {}
  page_links_dict = {}
  page_links_dict_02 = {}

  # Get all links per page
  for key, value in pairs_list:
    page_links_dict_02.setdefault(key, []).append(value)
    page_rank_dict.setdefault(key, 1)
    page_links_dict_02.setdefault(value, []).append(key)
    page_rank_dict.setdefault(value, 1)
  
  # Calculate PageRank
  def pr_calc(links_num, cur_pr):
    DECAY = 1
    
    updated_pr = cur_pr/links_num*DECAY
    return updated_pr

  iter = 0
  while iter >= 0:  
    for page_, rank in page_rank_dict.items():
      link_num = page_links_dict[page_]
      page_rank_dict[page_] = pr_calc(link_num, rank)
    iter -= 1
    
  # Get unic links list
  # for link_pairs in pairs_list:
  #   for page_ in link_pairs:
  #     links_list.append(page_)
  # pages_set = set(links_list)
  
  # # Set default page rank and number of links
  # for page_ in pages_set:
  #   page_rank_dict.setdefault(page_, def_rank)
  #   page_links_dict.setdefault(page_, 0)
  
  # # Get number of links per page
  # for page_ in pages_set:
  #   for l in links_list:
  #     if page_ is l:
  #       page_links_dict[page_] += 1

  for page_ in page_links_dict_02:
    print(f"{page_}:{page_rank_dict[page_]}  {page_links_dict_02[page_]}")
  #print(page_links_dict)
  #print(links_list)

#names_to_bands()
#insert_info_in_dict()
#every_word_in_paragraph_counter()
#word_reuse_counter()
#text_to_anagrams()
page_rank_like()
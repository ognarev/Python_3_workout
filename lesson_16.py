# Dictionaries 
# in, .get, .setdefault, collections.Counter, defaultdict, #del, 
# for, .keys, .values, .items

# band1_names = [
#     'John', 
#     'George', 
#     'Paul', 
#     'Ringo'
# ]
# band2_names = ['Paul']
# names_to_bands = {}
# for name in band1_names:
#   names_to_bands.setdefault(name, []).append('Beatles')
# for name in band2_names:
#   names_to_bands.setdefault(name, []).append('Wings')

# del names_to_bands['Ringo']
# print(names_to_bands)

info = {
  'firstname': 'Torrino', 
  'lastname': 'Chipollino', 
  'age': 10
}

phone_dict = {}
key_list = {'model', 'screen_size', 'memory', 'OS', 'provider'}


for key, value in phone_dict.items():
    print(f"{key}:{value}")
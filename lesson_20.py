# Unicode

from unicodedata import *

a = "\N{GOTHIC LETTER AHSA}"
b = "x\u00b2"
c = "\U0001034A"

some_text = "Some \"bla-bla-bla\" text. Awesome upside-down. \"It's just me.\""

# print(f"{name(u'a')} looks like this: {a}")
# print(f"b looks like this: {b}")
# print(f"{name(u'c')} looks like {c}")

def upside_down_string(stringin):
    "Returns string with reversed up symbols."
    upd_string = []
    symb_dict = {
        'a': 'ɐ', #'U+0250'
        'b': 'q',
        'c': 'ɔ', #'(U+0254)'
        'd': 'p',
        'e': 'ǝ', #'(U+01DD)',
        'f': 'ɟ', #'(U+025F)',
        'g': 'ƃ', #'(U+0183)',
        'h': 'ɥ', #'(U+0265)',
        'i': 'ᴉ', #'(U+1D09)',
        'j': 'ɾ', #'(U+027E)',
        'k': 'ʞ', #'(U+029E)',
        'l': 'l',
        'm': 'ɯ', #'(U+026F)',
        'n': 'u',
        'o': 'o',
        'p': 'd',
        'q': 'b',
        'r': 'ɹ', #'(U+0279)',
        's': 's',
        't': 'ʇ', #'(U+0287)',
        'u': 'n',
        'v': 'ʌ', #'(U+028C)',
        'w': 'ʍ', #'(U+028D)',
        'x': 'x',
        'y': 'ʎ', #(U+028E)',
        'z': 'z',
        'A': '∀', #(U+2200),
        'B': 'B',
        'C': 'Ɔ', #(U+0186),
        'D': 'D',
        'E': 'Ǝ', #(U+018E),
        'F': 'Ⅎ', #(U+2132),
        'G': 'פ', #(U+05E4),
        'H': 'H',
        'I': 'I',
        'J': 'ſ', #(U+017F),
        'K': 'K',
        'L': '˥', #(U+02E5),
        'M': 'W',
        'N': 'N',
        'O': 'O',
        'P': 'Ԁ', #(U+0500),
        'Q': 'Q',
        'R': 'R',
        'S': 'S',
        'T': '┴', #(U+2534),
        'U': '∩', #(U+2229),
        'V': 'Λ', #(U+039B),
        'W': 'M',
        'X': 'X',
        'Y': '⅄', #(U+2144),
        'Z': 'Z',
        '0': '0',
        '1': 'Ɩ', #(U+0196),
        '2': 'ᄅ', #(U+1105),
        '3': 'Ɛ', #(U+0190),
        '4': 'ㄣ', #(U+3123),
        '5': 'ϛ', #(U+03DB),
        '6': '9',
        '7': 'ㄥ', #(U+3125),
        '8': '8',
        '9': '6',
        ',': ',',
        '.': '˙', #(U+02D9),
        '?': '¿', #(U+00BF),
        '!': '¡', #(U+00A1),
        '"': ',,',
        "'": ',',
        "'": ',',
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '[',
        '{': '}',
        '}': '{',
        '<': '>',
        '>': '<',
        '&': '⅋', #'(U+214B)'
        '_': '‾', #'(U+203E)'
        ' ': ' ',
        '-': "-"    
    }
    #check every symbol from input string for upside-down symbol in dict. If it exists append upside-down symbol to new dict.
    for s in stringin:
        if s in symb_dict:
            #upd_string.append(symb_dict[s])
            upd_string.insert(0, symb_dict[s]) 
        else:
            #upd_string.append('?')
            upd_string.insert(0, symb_dict[s])
    return ''.join(upd_string)

def smart_quotes(stringin):
    "Returns string with smart quotes. Convert quotes to smart quotes."
    smart_text = []
    #Check all symbols for quotes
    fquotes = False
    for s in stringin:
        if (s == '"') & fquotes:
            fquotes = False
            s = "\N{RIGHT DOUBLE QUOTATION MARK}"
        elif s == '"':
            fquotes = True
            s = "\N{LEFT DOUBLE QUOTATION MARK}"
        smart_text.append(s)
    return ''.join(smart_text)

def smile_converter(stringin):
    "Returns text with smiles. Convert combinations of symbols to Unicode smiles."
    smiles_dict = {
        ':)': ['😀', 'Grinning Face'],
        ':8': ['😁', 'Grinning Face With Smiling Eyes'],
        '3)': ['😂', 'Face With Tears of Joy'],
        '8)': ['😃', 'Smiling Face With Open Mouth'],
        '7)': ['😄', 'Smiling Face With Open Mouth and Smiling Eyes'],
        '1)': ['😅', 'Smiling Face With Open Mouth and Cold Sweat'],
        '3)': ['😆', 'Smiling Face With Open Mouth and Tightly-Closed Eyes'],
        '0)': ['😇', 'Smiling Face With Halo'],
        '>)': ['😈', 'Smiling Face With Horns'],
        ';)': ['😉', 'Winking Face']        
    }
    text_with_smiles = []
    #check input text for slices of symbols from smiles dictionary
    n = 0
    while n <= len(stringin):
        if stringin[n] == ' ': #check first space in text
            temp_slice = ''.join(stringin[n + 1] + stringin[n + 2]) #check next 2 symbols after space if they are in smiles dict
            if temp_slice in smiles_dict: #if true change them to Unicode smile
                s = smiles_dict[temp_slice[0]]
                n =+ 3
        n += 1
    #add symbols to text_with_smiles
    return ''.join(text_with_smiles)

print(f"Correct:\n{some_text}\nUpside-down and reversed:\n{upside_down_string(some_text)}")
print(f"Smart quotes text:\n{smart_quotes(some_text)}")
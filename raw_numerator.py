# lesson 23. 

import sys

def number_raws(filename):
    rd = []
    try:
        with open(filename, 'r') as fin:
            for num, line in enumerate(fin):
                rd.append(f"{num}, {line}")
    except FileNotFoundError:
        print("File you try to open can't be found")
    
    with open('data\output.txt', 'w') as fout:
        for line in rd:
            fout.write(line)
    
def main():
    print(sys.argv)
    number_raws(input('Write file name: '))

if __name__ == '__main__':
    main()
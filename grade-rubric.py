import os
import re
import sys

def parse(opened_file):
    lst = []
    pattern = re.compile("[\s0-9].\/.[0-9]")
    for line in opened_file:
        match = pattern.search(line)
        if match:
            lst.append(match.group(0))
    return lst

def calculate(values):
    print(values)

def main():
    try:
        directory = sys.argv[1]
    except IndexError:
        print("No path specified running program on current directory...\n")
        directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    try:
        #get only the .txt file names in the curr_directory
        files = [txtfile for txtfile in os.listdir(directory) if re.match(r'(.*?)\.txt', txtfile)]
    except OSError:
        print(directory + ": (directory does not exists...)")
        sys.exit(1)    #exit with failure status

    for file_name in files:
        f = open(directory + '/' + file_name, 'r')
        value_lst = parse(f)
        calculate(value_lst)

main()
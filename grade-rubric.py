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

def calculate(values, name):
    answer = False
    totalpossible = 0
    totalearned = 0
    pattern = re.compile("[0-9]")
    for scores in values:
        points = pattern.findall(scores)
        if len(points) == 2:
            totalearned += int(points[0])
            totalpossible += int(points[1])
        else:
            if not answer:
                msg = "All grades were not entered for " + name + " would you like to continue anyway (y/n)? "
                userinput = input(msg)
                if userinput.lower() == 'y':
                    answer = True
                    totalpossible += int(points[0])
                    continue
                elif userinput.lower() == 'n':
                    print("Skipping " + name + "...")
                    return
                else:
                    print("Not a valid answer skipping " + name + "...")
                    return
            else:
                totalpossible += int(points[0])

    return name + '--> Total: ' + str(totalearned) + ' / ' + str(totalpossible)

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
        f = open(directory + '/' + file_name, 'r')    #open for reading and appending
        value_lst = parse(f)
        finaltotal = calculate(value_lst, file_name)
        if finaltotal != None:
            print(finaltotal)
            writefile = open(directory + '/' + file_name, 'a')
            writefile.write("\n" + finaltotal + "\n")
            writefile.close()
        f.close()
    sys.exit(0)

main()
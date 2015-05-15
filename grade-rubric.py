"""
@File:           grade-rubric.py
@Author:         Nick Mattis
@Date Created:   5/15/2015

A program to parse a rubric text file with values in the format:
            (2 / 2 points) or (2 / 2)
and calculate the totalpossible grade and totalearned grade for
that rubric. It can then be set to write that total to the file 
itself and will display all totals for all files at the end in 
alphabetical order.
"""
import os
import re
import sys

def parse(opened_file):
    """
    This function parses through each line of a opened file and uses regex to
    isolate the string "2 / 2" which can be any number of spaces between the
    number and "/", and any number. It then appends that string to a list if
    a match was found and returns the list.

    Args:
        opened_file (file_object): The opened file that you want to parse

    Returns:
        lst: a list of all the values to be calculated
    """
    lst = []
    pattern = re.compile("[\s0-9]*\/.*[0-9]")
    for line in opened_file:
        match = pattern.search(line)
        if match:
            lst.append(match.group(0))
    return lst

def calculate(values, name):
    """
    Calculates the total possible number of points and the total earned
    number of poitns given a list of "2 / 2" values. It uses regex to get the
    integer values on both sides of the divide symbol, these valuse can be any
    number. If there is not a pair (none filled out possible points field) it
    alerts and asks you if you want to conitnu with the calculation. Once
    everything is totaled up it returns a string of those values.

    Args:
        values (lst): List of values to be calculated
        name   (str): File name you are currently calculating

    Returns:
        str in the format "filename--> Total: int / int"
    """
    answer = False
    totalpossible = 0
    totalearned = 0
    pattern = re.compile("[0-9]+")
    for scores in values:
        points = pattern.findall(scores)
        if len(points) == 2:
            totalearned += int(points[0])
            totalpossible += int(points[1])
        else:    #if not all points fields were filled in ask for continue
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
                totalpossible += int(points[0])    #if you already continued don't
                                                   #don't ask anymore just add to
                                                   #possible score

    return name + '--> Total: ' + str(totalearned) + ' / ' + str(totalpossible)

def main():
    """
    Runs the entire program takes in a directory if specified, checks for text
    files, and if there are some parses and calculates there values. If
    specified it will write the total to the end of each file it calculates.
    Then it prints out a list of all the grades calculated.

    Returns:
        0: if exited successfully
        1: if exited with an error
    """
    try:
        directory = sys.argv[1]
    except IndexError:    #if no directory specified use current directory
        print("No path specified running program on current directory...\n")
        directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    try:
        #get only the .txt file names in the curr_directory
        files = [txtfile for txtfile in os.listdir(directory) if re.match(r'(.*?)\.txt', txtfile)]
        if files == []:
            print("No text files found in this directory...")
            return 1
        files.sort()
    except OSError:
        print(directory + ": (directory does not exists...)")
        return 1    #exit with failure status
    #ask if you want to write out the total to each file, default is no
    save = input("Would you like to save the totals to their respective files (y/N)? ")
    writeto = False
    if save.lower() == 'y':
        writeto = True
    grades = []
    for file_name in files:
        f = open(directory + '/' + file_name, 'r')    #open for reading
        value_lst = parse(f)
        finaltotal = calculate(value_lst, file_name)
        if finaltotal != None:    #if final total was calculated add to grades
            grades.append(finaltotal)
            if writeto:           #if you wanted the grade written do that
                writefile = open(directory + '/' + file_name, 'a')
                writefile.write("\n" + finaltotal + "\n")
                writefile.close()
        f.close()
    printgrades = input("Would you like to see all grades (Y/n)?")    #default is yes
    if printgrades.lower() != 'n':
        for grade in grades:
            print(grade)
    return 0

if __name__ == "__main__":
    sys.exit(main())
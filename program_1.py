# Claire Francis, March 23, 2025, Week9_program1.py

# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    total = 0
    with open("names.txt", "r") as f:
        numlines = f.readlines()
        for lines in numlines:
            total += 1
        

    ######################
    print(f'The number of names in list: {total}')


# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()

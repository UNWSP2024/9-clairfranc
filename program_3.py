# Claire Francis, March 25, 2025, Week9_program3.py

# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.

# The program should handle the following exceptions:

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file
# are converted to a number.
def sum_numbers_from_file():
    ######################

    total = 0
    with open('numbers.txt', 'r') as file:
        for line in file:
            try:
                total += float(line)

            except IOError:
                print('An error occurred trying to read the file.')
            except ValueError:
                print('Non-numeric data found in the file.')


    ######################
    print(f'In the sum_numbers_from_file function, the total is: {total}' )

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()

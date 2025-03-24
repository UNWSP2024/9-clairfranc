# Claire Francis, March 24, 2025, Week9_program2.py

# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).




def main():
    iterations = 0
    iterations = int(input("Enter how many numbers you want to input in file (has to be greater than 0 and less than 1000): "))
    if iterations <= 1000:

        def rand_file():
            for i in range(0, iterations):

                while True:
                    try:
                        num = float(input("Enter a number between 1 and 500: "))
                        if 1 <= num <= 500:
                            randnum_file = open('randnum_file.txt', 'a')
                            number = str(num)
                            randnum_file.write(number + '\n')
                            break
                        else:
                            print("Invalid input, please enter number between 1 and 500.")

                    except ValueError:
                        print("Invalid input, please enter a number.")
                randnum_file.close()

        if __name__ == '__main__':
            rand_file()
    else:
        print("Please enter in a valid number.")

if __name__ == '__main__':
    main()

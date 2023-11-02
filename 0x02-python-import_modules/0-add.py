#!/usr/bin/python3

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Import the 'add' function from the 'add_0' module
    from add_0 import add

    # Define two variables 'a' and 'b' with values 1 and 2
    a = 1
    b = 2

    # Call the 'add' function to add 'a', 'b', and store the result in 'result'
    result = add(a, b)

    # Print the result of the addition operation
    print("{} + {} = {}".format(a, b, result))

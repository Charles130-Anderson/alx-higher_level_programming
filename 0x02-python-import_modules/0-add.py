#!/usr/bin/python3
# Check if the script is being executed directly
if __name__ == "__main__":
    # Import the 'add' function from the 'add_0' module
    from add_0 import add

    # Define two variables 'a' and 'b' with initial values
    a = 1
    b = 2

    # Perform addition using the 'add' function and print the result
    print("{} + {} = {}".format(a, b, add(a, b)))

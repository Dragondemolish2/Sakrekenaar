# import os is to allow for it to run commands in the windows cmd
import os

# plus function to allow for addition
def plus(x: int, y: int):
    return x + y

# minus function to allow for subtraction
def minus(x: int, y: int):
    return x - y

# multiply function to allow for mulitplication
def multiply(x: int, y: int):
    return x * y

# divide function to allow for division with error checking for zero
def divide(x: int, y: int):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error cannot divide by zero"
    except Exception as error:
        return f"Other error {error}"

# clear the output
def clean():
    # uses cls for windows else for linux and macos uses clear to clean the terminal
    os.system("cls" if os.name == "nt" else "clear")

# sentinel variabele to control the loop
running = True

# the loop is running until "exit" is called to break it
while running:
    print("Calculator choose an option:")
    print("1. Plus")
    print("2. Minus")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear output")
    print("6. Exit")

    # get user input for first action
    user_input = input("Your input (1-6): ")

    if user_input == "6":
        # end the loop and close the program
        print("Goodbye")
        running = False
    
    elif user_input == "5":
        # clear output
        clean()

        # check if the user selected one of the 4 mathmatical operations
    elif user_input in ["1", "2", "3", "4"]:
        try:
            # get user input for the calculation
            a = int(input("Input first value: "))
            b = int(input("Input second value: "))

            # run one of the mathmatical operations selected
            if user_input == "1":
                print("Result: ", plus(a, b))
            elif user_input == "2":
                print("Result: ", minus(a, b))
            elif user_input == "3":
                print("Result: ", multiply(a, b))
            elif user_input == "4":
                print("Result: ", divide(a, b))
        
        # check if the values entered are correct
        except ValueError:
            print("Error incorrect value type submitted")

    else:
        print("Not valid selection")
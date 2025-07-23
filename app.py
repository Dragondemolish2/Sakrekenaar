print("Calculator (type 'exit' to quit)")

while True:  # while true creates a infinite loop so you can keep inputing diffierent calculations

    # Get the users calculation example: (5 + 5)
    calculation = input("Enter calculation: ")

    # To end the calculator session
    if calculation.lower() == 'exit':
        print("Goodbye!")
        break

        # try except block to cacth errors were if the values are valid it print the result else give the error message
    try:
        result = eval(calculation)
        print("Result:", result)
    except Exception as error:
        print("Invalid input. Please try again.")
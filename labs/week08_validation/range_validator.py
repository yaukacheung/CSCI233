# range_validator.py

def get_integer():
    while True:
        try:
            number = int(input("Enter an integer between 1 and 10: "))

            if 1 <= number <= 10:
                return number
            else:
                print("Error: Number must be between 1 and 10.")

        except ValueError:
            print("Error: Please enter a valid integer.")


# Call the function
value = get_integer()
print("Valid number entered:", value)
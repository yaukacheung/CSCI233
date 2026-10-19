# file_validator.py

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File opened successfully!")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
# function to append a line to the end of a file called "data.txt"

def append_to_file(filename, line):
    with open(filename, "a+") as file:
        file.write(line + "\n")
        file.close()


# function to read the contents of a file called "data.txt"
def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        file.close()
    return lines

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
sex = input("E")

data_to_add = 

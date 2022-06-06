def append_to_file(filename, line):
    """"
    Appending a line to the end of a file called "data.txt"
    Parameters:filename (string) - the name of the file to be read
    line (string) - the line to be appended to the file
    """
    with open(filename, "a+") as file:
        file.write(line + "\n")
        file.close()


def read_file(filename):
    """
    Opening a file and reading the contents into a variable called 'lines'
    Parameters:filename (string) - the name of the file to be read
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        file.close()
    return lines

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
sex = input("E")

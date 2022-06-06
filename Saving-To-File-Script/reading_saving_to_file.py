def append_to_file(filename, line):
    """
    Appending a line to the end of a file called 'data.txt'
    Parameters: filename (string) - the name of the file to be read
    line (string) - the line to be appended to the file
    """

    def is_file_empty(filename):
        """ Check if file is empty by reading first character in it"""
        with open(filename, 'r', encoding='utf-8') as read_obj:
            # Read first character
            first_character = read_obj.read(1)
            # If not fetched, then file is empty
            if not first_character:
                return True
        return False

    with open(filename, 'a+', encoding='utf-8') as file:
        if is_file_empty(filename) is True:
            file.write(line)
        else:
            file.write("\n" + line)
            file.close()


def read_file(filename):
    """
    Opening a file and reading the contents into a variable called 'lines'
    Parameters:filename (string) - the name of the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    return lines

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
sex = input("Enter your sex (M/F): ")

### Testing the functions ###
data_to_append = f'{name}, {age}, {city}, {sex}'
append_to_file("data.txt", data_to_append)

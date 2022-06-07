
def append_to_file(filename, data_to_write):
    """
    Appending a line to the end of a file
    Parameters: filename (string) - the name of the file to be read
    data_to_write (string) - the line to be appended to the file
    """
    with open(filename, "a+", encoding='utf-8') as file_object:
        file_object.seek(0)
        reading_data = file_object.read(100)
        if len(reading_data) > 0 :
            file_object.write("\n")
        file_object.write(data_to_write)
        file_object.close()

def read_file(filename):
    """
    Opening a file and reading the contents into a variable called 'lines_data'
    Parameters:filename (string) - the name of the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines_data = file.readlines()
        file.close()
    return lines_data

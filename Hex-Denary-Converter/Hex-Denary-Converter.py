import os, signal, sys

def sigint_handler(signal, frame):
    print ('KeyboardInterrupt is caught')
    sys.exit(0)

dictionary_hex_to_decimal = {
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "a":10,
        "b":11,
        "c":12,
        "d":13,
        "e":14,
        "f":15
    }

dictionary_denary_to_hex = {
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F"
    }


def denary_to_hex(denary_number):
    try:
        int(denary_number)
    except ValueError:
        print("Not a valid number, try again")
        return None
    if (int(denary_number) > 255) or (int(denary_number) < 1):
        print("Number too large or too small, try again")
        return None
    if int(denary_number) <= 16:
        first_character = dictionary_denary_to_hex[int(denary_number)]
        print(first_character + "\n")
    else:
        first_character = dictionary_denary_to_hex[int(denary_number) // 16]
        second_character = dictionary_denary_to_hex[int(denary_number) - (int(int(denary_number) // 16) * 16)]
        print(first_character + second_character + "\n")

def hex_to_denary(hex_number):
    if len(hex_number) == 2:
        digit1, digit2 = hex_number[0].lower(), hex_number[1].lower()
        # Must use formatted string when accessing dictionary because it has to be a string that is looked-up
        try:
            denary_digit1, denary_digit2 = dictionary_hex_to_decimal[f"{digit1}"], dictionary_hex_to_decimal[f"{digit2}"]
            print((denary_digit1 * 16) + denary_digit2)
        except KeyError:
            print("Invalid hex character\n")
            return None
    elif len(hex_number) == 1:
        digit1 = hex_number[0].lower()
        try:
            print(int(dictionary_hex_to_decimal[f"{digit1}"]))
        except KeyError:
            print("Invalid hex character\n")
    else:
        print("Hex number too large, too small or invalid, try again")
        return None

### Main Menu ###
while True:
    os.system("clear")
    choice = input("""Choose an option:

[1] Hex → Denary
[2] Denary → Hex
[exit] Quit the program
: """)
    if choice == '1':
        hex_number_inputted = input("Enter a hex number\n> ")
        hex_to_denary(hex_number_inputted)
        temp = input("Press ENTER to continue ")
        continue
    elif choice == '2':
        denary_number_inputted = input("Enter a denary number to convert to hex, between 1 and 255\n> ")
        denary_to_hex(denary_number_inputted)
        temp = input("Press ENTER to continue ")
        continue
    elif choice == 'exit':
        print("Quitting...")
        exit(0)
    else:
        print("Incorrect option")
        continue

signal.signal(signal.SIGINT, sigint_handler)

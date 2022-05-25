import os

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
        10:"a",
        11:"b",
        12:"c",
        13:"d",
        14:"e",
        15:"f"
    }


def denary_to_hex(denary_number):
    if (int(denary_number) > 255) or (int(denary_number) < 1):
        print("Number too large or too small, try again")
        return None
    first_character = dictionary_denary_to_hex[int(denary_number) // 16]
    second_character = dictionary_denary_to_hex[int(denary_number) - (int(first_character) * 16)]
    print(first_character + second_character + "\n")

def hex_to_denary(hex_number):
    try:
        digit1, digit2 = hex_number[0].lower(), hex_number[1].lower()
        denary_digit1, denary_digit2 = dictionary_hex_to_decimal[f"{digit1}"], dictionary_hex_to_decimal[f"{digit2}"]
        print((denary_digit1 * 16) + denary_digit2)
    except IndexError:
        digit1 = hex_number[0].lower()
        print(dictionary_hex_to_decimal[f"{digit1}"])
    except KeyError:
        print("Incorrect format of hex number, try again\n")

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

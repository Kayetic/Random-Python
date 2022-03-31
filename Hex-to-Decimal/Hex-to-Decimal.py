hex = input("Enter a hex digit: ")

def hex_to_denary(hex_number):
    dictionary = {
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

    digit1 = hex_number[0]
    digit2 = hex_number[1].lower()
    denary_digit1 = int(dictionary[f"{digit1}"]) * 16
    denary_digit2 = int(dictionary[f"{digit2}"])
    print(denary_digit1 + denary_digit2)

hex_to_denary(hex)
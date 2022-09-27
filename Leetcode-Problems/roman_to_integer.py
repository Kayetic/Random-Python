def roman_to_integer(roman):
    """
    Convert roman numeral to integer
    """
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if len(roman) == 1:
        return roman_dict[roman]
    else:
        result = 0
        

# Roman to Integer Conversion Using Proper  error handling 

def roman_to_int(roman_str):
    current = 0
    previous = 0
    total = 0
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    roman_str = roman_str.upper()

    try:
        for ch in reversed(roman_str):
            current = roman_map[ch]
            if current >= previous:
                total += current
            else:
                total -= current
            previous = current
    except KeyError:
        raise ValueError("Invalid character found in Roman numeral!")

    if total > 0:
        return total
    else:
        raise ValueError("Enter a valid Roman numeral!")

if __name__ == "__main__":
    num = input("Enter the Roman number: ")
    try:
        res = roman_to_int(num)
        print(f"Integer value: {res}")
    except ValueError as e:
        print(e)

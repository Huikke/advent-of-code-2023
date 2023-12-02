list_of_digits = []
# english = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def english_to_number(input):
    if input[:3] == "one":
        return "1"
    if input[:3] == "two":
        return "2"
    if input[:5] == "three":
        return "3"
    if input[:4] == "four":
        return "4"
    if input[:4] == "five":
        return "5"
    if input[:3] == "six":
        return "6"
    if input[:5] == "seven":
        return "7"
    if input[:5] == "eight":
        return "8"
    if input[:4] == "nine":
        return "9"
    
    return False


with open("day1_data.txt") as data:
    for line in data:
        first = True
        last = True
        first_digit = None
        last_digit = None
        for i, char in enumerate(line):
            if char.isdigit() == False:
                char = english_to_number(line[i:])
                if char == False:
                    continue

            if first == True:
                first = False
                first_digit = char

            last_digit = char

        list_of_digits.append(int(first_digit + last_digit))

print(sum(list_of_digits))
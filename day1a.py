list_of_digits = []

with open("day1_data.txt") as data:
    for line in data:
        first = True
        last = True
        first_digit = None
        last_digit = None
        for char in line:
            if char.isdigit():
                if first == True:
                    first = False
                    first_digit = char
                last_digit = char
        list_of_digits.append(int(first_digit + last_digit))

print(sum(list_of_digits))
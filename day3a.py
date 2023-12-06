def is_next_digit(line, i):
    try:
        if line[i+1].isdigit():
            return line[i+1] + is_next_digit(line, i+1)
        else:
            return ""
    except IndexError:
        return ""

def check_surroundings(engine_list, i, j, k):
    checklist = []
    # Topleft
    try:
        if i-1 != -1 and j+k-1 != -1:
            checklist.append(engine_list[i-1][j+k-1])
    except IndexError:
        pass
    # Top
    try:
        if i-1 != -1:
            checklist.append(engine_list[i-1][j+k])
    except IndexError:
        pass
    # Topright
    try:
        if i-1 != -1:
            checklist.append(engine_list[i-1][j+k+1])
    except IndexError:
        pass
    # Bottom left
    try:
        if j+k-1 != -1:
            checklist.append(engine_list[i+1][j+k-1])
    except IndexError:
        pass
    # Bottom
    try:
        checklist.append(engine_list[i+1][j+k])
    except IndexError:
        pass
    # Bottom right
    try:
        checklist.append(engine_list[i+1][j+k+1])
    except IndexError:
        pass
    # Left
    try:
        if j+k-1 != -1:
            checklist.append(engine_list[i][j+k-1])
    except IndexError:
        pass
    # Right
    try:
        checklist.append(engine_list[i][j+k+1])
    except IndexError:
        pass

    return checklist

answer = 0
with open("day3_data.txt") as engine:
    engine_list = []
    for line in engine:
        engine_list.append(line.replace("\n", ""))

    i = 0
    for line in engine_list:
        j = 0
        while len(line) > j:
            cond = False
            if line[j].isdigit() == True:
                number = line[j] + is_next_digit(line, j)

                for k in range(len(number)):
                    checklist = check_surroundings(engine_list, i, j, k)

                    for item in checklist:
                        if item.isdigit() or item == ".":
                            pass
                        else:
                            cond = True

                if cond:
                    answer += int(number)

                j += len(number)
            else:
                j += 1
        i += 1

print(answer)
def adjacent_digit(i, j, d): # d = direction
    if engine_list[i][j+d].isdigit():
        try:
            if d < 0:
                return adjacent_digit(i, j+d, d) + engine_list[i][j+d]
            else:
                return engine_list[i][j+d] + adjacent_digit(i, j+d, d)
        except IndexError:
            return engine_list[i][j+d]
    else:
        return ""

def check_surroundings(engine_list, i, j):
    checklist = []
    # Topleft
    checklist.append(engine_list[i-1][j-1])
    # Top
    checklist.append(engine_list[i-1][j])
    # Topright
    checklist.append(engine_list[i-1][j+1])
    # Bottom left
    checklist.append(engine_list[i+1][j-1])
    # Bottom
    checklist.append(engine_list[i+1][j])
    # Bottom right
    checklist.append(engine_list[i+1][j+1])
    # Left
    checklist.append(engine_list[i][j-1])
    # Right
    checklist.append(engine_list[i][j+1])

    return checklist

def number_retriever(num):
    if num == 0:
        return adjacent_digit(i-1, j-1, -1) + engine_list[i-1][j-1] + adjacent_digit(i-1, j-1, 1)
    elif num == 1:
        return adjacent_digit(i-1, j, -1) + engine_list[i-1][j] + adjacent_digit(i-1, j, 1)
    elif num == 2:
        return adjacent_digit(i-1, j+1, -1) + engine_list[i-1][j+1] + adjacent_digit(i-1, j+1, 1)
    elif num == 3:
        return adjacent_digit(i+1, j-1, -1) + engine_list[i+1][j-1] + adjacent_digit(i+1, j-1, 1)
    elif num == 4:
        return adjacent_digit(i+1, j, -1) + engine_list[i+1][j] + adjacent_digit(i+1, j, 1)
    elif num == 5:
        return adjacent_digit(i+1, j+1, -1) + engine_list[i+1][j+1] + adjacent_digit(i+1, j+1, 1)
    elif num == 6:
        return adjacent_digit(i, j-1, -1) + engine_list[i][j-1] + adjacent_digit(i, j-1, 1)
    elif num == 7:
        return adjacent_digit(i, j+1, -1) + engine_list[i][j+1] + adjacent_digit(i, j+1, 1)


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
            if line[j] == "*":

                checklist = check_surroundings(engine_list, i, j)

                k = 0
                found = None
                pair = None
                for item in checklist:
                    if item.isdigit():
                        if found == None:
                            found = k
                        else:
                            if found == 0 and k == 1:
                                pass
                            elif found == 0 and k == 2:
                                if not checklist[1].isdigit():
                                    pair = (number_retriever(found), number_retriever(k))
                                    break
                            elif found == 1 and k == 2:
                                pass
                            elif found == 3 and k == 4:
                                pass
                            elif found == 3 and k == 5:
                                if not checklist[4].isdigit():
                                    pair = (number_retriever(found), number_retriever(k))
                                    break
                            elif found == 4 and k == 5:
                                pass
                            else:
                                pair = (number_retriever(found), number_retriever(k))
                                break
                    k += 1

                print(i, pair)

                if pair != None:
                    answer += int(pair[0]) * int(pair[1])

            j += 1
        i += 1

print(answer)
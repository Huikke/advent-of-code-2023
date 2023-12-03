import re

red_cubes = 12
green_cubes = 13
blue_cubes =  14

answer = 0

with open("day2_data.txt") as games:
    for game in games:
        game = game.replace("\n", "")
        game = re.split(r'[:;, ]+', game)

        impossible = False
        i = 0
        for e in game:
            if e == "red":
                if int(game[i-1]) > red_cubes:
                    impossible = True
            elif e == "green":
                if int(game[i-1]) > green_cubes:
                    impossible = True
            elif e == "blue":
                if int(game[i-1]) > blue_cubes:
                    impossible = True
            i += 1

        if impossible == False:
            answer += int(game[1])

print(answer)
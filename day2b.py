import re

answer = 0

with open("day2_data.txt") as games:

    for game in games:
        game = game.replace("\n", "")
        game = re.split(r'[:;, ]+', game)

        red_cubes = 0
        green_cubes = 0
        blue_cubes =  0
        i = 0
        for e in game:
            if e == "red":
                if int(game[i-1]) > red_cubes:
                    red_cubes = int(game[i-1])
            elif e == "green":
                if int(game[i-1]) > green_cubes:
                    green_cubes = int(game[i-1])
            elif e == "blue":
                if int(game[i-1]) > blue_cubes:
                    blue_cubes = int(game[i-1])
            i += 1

        answer += red_cubes * green_cubes * blue_cubes

print(answer)
import re

with open("input.txt", 'r') as file:
    res = 0
    red_total = 12
    green_total = 13
    blue_total = 14

    for line in file:
        line = re.split(";|:", line)
        print(line)
        id = ''.join(filter(str.isdigit, line[0]))
        id = int(id)
        possible_game_flag = True

        for handful in line[1:]:  # start from 1 because 0 is the id
            handful = handful.split(",")
            red = 0
            blue = 0
            green = 0
            for dice in handful:
                if "red" in dice:
                    red = int(''.join(filter(str.isdigit, dice)))
                if "blue" in dice:
                    blue = int(''.join(filter(str.isdigit, dice)))
                if "green" in dice:
                    green = int(''.join(filter(str.isdigit, dice)))

            if red > red_total or blue > blue_total or green > green_total:
                possible_game_flag = False
                break  # No need to check further if one color is over the total

        if possible_game_flag:
            res += id

    print(res)
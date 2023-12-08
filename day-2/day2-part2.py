import re

with open("input.txt", 'r') as file:
    res = 0

    for line in file:
        line = re.split(";|:", line)
        #print(line)

        red = 0
        blue = 0
        green = 0

        for handful in line[1:]:  # start from 1 because 0 is the id
            handful = handful.split(",")

            for dice in handful:
                if "red" in dice:
                    red = max(red, int(''.join(filter(str.isdigit, dice))))
                if "blue" in dice:
                    blue = max(blue, int(''.join(filter(str.isdigit, dice))))
                if "green" in dice:
                    green = max(green, int(''.join(filter(str.isdigit, dice))))

        x = lambda n: 1 if n == 0 else n
        power = x(red) * x(blue) * x(green)
        res += power

    print(res)
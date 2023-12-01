with open("input.txt", 'r') as file:
    res = 0
    print(type(res))

    for line in file:
        # Stripping non-digit characters and newlines
        line = ''.join(filter(str.isdigit, line))
        # print("Stripped = ", line)

        # doubling int if line is only one digit
        if len(line) == 1:
            print("sum = ", res)
            print("line = ", line[0] + line[0])
            res += int(line[0] + line[0])
            print("new sum = ", res)
        
        else:
            res += int(line[0] + line[-1])
        #print("----------NEW SUM = ", res)
    
    print(res)
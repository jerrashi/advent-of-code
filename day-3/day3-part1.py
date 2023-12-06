with open("input.txt", 'r') as file:
    file_2d_array = []
    for line in file:
        row = [char for char in line.strip()]  # List comprehension for each character
        file_2d_array.append(row)  # Append the row to the 2d array

directions = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
res = 0

for i in range(len(file_2d_array)):
    for j in range(len(file_2d_array[0])):
        symbol = file_2d_array[i][j]
        if not symbol.isdigit() and symbol != ".":  # symbol is not a period or number
            # search all directions
            for direction in directions:
                new_i, new_j = i + direction[0], j + direction[1]
                if 0 <= new_i < len(file_2d_array) and 0 <= new_j < len(file_2d_array[0]):
                    if file_2d_array[new_i][new_j].isdigit():
                        current_number = file_2d_array[new_i][new_j]
                        file_2d_array[new_i][new_j] = '.'
                        # prepend all the left digits
                        scan = -1
                        while 0 <= new_j + scan and file_2d_array[new_i][new_j + scan].isdigit():
                            current_number = file_2d_array[new_i][new_j + scan] + current_number
                            file_2d_array[new_i][new_j + scan] = '.'
                            scan -= 1
                        # append all the right digits
                        scan = 1
                        while new_j + scan < len(file_2d_array[0]) and file_2d_array[new_i][new_j + scan].isdigit():
                            current_number += file_2d_array[new_i][new_j + scan]
                            file_2d_array[new_i][new_j + scan] = '.'
                            scan += 1
                        res += int(current_number)

print(res)
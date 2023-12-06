import re

with open("input.txt", 'r') as file:
    file_2d_array = []
    i = 0
    for line in file:
        print(line.strip())  # strip() removes newline characters at the end
        row = [char for char in line.strip()]  # List comprehension for each character
        file_2d_array.append(row)  # Append the row to the 2d array
    print(file_2d_array)
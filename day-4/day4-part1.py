import pandas as pd
df = pd.read_csv('C:\\Users\\280586\\OneDrive - CarMax\\Documents\\advent-of-code\\day-4\\input.txt', 
                  sep=':', header=None, engine='python')

# Create the dictionary
cards_dict = {i+1: [part.strip().split() for part in df.iloc[i, 1].split('|')] for i in range(len(df))}

total_points = 0

# Convert all strings in the lists to integers
for key, value in cards_dict.items():
    matching_count = 0
    winning_numbers = set()
    for num in value[0]:
        winning_numbers.add(num)
    for num in value[1]:
        if num in winning_numbers:
            matching_count += 1
    if matching_count > 0:
        total_points += pow(2, matching_count-1)

print(total_points)
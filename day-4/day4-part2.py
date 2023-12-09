import pandas as pd
df = pd.read_csv('C:\\Users\\280586\\OneDrive - CarMax\\Documents\\advent-of-code\\day-4\\input.txt', 
                  sep=':', header=None, engine='python')

# Create the dictionary
cards_dict = {i+1: [part.strip().split() for part in df.iloc[i, 1].split('|')] for i in range(len(df))}
print(cards_dict)
total_cards = 0

stack_of_cards = [1 for i in range(len(df))]

# Convert all strings in the lists to integers
for key, value in cards_dict.items():
    matching_count = 0
    winning_numbers = set()
    # Create set of winning numbers
    for num in value[0]:
        num = int(num)
        winning_numbers.add(num)
    # Compare ticket numbers to winning numbers
    for num in value[1]:
        num = int(num)
        if num in winning_numbers:
            matching_count += 1
    #print("MATCHING COUNT = ", matching_count)
    if matching_count > 0:
        for i in range(matching_count):
            # check to make sure we are not extending the array/stack
            if key + i <= len(df):
                stack_of_cards[key + i] += stack_of_cards[key - 1]
total_cards = sum(stack_of_cards)

print(total_cards)
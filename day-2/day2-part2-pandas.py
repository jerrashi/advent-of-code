import pandas as pd

# df2 = pd.read_fwf('C:\\Users\\280586\\OneDrive - CarMax\\Documents\\advent-of-code\\day-2\\input.txt', header=None)
# print(df2)
# Read the file using a custom separator that splits at ":"
df2 = pd.read_csv('C:\\Users\\280586\\OneDrive - CarMax\\Documents\\advent-of-code\\day-2\\input.txt', 
                  sep=':', header=None, engine='python')
print(df2)

# Create the dictionary
dict = {i+1: df2.iloc[i, 1].split(';') for i in range(len(df2))}

valid_vals = []
power = 0
for key, value in zip(dict.keys(), dict.values()):
    red_count = green_count = blue_count = 0
    for st in value:
        sub_list = ''.join([char for char in st if char.isalnum() or char == ' ']).split()
        #print(sub_list)
        for i, val in enumerate(sub_list):
            if val.isnumeric():
                if sub_list[i + 1] == 'red':
                    red_count = max(int(val), red_count)
                elif sub_list[i + 1] == 'green':
                    green_count = max(int(val), green_count)
                elif sub_list[i + 1] == 'blue':
                    blue_count = max(int(val), blue_count)
    #print("REDMAX: ", red_count, "GREEN MAX: ", green_count, "BLUE MAX: ", blue_count)
                
    if red_count <= 12 and green_count <= 13 and blue_count <= 14:
        valid_vals.append(key)
    power += red_count*green_count*blue_count
print(sum(valid_vals) + 1)
print(power)
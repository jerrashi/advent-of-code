with open("input.txt", 'r') as file:
    data = file.readlines()

total_sum = sum([
    int("".join([y for y in x.strip().replace('one','oonee').replace('two','ttwoo').replace('three','tthreee')
                .replace('four','ffourr').replace('five','ffivee').replace('six','ssixx')
                .replace('seven','ssevenn').replace('eight','eeightt').replace('nine','nninee')
                .replace('zero','zzeroo').replace('one','1').replace('two','2').replace('three','3')
                .replace('four','4').replace('five','5').replace('six','6').replace('seven','7')
                .replace('eight','8').replace('nine','9')
                if y.isdigit()][i] for i in (0, -1))) 
    for x in data if x
])

print("Total sum of calibration values:", total_sum)
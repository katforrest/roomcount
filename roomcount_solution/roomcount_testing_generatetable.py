import numpy as np
##print(np.random.randint(0,1))

table = []
for i in range(5):
    row_name = f"row_{i + 1}"
    list = []
    for i in range(5):
        number = np.random.randint(0,2)
        list.append(number)
    globals()[row_name] = list
    table.append(globals()[row_name])

print(table[0])
print(table[1])
print(table[2])
print(table[3])
print(table[4])


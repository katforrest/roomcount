import numpy as np

table = []
for i in range(5):
    row_name = f"row_{i + 1}"
    list = []
    for i in range(5):
        number = np.random.randint(0,2)
        list.append(number)
    globals()[row_name] = list
    table.append(globals()[row_name])

for row in table:
    print(row)


rooms = 0
x = 0
y = 0
value = table[x][y]
yleft=0
xup=0
xrange=0
for row in table:
    xrange+=1
yrange=len(table[0])

x = 0
y = 0
for a in range(xrange):
    for b in range(yrange):
        value = table[x][y]
        if value == 1:
            yleft = (y-1)
            previousleftvalue = table[x][yleft]
            if previousleftvalue == 0:
                xup = (x-1)
                previousupvalue = table[xup][y]
                if previousupvalue == 1:
                    rooms = rooms
                else:
                    rooms += 1
            else:
                rooms = rooms
            y += 1
        else:
            y += 1
    y=0
    x+=1
print("there are " + str(rooms) +" rooms.")
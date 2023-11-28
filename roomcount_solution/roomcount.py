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
        print("the value at " + str(x) + ", "+ str(y) + " is "+ str(value))
        if value == 1:
            yleft = (y-1)
            if yleft >= 0: 
                leftvalue = table[x][yleft]
                if leftvalue == 0:
                    xup = (x-1)
                    if xup >= 0:
                        upvalue = table[xup][y]
                        if upvalue == 1:
                            rooms = rooms
                        else:
                            rooms += 1
                            print("Plus 1 room")
                    else: 
                        rooms += 1
                        print("Plus 1 room")
                    y += 1
                else:
                    rooms = rooms
                    y += 1
            else:
                xup = (x-1)
                if xup >= 0:
                    upvalue = table[xup][y]
                    if upvalue == 1:
                         rooms = rooms
                    else:
                        rooms += 1
                        print("Plus 1 room")
                else: 
                    rooms += 1
                    print("Plus 1 room")
                y += 1
        else:
            y += 1
    y=0
    x+=1

print(str(rooms)+" rooms")

print("there are " + str(rooms) +" rooms.")
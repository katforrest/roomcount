Create an algorithm that returns the number of "rooms" given an ascii string like the following:
```
1100011
1100011
0001000
1000000
```
1's denote an occupied tile, 0 means unoccupied. A room is a collection of connected 1's. Tiles do not connect on diagonals.

Examples:

One Room:
```
100
000
000
```

One Room:
```
110
000
000
```

Two Rooms:
```
1010
0010
0000
```
Three Rooms:
```
100
010
001
```
Six Rooms:
```
1100011
1100011
0001000
1010011
```

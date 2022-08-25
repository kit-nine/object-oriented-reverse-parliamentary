"""r1,r2,r3,r4,r5,r6,r7,r8,r9,r10 = (100,60), (90,50), (80,40), (70,50), (60,50), (50,40), (40,30), (30,30), (20,20), (10,10)
points = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
columns = [100,90,80,70,60,50,40,30,20,10]

for b in columns:
    row_points = []
    for a in points:
        if a[1] == b:
            row_points.append(a)
    if row_points != []:
        after_points = int(len(columns) - (row_points[0][0] / 10))
        middle_points = 

        before_points = len(columns) - len(row_points) - after_points
        print(b, "	|", " ░"*before_points, " ▓"*len(row_points), " ░"*after_points, sep="")
    else: print(b, "	|", " ░"*len(columns), sep="")"""

grid = []
printable_grid = []
cols = 10
rows = 10

r1,r2,r3,r4,r5,r6,r7,r8,r9,r10 = (60,100), (50,90), (40,80), (50,70), (50,60), (40,50), (30,40), (30,30), (20,20), (10,10)
points = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]

for a in range(cols):
    temp = []
    for b in range(rows):
        temp.append(b)
    grid.append(temp)
for a in range(cols):
    for c in points:
        if c[1] == a*10:
            grid[int((c[0] / 10) - 1)][int((c[1] / 10) - 1)] = "▓"
for a in range(rows):
    temp = []
    for b in range(cols):
        temp.append(grid[a][b])
    printable_grid.append(temp)
for a in range(rows):
    print(str(100-(a*10)), " |", sep="", end="")
    for b in range(cols):
        if printable_grid[a][b] == "▓":
            print("▓ ", end="")
        else:
            print("░ ", end="")
    print("\n", end="")
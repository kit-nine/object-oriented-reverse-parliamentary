r1,r2,r3,r4,r5,r6,r7,r8,r9,r10 = (100,60), (90,50), (80,40), (70,50), (60,50), (50,40), (40,30), (30,30), (20,20), (10,10)
points = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
columns = [100,90,80,70,60,50,40,30,20,10]
row_points = []

for b in columns:
    for a in points:
        if a[1] == b:
            row_points.append(a)
    if row_points != []:
        before_points = len(columns)-len(row_points)-(len(columns)-(10-points.index(row_points[0])))
        after_points = len(columns)-len(row_points)-before_points
        print(b, "	|", " ░"*before_points, " ▓"*len(row_points), " ░"*after_points, sep="")
    else: print(b, "	|", " ░"*len(columns), sep="")
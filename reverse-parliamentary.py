# create grid
grid = [[i for i in range(21)] for i in range(21)]
for i,j in enumerate(range(-10,11)):
    for k,l in enumerate(range(-10,11)):
        grid[i][k] = (j,l)

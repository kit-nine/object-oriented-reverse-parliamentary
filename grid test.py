# Upcoming Grid (really annoying to code [and write, this took forever :/], but makes position changing really easy)
# (-5, 5) (-4, 5) (-3, 5) (-2, 5) (-1, 5) (0, 5)  (1, 5)  (2, 5)  (3, 5)  (4, 5)  (5, 5)
# (-5, 4) (-4, 4) (-3, 4) (-2, 4) (-1, 4) (0, 4)  (1, 4)  (2, 4)  (3, 4)  (4, 4)  (5, 4)
# (-5, 3) (-4, 3) (-3, 3) (-2, 3) (-1, 3) (0, 3)  (1, 3)  (2, 3)  (3, 3)  (4, 3)  (5, 3)
# (-5, 2) (-4, 2) (-3, 2) (-2, 2) (-1, 2) (0, 2)  (1, 2)  (2, 2)  (3, 2)  (4, 2)  (5, 2)
# (-5, 1) (-4, 1) (-3, 1) (-2, 1) (-1, 1) (0, 1)  (1, 1)  (2, 1)  (3, 1)  (4, 1)  (5, 1)
# (-5, 0) (-4, 0) (-3, 0) (-2, 0) (-1, 0) (0, 0)  (1, 0)  (2, 0)  (3, 0)  (4, 0)  (5, 0)
# (-5, -1)(-4, -1)(-3, -1)(-2, -1)(-1, -1)(0, -1) (1, -1) (2, -1) (3, -1) (4, -1) (5, -1)
# (-5, -2)(-4, -2)(-3, -2)(-2, -2)(-1, -2)(0, -2) (1, -2) (2, -2) (3, -2) (4, -2) (5, -2)
# (-5, -3)(-4, -3)(-3, -3)(-2, -3)(-1, -3)(0, -3) (1, -3) (2, -3) (3, -3) (4, -3) (5, -3)
# (-5, -4)(-4, -4)(-3, -4)(-2, -4)(-1, -4)(0, -4) (1, -4) (2, -4) (3, -4) (4, -4) (5, -4)
# (-5, -5)(-4, -5)(-3, -5)(-2, -5)(-1, -5)(0, -5) (1, -5) (2, -5) (3, -5) (4, -5) (5, -5)

# (y, x) column priority index

max_cols = 10
max_rows = 10
grid = []
temp = []
count = 0

for cols in range(max_cols):
    for rows in range(max_rows):
        temp.append(count)
        count += 1
    grid.append(temp)
    temp = []

for i in grid:
  print(i)

grid[0][3]

# need to switch to (x, y) to fit the grid (-+ = AL, ++ = AR, -- = LL, +- = LR)
# it also needs to go from -5 to 5 and instead of adding 1 each time it needs to be like in the grid
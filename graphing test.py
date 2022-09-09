# y - position (two graphs displayed for each position; one graph used for left-right and the other for authoritarian-libertarian)
# x - time
# center - (0,0)

# this should be similar to the optimal graph
# so it is the example graph this test will use
# |-------------------------|
# | ░░░░░░░░░░ | ░░░░░░░░░░ |
# | ▓░░░░░░░░░ | ░░░░░░░░░░ |
# | ░░░░░░░░░░ | ░░░░░░░░░░ |
# | ░▓░░░░░░░░ | ░░░░░░░░░░ |
# | ░░▓░░░░░▓░ | ░░▓▓▓▓▓░░░ |
# |------------|------------|
# | ░░░░░░▓▓░▓ | ▓▓░░░░░▓▓▓ |
# | ░░░▓░░░░░░ | ░░░░░░░░░░ |
# | ░░░░░▓░░░░ | ░░░░░░░░░░ |
# | ░░░░▓░░░░░ | ░░░░░░░░░░ |
# | ░░░░░░░░░░ | ░░░░░░░░░░ |
# |-------------------------|
points = [(-10,4), (-9,2), (-8,1), (-7,-2), (-6,-4), (-5,-3), (-4,-1), (-3,-1), (-2,1), (-1,-1), (0,-1), (1,-1), (2,-1), (3,1), (4,1), (5,1), (6,1), (7,1), (8,-1), (9,-1), (10,-1)]
print("┌──────────┬──────────┐")
for a in range(5):
    print("│", end="")
    for b in range(len(points)):
        if b == 10:
            print("│", end="")
        elif points[b][1] == 5 - a:
            print("▓", end="")
        else:
            print("░", end="")
    print("│\n", end="")
print("├──────────┼──────────┤")
for a in range(5):
    print("│", end="")
    for b in range(len(points)):
        if b == 10:
            print("│", end="")
        elif points[b][1] == -1 * (a + 1):
            print("▓", end="")
        else:
            print("░", end="")
    print("│\n", end="")
print("└──────────┴──────────┘")
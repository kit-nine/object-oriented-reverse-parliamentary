def create_grid():
    grid = [[i for i in range(21)] for i in range(21)]
    for i,j in enumerate(range(-10,11)):
        for k,l in enumerate(range(-10,11)): grid[i][k] = (j,l)
    return grid
"""
PSUEDOCODE

define:
    people per state

for each state
    for the number of people in a state
        create a person
        check their age
        if >= 18
            they vote
        if == 27
            they have 2 children
        if == 76
            they die
    average the positions of the votes for the state
    the two people with positions closest to the average position in that state are chosen as the senators
    the dictionary of states to house members is accessed, and that many representatives are chosen from the state
"""
# functions
#   create the political compass grid with -10 - 10 stylization for ease of understanding
def create_grid():
    grid = [[i for i in range(21)] for i in range(21)]
    for i,j in enumerate(range(-10,11)):
        for k,l in enumerate(range(-10,11)): grid[i][k] = (j,l)
    return grid
#   average a list of tuples into a single tuple, effectively averaging the positions of a group
def average(list_of_tups):
    temp_0 = 0
    temp_1 = 0
    for i in list_of_tups:
        temp_0 += i[0]
        temp_1 += i[1]
    temp_0 /= len(list_of_tups)
    temp_1 /= len(list_of_tups)
    return (temp_0,temp_1)
"""
PSEUDOCODE

define
    person list
    list of states
    people per state = 68
    positions in each state lists
    number of reps per state dict
    reps list
    senators list
    contra domus vote list
    contrum senatum vote list
    bills per rep = 10
    bills per senator = 10
    voting radius
    yes total
    law list
    background
    previous law location
    displayed year

for each state
    for the number of people per state
        create a person

VOTING
while year < runtime
    for each person in person list
        if person can vote
            person's position is recorded for the state
    for each state in the list of states
        average the positions in each state
        access reps per state dict for the current state
        choose that number + 2 representatives whose positions are closest to the average
        select a random two of them to be senators
        append the reps to the reps list 
        append the senators to the senators list
    average the positions of the reps
    find the corner that the average position is in
    find the opposite corner of that one
    for each person in person list
        find their position, shrunk to the corner
        append their position to the contra domus vote list
    average the contra domus vote list
    choose the person in the person list whose position is closest to the contra domus vote list average
    average the positions of the senators
    find the corner that the average position is in
    find the opposite corner of that one
    for each person in person list
        find their position, shrunk to the corner
        append their position to the contrum senatum vote list
    average the contrum senatum vote list
    choose the person in the person list whose position is closest to the contra domus vote list average
    the 13 iustitiarii are chosen from the person list, the 13 most centrist people who are not already senators, reps, or conciduorum

LAWMAKING
    for each representative in the reps list
        for i in bills per rep
            create bill (position, constitutionality score (-1, 1))
            reps deliberate on bill (simplified) for i in reps list
                if i's position and bill's position are close (within a set radius)
                    vote yes
                else
                    vote no
                sum up 'yes's and 'no's
                if yes total > 2/3 of the house of reps
                    bill moves on to senate
                else
                    bill dies
            senate deliberates on bill (simplified, they just vote)
                if i's position and bill's position are close (within a set radius)
                    vote yes
                else
                    vote no
                sum up 'yes's and 'no's
                if yes total > 2/3 of the senate
                    bill moves on to conciduorum
                else
                    bill dies
            conciduorum decides to veto or not -- if bill position within radius of contra domus position
                bill moves on to contrum senatum
            else
                bill dies
            if bill position within radius of contrum senatum position
                bill moves on to atrium
            else
                bill dies
            atrium determines constitutionality -- if constitutionality score > 0
                if position within radius of iustitiarii position
                    bill passes into law
                    append law to law list
    for each senator in the senate list
        for i in bills per senator
            create bill (position, constitutionality score (-1, 1))
            senate deliberates on bill (simplified) for i in senate list
                if i's position and bill's position are close (within a set radius)
                    vote yes
                else
                    vote no
                sum up 'yes's and 'no's
                if yes total > 2/3 of the senate
                    bill moves on to reps
                else
                    bill dies
            reps deliberate on bill (simplified, they just vote)
                if i's position and bill's position are close (within a set radius)
                    vote yes
                else
                    vote no
                sum up 'yes's and 'no's
                if yes total > 2/3 of the reps
                    bill moves on to conciduorum
                else
                    bill dies
            conciduorum decides to veto or not -- if bill position within radius of contra domus position
                bill moves on to contrum senatum
            else
                bill dies
            if bill position within radius of contrum senatum position
                bill moves on to atrium
            else
                bill dies
            atrium determines constitutionality -- if constitutionality score > 0
                if position within radius of iustitiarii position
                    bill passes into law
                    append law to law list
    increase year

DRAWING
while looping
    i = 2
    blit background
    if the spacebar is clicked
        i -= 1
        displayed year variable += 1
    while i > 1
        convert law position to a location on the screen
        if law.index = 0
            draw a dot at that location
        else
            draw a line from the previous law's location to the current law's location
        save the law's location into the variable previous law
        convert conciduorum positions to locations on the screen
        if conciduorum position.index = 0
            draw a dot at that location
        else
            draw a line from the previous conciduorum positions' location to the current conciduorum positions' location
        convert senate position to location on the screen
        if senate position.index = 0
            draw a dot at that location
        else
            draw a line from the previous year's senate's location to the current year's senate's location
        convert house position to location on the screen
        if house position.index = 0
            draw a dot at that location
        else
            draw a line from the previous year's house's location to the current year's house's location
        print the year
        i += 1
"""
import pygame, random, sys
from pygame.locals import *
pygame.init()

WINDOW = pygame.display.set_mode((625,500))
NUM_OF_COMPASSES = 3    # the SQUARE ROOT of the number of compasses to display - displays in a square
DISTANCE_BETWEEN_LINES = (min(WINDOW.get_height(), WINDOW.get_width())) / (10 * NUM_OF_COMPASSES)   # distance between lines on the compass grid
DAYS_PER_YEAR = 100     # in accordance with the laws of timetime.
LAWS_PER_DAY = 45       # based off data from https://www.govtrack.us/congress/votes#chamber[]=2&session=__ALL__ 
year_skip = 1           # number of years skipped with each press of the enter key
color = (255, 0, 0)
reps_params, sen_params, cd_params, cs_params, j_params, law_params = [], [], [], [], [], []
all_params = [reps_params, sen_params, cd_params, cs_params, j_params, law_params]
year = 0
compass_top_lefts = {0 : (0, 0), 1 : (DISTANCE_BETWEEN_LINES * 10, 0), 2 : (DISTANCE_BETWEEN_LINES * 20, 0), 3 : (0, DISTANCE_BETWEEN_LINES * 10), 4 : (DISTANCE_BETWEEN_LINES * 10, DISTANCE_BETWEEN_LINES * 10), 5 : (DISTANCE_BETWEEN_LINES * 20, DISTANCE_BETWEEN_LINES * 10), 6 : (0, DISTANCE_BETWEEN_LINES * 20), 7 : (DISTANCE_BETWEEN_LINES * 10, DISTANCE_BETWEEN_LINES * 20), 8 : (DISTANCE_BETWEEN_LINES * 20, DISTANCE_BETWEEN_LINES * 20)}    # MUST BE EDITED WHEN THE OTHER CONSTANTS ARE CHANGED!!! OTHERWISE IT ALL BREAKS!!!
msg = "year: "
COLOR = {0: (255,0,0), 1: (255,125,0), 2: (255,255,0), 3: (0,255,0), 4: (0,0,255), 5: (125,0,255)}
YEARS_TO_KEEP = 100
font = pygame.font.Font(None, 50)

def create_compass():
    """makes a compass, 10x10, with a center"""
    grid = []
    temp = []
    for cols in range(11):
        for rows in range(11): temp.append((rows - 5, cols + (10 - 5 - (2 * cols))))
        grid.append(temp)
        temp = []
    return grid
compass = create_compass()

def run_sim(years):
    """"runs" the "simulation" (it just picks a bunch of random numbers that are in the right ballpark)"""
    laws_passed = random.randint(0, years * DAYS_PER_YEAR * LAWS_PER_DAY)
    output = []
    for i in range(years):
        year_output = [(random.randint(-5, 5), random.randint(-5, 5)), (random.randint(-5, 5), random.randint(-5, 5)), (random.randint(-5, 5), random.randint(-5, 5)), (random.randint(-5, 5), random.randint(-5, 5)), (random.randint(-5, 5), random.randint(-5, 5)), (random.randint(-5, 5), random.randint(-5, 5)), laws_passed / (years * DAYS_PER_YEAR * LAWS_PER_DAY)]  # reps average position, senate average position, contra domus position, contrum senatum position, judiciary average position, law average position, percentage of laws passed
        output.append(year_output)
    return output

def comp_to_coords(compass_coords, which_compass):
    """outputs coords for the positions on the board given which compass and what the local coords are for the compass"""
    n_coord_1 = ((compass_coords[0] + 5) * DISTANCE_BETWEEN_LINES) + compass_top_lefts.get(which_compass)[0]
    n_coord_2 = ((compass_coords[1] + 5) * DISTANCE_BETWEEN_LINES) + compass_top_lefts.get(which_compass)[1]
    return [int(n_coord_1), int(n_coord_2)]

while True:
    WINDOW.fill((0,0,0))
    # draw the grid
    for col in range(0, 10 * NUM_OF_COMPASSES):
        thickness = 1
        for i in range(NUM_OF_COMPASSES):
            num1 = 4 + (10 * i)
            num2 = 9 + (10 * (i - 1))
            if col == num1: thickness = 3
            elif col == num2: thickness = 5
        pygame.draw.line(WINDOW, (255,255,255), ((DISTANCE_BETWEEN_LINES * (col + 1)), 0), ((DISTANCE_BETWEEN_LINES * (col + 1)), min(WINDOW.get_height(), WINDOW.get_width())), thickness)
    for row in range(0, 10 * NUM_OF_COMPASSES):
        thickness = 1
        for i in range(NUM_OF_COMPASSES):
            num1 = 4 + (10 * i)
            num2 = 9 + (10 * (i - 1))
            if row == num1: thickness = 3
            elif row == num2: thickness = 5
        pygame.draw.line(WINDOW, (255,255,255), (0, (DISTANCE_BETWEEN_LINES * (row + 1))), (min(WINDOW.get_height(), WINDOW.get_width()), (DISTANCE_BETWEEN_LINES * (row + 1))), thickness)
    # draw the lines
    if len(all_params[0]) > 2:
        for i in all_params:
            pygame.draw.lines(WINDOW, COLOR.get(all_params.index(i)), False, i, 3)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN and year_skip != 1: year_skip = int(year_skip / 10)
            elif event.key == K_UP: year_skip *= 10
            if event.key == K_RIGHT:
                output = run_sim(year_skip)
                for i in output:
                    for j in range(len(all_params)):
                        which_compass = j
                        coords = comp_to_coords(i[j], which_compass)
                        if len(all_params[j]) >= YEARS_TO_KEEP:
                            all_params[j].pop(0)
                        all_params[j].append(coords)
                year += year_skip
            if event.key == K_LEFT:
                pass # remove year_skip items from the end of the param list for the lines and year_skip years from the year variable
    
    pygame.display.update()
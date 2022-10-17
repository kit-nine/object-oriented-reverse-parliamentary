# → - I think to rework the compass and to add the graphical representation, I need to restart in a new file. This is that reworking.

#   - two executives
#   - a set amount of laws per year - manual input or a set amount can be built in
#   - go through entire legislative process rather than just simple voting
#   - full political compass; left-right and libertarian-authoritarian (array)
#   - get rid of most global variables
#   - object-oriented legislature
#   - the parents will survive 1 year
#   - media influence can skew the voting by a certain amount - manual input
#   - law creation is skewed toward the position of the legislative, not just random from their side
#   - reproduction is yearly, for simplicity of elections
#   - cool & easy to use graphics that show all the possible information you can take from the simulation
#   - passed laws' average position
#   - make some voters not vote
#   - electoral system
# imports
import random, pygame, sys
from pygame.locals import *
pygame.init()
#variables
fps_clock = pygame.time.Clock()
WINDOW = pygame.display.set_mode((1920,1070))
YEARS = 10
grid = []
temp = []
X = -4
Y = -3
voters = []
VOTERS_PER_STATE = 200 # Default: 200
STATES = {0:"AK",1:"AL",2:"AR",3:"AZ",4:"CA",5:"CO",6:"CT",7:"DE",8:"FL",9:"GA",10:"HI",11:"IA",12:"ID",13:"IL",14:"IN",15:"KS",16:"KY",17:"LA",18:"MA",19:"MD",20:"ME",21:"MI",22:"MN",23:"MO",24:"MS",25:"MT",26:"NC",27:"ND",28:"NE",29:"NH",30:"NJ",31:"NM",32:"NV",33:"NY",34:"OH",35:"OK",36:"OR",37:"PA",38:"RI",39:"SC",40:"SD",41:"TN",42:"TX",43:"UT",44:"VA",45:"VT",46:"WA",47:"WI",48:"WV",49:"WY"}
REPS_PER_STATE = {"AK":1,"AL":7,"AR":4,"AZ":9,"CA":53,"CO":7,"CT":5,"DE":1,"FL":27,"GA":14,"HI":2,"IA":4,"ID":2,"IL":18,"IN":9,"KS":4,"KY":6,"LA":6,"MA":9,"MD":8,"ME":2,"MI":14,"MN":8,"MO":8,"MS":4,"MT":1,"NC":13,"ND":1,"NE":3,"NH":2,"NJ":12,"NM":3,"NV":4,"NY":27,"OH":16,"OK":5,"OR":5,"PA":18,"RI":2,"SC":7,"SD":1,"TN":9,"TX":36,"UT":4,"VA":11,"VT":1,"WA":10,"WI":8,"WV":3,"WY":1}
SKEW = 0 # Default: 0 (float from -1 to 1, inclusive)
s_votes = []
cs_votes = []
r_votes = []
cd_votes = []
# output_coords = None
# put the object-oriented reverse parliamentary system code here
# congress
class Senator():
    def __init__(self):
        pass
class Representative():
    def __init__(self):
        pass
# conciduorum
class ContraDomus():
    def __init__(self):
        pass
class ContrumSenatum():
    def __init__(self):
        pass
# supreme court
class Justice():
    def __init__(self):
        pass
class Chief(Justice):
    def __init__(self):
        pass
# voters
class Voter():
    def __init__(self, state, pos):
        self.s_vote = None # this voter's vote for the senators from their state
        self.cs_vote = None # this voter's vote for the contrum senatum
        self.r_vote = None # this voter's vote for the reps from their state
        self.cd_vote = None # this voter's vote for the contra domus
        self.state = state # the state they're from
        self.pos = pos # their position, used for skewing their vote
    def s_voting(self): # vote for the senators from the voter's state
        self.s_vote = skew(self.pos - 1, self.pos + 1)
    def cs_voting(self): # vote for the contrum senatum
        pass
    def r_voting(self): # vote for the reps from the voter's state
        pass
    def cd_voting(self): # vote for the contra domus
        pass
# FUNCTIONSs
# randomness skew function
def skew(min, max): # both min and max are inclusive
    output = random.randint(min, max)
    output * (1 + SKEW)
    return int(output)
# create the compass
for cols in range(11):
    for rows in range(11):
        temp.append((rows - 5, cols + (10 - 5 - (2 * cols))))
    grid.append(temp)
    temp = []
# output_coords = grid[(6 - Y) - 1][(6 + X) - 1]
# create the voters
for i in range(50):
    for i_1 in range(VOTERS_PER_STATE):
        voter = Voter(i, grid[(6 - skew(-5, 5)) - 1][(6 + skew(-5, 5)) - 1])
# every 1 years
for i in YEARS:
    # every year
        # lawmaking
            # house voting
            # senate voting
            # conciduorum voting
            # judicial ruling
    # every 2 years
    if i % 2 == 0:
        # voters vote for the senators from their state
        for i_1 in voters:
            for i_2 in range(2):
                avgvote = 0
                s_votes.append(i_1.s_voting())
                for i_3 in s_votes:
                    avgvote += i_3
                avgvote = int(avgvote / len(s_votes))





    # every 4 years
    if i % 4 == 0:
        # voters vote for the conciduorum members
        for i_1 in voters:
            cs_votes.append(i_1.cs_voting())
            cd_votes.append(i_1.cd_voting())
    # every 6 years
    if i % 6 == 0:
        # voters vote for the HOR reps from their state
        for i_1 in voters:
            r_votes.append(i_1.r_voting())
# when all calculations have been run and the simulation is ready to display:
display_start = True
# the display, using pygame
while display_start == True:



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        


    pygame.display.update()
    fps_clock.tick(30)
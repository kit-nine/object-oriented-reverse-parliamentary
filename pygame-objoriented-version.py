# → - to rework the compass and to add the graphical representation, i need to restart in a new file. this is that reworking.

#   - two executives
#   - a set amount of laws per year - manual input or a set amount can be built in
#   - go through entire legislative process rather than just simple voting
#   - full political compass; left-right and libertarian-authoritarian (array)
#   - get rid of most global variables
#   - object-oriented legislature
#   - the parents will survive 1 year
#   - media influence can skew the voting by a certain amount - manual input
#   - law creation is skewed toward the position of the legislative, not just random from their corner
#   - reproduction is yearly, for simplicity of elections
#   - cool & easy to use graphics that show all the possible information you can take from the simulation
#   - passed laws' average positions
#   - make some voters not vote
#   - electoral system

# imports
import random, pygame, sys
from pygame.locals import *
pygame.init()

# variables
fps_clock = pygame.time.Clock()
X = -4
Y = -3
voters = []
senators = []
reps = []
contra_domus = None
contrum_senatum = None
all_bills = []
font = pygame.font.Font(None, 50)
loop = True
year = 0
reps_avg_pos = (0, 0)
# constants
#WINDOW = pygame.display.set_mode((1109,515))
YEARS = 1000 # Testing should use 10 or 100, but normally at least 1000 should be run to get accurate results
VOTERS_PER_STATE = 200 # Default: 200
STATES = {0:"AK",1:"AL",2:"AR",3:"AZ",4:"CA",5:"CO",6:"CT",7:"DE",8:"FL",9:"GA",10:"HI",11:"IA",12:"ID",13:"IL",14:"IN",15:"KS",16:"KY",17:"LA",18:"MA",19:"MD",20:"ME",21:"MI",22:"MN",23:"MO",24:"MS",25:"MT",26:"NC",27:"ND",28:"NE",29:"NH",30:"NJ",31:"NM",32:"NV",33:"NY",34:"OH",35:"OK",36:"OR",37:"PA",38:"RI",39:"SC",40:"SD",41:"TN",42:"TX",43:"UT",44:"VA",45:"VT",46:"WA",47:"WI",48:"WV",49:"WY"}
REPS_PER_STATE = {"AK":1,"AL":7,"AR":4,"AZ":9,"CA":53,"CO":7,"CT":5,"DE":1,"FL":27,"GA":14,"HI":2,"IA":4,"ID":2,"IL":18,"IN":9,"KS":4,"KY":6,"LA":6,"MA":9,"MD":8,"ME":2,"MI":14,"MN":8,"MO":8,"MS":4,"MT":1,"NC":13,"ND":1,"NE":3,"NH":2,"NJ":12,"NM":3,"NV":4,"NY":27,"OH":16,"OK":5,"OR":5,"PA":18,"RI":2,"SC":7,"SD":1,"TN":9,"TX":36,"UT":4,"VA":11,"VT":1,"WA":10,"WI":8,"WV":3,"WY":1}
SKEW = 0 # Default: 0 (float from -1 to 1, inclusive)
SKEW_DISTANCE = 1 # Default: 1 (positive non-zero integer)
DISPLAY_BG = pygame.image.load('display background.png')
DISPLAY_KEY = pygame.image.load('display key.png')
DISPLAY_COORDS = [(180,165), (180,320), (180,65), (400,165), (400,320), (400, 65), (280,165), (280,320), (280,65), (520,165), (520,320), (520, 65), (20,125), (20,175), (20,250), (20,300)]
# congress
class Senator():
    def __init__(self, pos, gen, state):
        self.pos = pos
        self.generation = gen
        self.state = state
class Representative():
    def __init__(self, pos, gen, state):
        self.pos = pos
        self.generation = gen
        self.state = state
# conciduorum
class ContraDomus():
    def __init__(self, pos, gen):
        self.pos = pos
        self.generation = gen
class ContrumSenatum():
    def __init__(self, pos, gen):
        self.pos = pos
        self.generation = gen
# supreme court
class Justice():
    def __init__(self, bias, gen):
        self.bias = bias
        self.generation = gen
class Chief(Justice):
    def __init__(self, bias, gen):
        self.bias = bias
        self.generation = gen
# voters
class Voter():
    def __init__(self, state, pos, gen, compass):
        global SKEW
        global SKEW_DISTANCE
        self.s_vote = self.voting() # this voter's vote for the senators from their state
        self.cs_vote = self.voting() # this voter's vote for the contrum senatum
        self.r_vote = self.voting() # this voter's vote for the reps from their state
        self.cd_vote = self.voting() # this voter's vote for the contra domus
        self.state = STATES.get(state) # the state they're from
        self.pos = pos # their position, used for skewing their vote
        self.parent = None # whether this voter votes with or against their parent
        self.skew = skew
        self.generation = gen
        self.skew_params_0 = self.find_skew_params(self.pos[0], SKEW_DISTANCE)
        self.skew_params_1 = self.find_skew_params(self.pos[1], SKEW_DISTANCE)
        self.compass = compass
    def voting(self): # vote for the contra domus
        return (skew(self.skew_params_0[0], self.skew_params_0[1]), skew(self.skew_params_1[0], self.skew_params_1[1]))
    def reproduce(self):
        child = Voter(self.state, self.compass[(6 - skew(self.skew_params_0[0], self.skew_params_0[1]) - 1)][6 + skew(self.skew_params_1[0], self.skew_params_1[1]) - 1], self.generation + 1)
        voters.append(child)
    def find_skew_params(self, a, b):
        if a - b < -5 and a + b > 5: params = (a, a)
        elif a - b >= -5 and a + b > 5: params = (a - b, a)
        elif a - b < -5 and a + b <= 5: params = (a, a + b)
        else: params = (a - b, a + b)
        return params
# FUNCTIONS
# finds the parameters for skewing that won't go outside the grid
# randomness skew function
def skew(min, max): # both min and max are inclusive
    output = random.randint(min, max)
    output * (1 + SKEW)
    return int(output)
# create the compass
def create_compass():
    grid = []
    temp = []
    for cols in range(11):
        for rows in range(11): temp.append((rows - 5, cols + (10 - 5 - (2 * cols))))
        grid.append(temp)
        temp = []
    return grid
# output_coords = grid[(6 - Y) - 1][(6 + X) - 1]
# create the voters
def create_gen_1(VOTERS_PER_STATE, compass, voters):
    for i in range(50):
        for i_1 in range(VOTERS_PER_STATE):
            voter = Voter(i, compass[(6 - skew(-5, 5)) - 1][(6 + skew(-5, 5)) - 1], 1, compass)
            voters.append(voter)
# vote for reps
def reps_voting():
    for i in voters: i.r_voting()
    for i in range(50):
        state = STATES.get(i)
        rep_pos = (0,0)
        for j in range(REPS_PER_STATE.get(state)):
            for k in range(VOTERS_PER_STATE): rep_pos = (rep_pos[0] + voters[k].r_vote[0], rep_pos[1] + voters[i * j].r_vote[1])
            rep_pos = (int(rep_pos[0] / VOTERS_PER_STATE), int(rep_pos[1] / VOTERS_PER_STATE))
            rep = Representative(rep_pos, year + 1, state)
            reps.append(rep)
# vote for contra domus
def contradomus_voting():
    cd_pos = (0,0)
    for i in reps: reps_avg_pos = (reps_avg_pos[0] + i.pos[0], reps_avg_pos + i.pos[1])
    reps_avg_pos = (reps_avg_pos[0] / len(reps), reps_avg_pos[1] / len(reps))
    for i in voters:
        i.cd_voting()
        i.cd_vote = (int((i.cd_vote[0] + 5) / 2), int((i.cd_vote[0] + 5) / 2))
        if reps_avg_pos[0] >= 0 and reps_avg_pos[1] >= 0: i.cd_vote = (i.cd_vote[0] * -1, i.cd_vote[1] * -1)
        elif reps_avg_pos[0] <= 0 and reps_avg_pos[1] >= 0: i.cd_vote = (i.cd_vote[0], i.cd_vote[1] * -1)
        elif reps_avg_pos[0] >= 0 and reps_avg_pos[1] <= 0: i.cd_vote = (i.cd_vote[0] * -1, i.cd_vote[1])
    cd_pos = (cd_pos + i.cd_vote[0], cd_pos + i.cd_vote[1])
    cs_pos = (cs_pos[0] / len(voters), cs_pos[1] / len(voters))
    contra_domus = ContraDomus(cd_pos)
    return contra_domus
# vote for senate
def senate_voting():
    for i in voters: i.s_voting()
    for i in range(50):
        state = STATES.get(i)
        sen_pos = (0,0)
        for j in range(2):
            for k in range(VOTERS_PER_STATE): sen_pos = (sen_pos[0] + voters[k].s_vote[0], sen_pos[1] + voters[i * j].s_vote[1])
            sen_pos = (int(sen_pos[0] / VOTERS_PER_STATE), int(sen_pos[1] / VOTERS_PER_STATE))
            sen = Senator(sen_pos, year + 1, state)
            senators.appen(sen)
# vote for contrum senatum
def contrumsenatum_voting():
    cs_pos = (0,0)
    for i in senators: sens_avg_pos = (sens_avg_pos[0] + i.pos[0], sens_avg_pos[1] + i.pos[1])
    sens_avg_pos = (sens_avg_pos[0] / len(senators), sens_avg_pos[1] / len(senators))
    for i in voters:
        i.cs_voting()
        i.cs_vote = (int((i.cs_cote[0] + 5) / 2), int((i.cs_vote[0] + 5) / 2))
        if sens_avg_pos[0] >= 0 and sens_avg_pos[1] >= 0: i.cs_vote = (i.cs_vote[0] * -1, i.cs_vote[1] * -1)
        elif sens_avg_pos[0] <= 0 and sens_avg_pos[1] >= 0: i.cs_vote = (i.cs_vote[0], i.cs_vpte[1] * -1)
        elif sens_avg_pos[0] >= 0 and sens_avg_pos[1] <= 0: i.cs_vote = (i.cs_vote[0] * -1, i.cs_vote[1])
    cs_pos = (cs_pos + i.cs_pos[0], cs_pos + i.cs_vote[1])
    cs_pos = (cs_pos[0] / len(voters), cs_pos[1] / len(voters))
# lawmaking (overall)
def lawmaking(bills):
    bill = bill_creation()
    all_bills.append(bill)
    bill_0 = chamber_0_committee(bill)
    alive = chamber_0_vote(bill_0)
    if alive == False: law_failed(bill) 
    else:
        bill_1 = chamber_1_committee(bill)
        alive = chamber_1_vote(bill_1)
        if alive == False: law_failed(bill) 
        else:
            bill = conf_committee(bill_0, bill_1)
            alive = congress_overall(bill)
            if alive == False: law_failed(bill)
            else:
                alive = concid_chamber_0_check(bill)
                if alive == False:
                    alive = congress_overrule(bill)
                    if alive == False: law_failed(bill)
                    else:
                        alive = concid_chamber_1_check(bill)
                        if alive == False:
                            alive = congress_overrule(bill)
                            if alive == False: law_failed(bill)
                            else:
                                alive = judicial_review(bill)
                                if alive == True: law_passed(bill)
                                else: law_failed(bill)
# lawmaking sub-functions:
# congress chamber 1 bill creation
def bill_creation():
    pass
# congress chamber 1 committee process
def chamber_0_committee():
    pass
# congress chamber 1 overall
def chamber_0_vote():
    pass
# failure by chamber 1 vote
# congress chamber 2 committee process
def chamber_1_committee():
    pass
# congress chamber 2 overall
def chamber_1_vote():
    pass
# failure by chamber 2 vote
# combine the laws
def conf_committee():
    pass
# congress overall
def congress_overall():
    pass
# failure by congress vote
# conciduorum chamber 1 check
def concid_chamber_0_check():
    pass
# conciduorum chamber 2 check
def concid_chamber_1_check():
    pass
# congressional override (if concid vetoed)
def congress_overrule():
    pass
# failure by conciduorum veto
# judicial review
def judicial_review():
    pass
# failure by unconstitutionality
# law failed
def law_failed():
    pass
# law passed
def law_passed():
    pass
# 7 types of years: first year, in-between year1, in-between year 2, reps, reps&concid, reps&senate, and reps&concid&senate
def year_type_0(reps, senators, contra_domus, contrum_senatum): # makes compass, voters, votes for reps, cocid, and senate, lawmaking ~ happens on only year 0
    # make compass
    compass = create_compass()
    # make voters
    create_gen_1(VOTERS_PER_STATE, compass, voters)
    # vote for reps
    reps_voting()
    # vote for senate
    senate_voting()
    # vote for cd
    contra_domus = contradomus_voting()
    # vote for cs
    contrum_senatum = contrumsenatum_voting()
    # lawmaking

def year_type_1(reps, senators, contra_domus, contrum_senatum): # new children are born, lawmaking ~ happens on only year 1
    # new children
    for i in voters:
        i.reproduce()
    # lawmaking

def year_type_2(reps, senators, contra_domus, contrum_senatum): # old voters die, new children are born, lawmaking ~ happens on every odd-numbered year after 1
    # old voters die
    for i in voters:
        if i.generation < year:
            del voters[i.index()]
    # new children
    for i in voters:
        i.reproduce()
    # lawmaking

def year_type_3(reps, senators, contra_domus, contrum_senatum): # old reps leave, new reps voted for, old voters die, new children are born, lawmaking ~ happens on every even-numbered year after 0
    # old reps leave
    reps = []
    # new reps voted for
    reps_voting()
    # old voters die
    for i in voters:
        if i.generation < year:
            del voters[i.index()]
    # new children
    for i in voters:
        i.reproduce()
    # lawmaking

def year_type_4(reps, senators, contra_domus, contrum_senatum): # old reps leave, new reps voted for, old concid leave, new concid voted for, old voters die, new children are born, lawmaking ~ happens on every year divisible by 4 after 0
    # old reps leave
    reps = []
    # new reps voted for
    reps_voting()
    # old concid leave
    # new concid voted for
    contra_domus = contradomus_voting()
    contrum_senatum = contrumsenatum_voting()
    # old voters die
    for i in voters:
        if i.generation < year:
            del voters[i.index()]
    # new children
    for i in voters:
        i.reproduce()
    # lawmaking

def year_type_5(reps, senators, contra_domus, contrum_senatum): # old reps leave, new reps voted for, old senate leave, new senate voted for, old voters die, new children are born, lawmaking ~ happens on every year divisible by 6 after 0
    # old reps leave
    reps = []
    # new reps voted for
    reps_voting()
    # old senate leave
    senators = []
    # new senate voted for
    senate_voting()
    # old voters die
    for i in voters:
        if i.generation < year:
            del voters[i.index()]
    # new children
    for i in voters:
        i.reproduce()
    # lawmaking

def year_type_6(reps, senators, contra_domus, contrum_senatum): # old reps leave, new reps voted for, old concid leave, new concid voted for, old senate leave, new senate voted for, old voters die, new children are born, lawmaking ~ happens on every year divisible by both 4 and 6 after 0
    # old reps leave
    reps = []
    # new reps voted for
    reps_voting()
    # old concid leave
    # new concid voted for
    contra_domus = contradomus_voting()
    contrum_senatum = contrumsenatum_voting()
    # old senate leave
    senators = []
    # new senate voted for
    senate_voting()
    # old voters die
    for i in voters:
        if i.generation < year:
            del voters[i.index()]
    # new children
    for i in voters:
        i.reproduce()
    # lawmaking

year_type_0(reps, senators, contra_domus, contrum_senatum)
# the display, using pygame
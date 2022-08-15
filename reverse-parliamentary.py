import random
from types import NoneType

# ADDITIONAL NOTES
# → - two executives
#   - a set amount of laws per year - manual input or a set amount can be built in
# → - go through entire legislative process rather than just simple voting
# → - full political compass; left-right and libertarian-authoritarian (array)
# → - get rid of global variables
# → - object-oriented legislature
# → - the parents will survive 1 year.
#   - media influence can skew the voting by a certain amount - manual input
# → - law creation is skewed toward the position of the legislative, not just random from their side
# → - reproduction is yearly, for simplicity of elections

# variables
voters = []
year = 0
day = 1
new_voters = []
old_voters = []
results = []
# CONSTANTS
VOTERS_PER_STATE = 200 # Default: 200
STATES = {0:"AK",1:"AL",2:"AR",3:"AZ",4:"CA",5:"CO",6:"CT",7:"DE",8:"FL",9:"GA",10:"HI",11:"IA",12:"ID",13:"IL",14:"IN",15:"KS",16:"KY",17:"LA",18:"MA",19:"MD",20:"ME",21:"MI",22:"MN",23:"MO",24:"MS",25:"MT",26:"NC",27:"ND",28:"NE",29:"NH",30:"NJ",31:"NM",32:"NV",33:"NY",34:"OH",35:"OK",36:"OR",37:"PA",38:"RI",39:"SC",40:"SD",41:"TN",42:"TX",43:"UT",44:"VA",45:"VT",46:"WA",47:"WI",48:"WV",49:"WY"}
REPS_PER_STATE = {"AK":1,"AL":7,"AR":4,"AZ":9,"CA":53,"CO":7,"CT":5,"DE":1,"FL":27,"GA":14,"HI":2,"IA":4,"ID":2,"IL":18,"IN":9,"KS":4,"KY":6,"LA":6,"MA":9,"MD":8,"ME":2,"MI":14,"MN":8,"MO":8,"MS":4,"MT":1,"NC":13,"ND":1,"NE":3,"NH":2,"NJ":12,"NM":3,"NV":4,"NY":27,"OH":16,"OK":5,"OR":5,"PA":18,"RI":2,"SC":7,"SD":1,"TN":9,"TX":36,"UT":4,"VA":11,"VT":1,"WA":10,"WI":8,"WV":3,"WY":1}
FULL_COMPASS_TO_CORNER = {1:1,2:1,6:1,7:1,3:2,4:2,8:2,9:2,5:3,26:3,10:3,31:3,27:4,28:4,32:4,33:4,29:5,30:5,34:5,35:5,11:6,12:6,16:6,17:6,13:7,14:7,18:7,19:7,15:8,36:8,20:8,41:8,37:9,38:9,42:9,43:9,39:10,40:10,44:10,45:10,21:11,22:11,51:11,52:11,23:12,24:12,53:12,54:12,25:13,46:13,55:13,76:13,47:14,48:14,77:14,78:14,49:15,50:15,79:15,80:15,56:16,57:16,61:16,62:16,58:17,59:17,63:17,64:17,60:18,81:18,65:18,86:18,82:19,83:19,87:19,88:19,84:20,85:20,89:20,90:20,66:21,67:21,71:21,72:21,68:22,69:22,73:22,74:22,70:23,91:23,75:23,96:23,92:24,93:24,97:24,98:24,94:25,95:25,99:25,100:25}
RUNTIME = 100
PERCENTAGES = {1:90, 2:80, 3:70, 4:60, 5:50, 6:40, 7:30, 8:20, 9:10}
# Classes
# Voter class
class Voter: # The voter class will have methods of voting for the position for the legislature, voting for the executive, and reproduction 
    def __init__(self, parent, parent_vote, parent_corner, will_follow_parent): #(self, bool, int, str, bool)
        self.leg_vote = 0                               # the vote the voter will place for the legislative branch.                - int
        self.exe_vote = 0                               # the vote the voter will place for the executive branch                   - int
        self.parent = parent                            # whether or not this voter has a parent                                   - bool
        self.parent_vote = parent_vote                  # the parent of this voter's previous legislative vote                     - int
        self.parent_corner = parent_corner              # the parent of this voter's previous corner                               - str
        self.will_follow_parent = will_follow_parent    # whether or not this voter will follow their parent                       - bool
    def leg_voting(self): # Each voter will place their vote, an integer 1-100, representing a coordinate on the political compass, for 2 senators and for the number of representatives their state is allotted. Voting procedure depends on the generation. Happens every 2 years.
        if self.parent == True: self.leg_vote = parent_vote_math(self.parent_vote, self.will_follow_parent, self.parent_corner)
        else: self.leg_vote = random.randint(1,100)
    def exe_voting(self, leg_corner, leg_pos): # Each voter will place their vote, an integer either 1-25, 26-50, 51-75, or 76-100, (these corners are named AL, AR, LL, and LR, respectively) representing a coordinate on the political compass. Which corner they choose from for each executive depends on the average position of the legislators in each chamber of congress.
        if self.parent == True:
            self.exe_vote = exe_parent_vote_math(leg_pos, self, leg_corner)
        else:
            if leg_corner == "AL": add = 75
            if leg_corner == "AR": add = 50
            if leg_corner == "LL": add = 25
            if leg_corner == "LR": add = 0
            self.exe_vote = FULL_COMPASS_TO_CORNER.get(random.randint(1,100)) + add
    def reproduce(self): # Each voter will reproduce by creating a new voter and deciding whether the voter will vote the same or the opposite as this voter. In this simulation, each person has one child and has full authority on the way that they treat this child. Any outside environmental factors that may affect the child's voting decisions are ignored for variable control.
        if self.leg_vote <= 25: corner = "AL"
        if self.leg_vote > 25 and self.leg_vote <= 50: corner = "AR"
        if self.leg_vote > 50 and self.leg_vote <= 75: corner = "LL"
        if self.leg_vote > 75 and self.leg_vote <= 100: corner = "LR"
        if random.randint(0,1) == 0: will_follow_parent = True
        else: will_follow_parent = False
        child = Voter(True, self.leg_vote, corner, will_follow_parent)
        return child
# Legislator class
class Legislator: # The legislator class will have methods of breaking a tie in the contra domus and contrarum senatum elections, introducing a bill, vote on a bill as a member of a subcommittee, vote on a bill as a member of a committee, schedule a bill's consideration, debate on a bill, override a veto with a 2/3 vote of each chamber, and send a bill to the executive for reviewing
    def __init__(self, state, pos, chamber): # (self, str, int)
        self.state = state
        self.pos = pos
        self.exe_tiebreaker_vote = 0
        self.chamber = chamber
    def introduce_bill(self, last_number):
        chance = random.randint(1,100)
        if chance < 93:
            bill_pos = self.pos
        else:
            bill_pos = random.randint(1,100)
        if self.chamber == "house":
            H = Bill(bill_pos ,self.chamber, last_number + 1)
            return H
        elif self.chamber == "senate":
            S = Bill(bill_pos ,self.chamber, last_number + 1)
            return S
    def committee_vote(self, bill):
        if random.randint(1,100) < 93 and abs(bill.pos - self.pos) <= 10: committee_vote = 1
        else: committee_vote = 0
        return committee_vote
    def vote_on_final_bill(self, bill):
        if abs(bill.pos - self.pos)
    def debate(self, bill):
        if abs(bill.pos-self.pos) > 10:
            bill.pos -= self.pos - bill.pos
        else:
            bill.pos += self.pos - bill.pos
    def override(self, bill):
        if abs(bill.pos - self.pos) > 25:
            return False
        else:
            return True
    # only reps
    def break_exe_tie(self, exe_options):
        diff = 101
        for i in exe_options:
            if abs(i-self.pos) < diff:
                diff = abs(i-self.pos)
                self.exe_tiebreaker_vote = i
#Bill class
class Bill: # The Bill class will have certain properties, but no methods.
    def __init__(self, pos, chamber, number):
        global PERCENTAGES
        self.created_by = chamber
        if self.created_by == "house": self.designation = ("H." + str(number))
        if self.created_by == "senate": self.designation = ("S." + str(number))
        self.pos = pos
        self.alive = True
        self.passed = False
        self.distance, PERCENTAGES = self.determine_distance()
        self.constitutionality = None
        if self.pos < 26: self.corner = "AL"
        if self.pos > 25 and self.pos < 51: self.corner = "AR"
        if self.pos > 50 and self.pos < 76: self.corner = "LL"
        if self.pos > 75: self.corner = "LR"
    def determine_distance(self):
        global PERCENTAGES
        distance = None
        d1 = (25,46,76,55)
        d2 = (24,20,41,47,77,81,60,54)
        d3 = (23,19,15,36,42,48,78,82,86,65,59,53)
        d4 = (22,18,14,10,31,37,43,49,79,83,87,91,70,64,58,52)
        d5 = (21,17,13,9,5,26,32,38,44,50,80,84,88,92,96,75,69,63,57,51)
        d6 = (16,12,8,4,27,33,39,45,85,89,93,97,74,68,62,56)
        d7 = (11,7,3,28,34,40,90,94,98,73,67,61)
        d8 = (6,2,29,35,95,99,72,66)
        d9 = (1,30,100,71)
        dlist = [d1,d2,d3,d4,d5,d6,d7,d8,d9]
        while distance == None:
            for a in dlist:
                templist = []
                for b in a:
                    if self.pos == b:
                        templist.append(True)
                    else:
                        templist.append(False)
                if any(templist):
                    distance = dlist.index(a) + 1
        return distance, PERCENTAGES
# Executive class
class Executive: # The executive class will have methods of signing bills into law, vetoing and sending the bill back to congress, and pocket vetoing.
    def __init__(self, pos):
        self.pos = pos
        if self.pos < 26: self.corner = "AL"
        if self.pos > 25 and self.pos < 51: self.corner = "AR"
        if self.pos > 50 and self.pos < 76: self.corner = "LL"
        if self.pos > 75: self.corner = "LR"
    def sign_bill(self, bill):
        bill.passed = True
    def veto(self, bill):
        bill.alive == False
    def pocket_veto():
        pass
# Justice class
class Justice: # The Justice class will have methods of declaring laws constitutional and declaring laws unconstitutional.
    def __init__(self, pos, bias):
        self.pos = pos
        self.bias = bias
        self.vote = None
        if self.pos < 26:
            self.corner = "AL"
            self.opp_corner = "LR"
        if self.pos > 25 and self.pos < 51:
            self.corner = "AR"
            self.opp_corner = "LL"
        if self.pos > 50 and self.pos < 76:
            self.corner = "LL"
            self.opp_corner = "AR"
        if self.pos > 75:
            self.corner = "LR"
            self.opp_corner = "AL"
    def declare_constitutional(bill):
        bill.constitutionality = True
    def declare_unconstitutional(bill):
        bill.constitutionality = False

# functions
# used by Voter class only
def parent_vote_math(parent_vote, will_follow_parent, parent_corner):
    operation_options = ["ADD", "SUBTRACT"]
    if will_follow_parent == True:
        corner = parent_corner
    else:
        if parent_corner == "AL": corner = "LR"
        if parent_corner == "AR": corner = "LL"
        if parent_corner == "LL": corner = "AR"
        if parent_corner == "LR": corner = "AL"
        parent_vote = 100 - (parent_vote - 1)
    if corner == "AL": min, max = 1, 25
    if corner == "AR": min, max = 26, 50
    if corner == "LL": min, max = 51, 75
    if corner == "LR": min, max = 76, 100
    add_or_subtract = random.choice(operation_options)
    return vote_from_parent_vote(parent_vote, min, max, add_or_subtract)
def vote_from_parent_vote(parent_vote, min, max, add_or_subtract):
    if add_or_subtract == "ADD":
        vote = parent_vote + (random.randint(1,abs(max - parent_vote) + 1) - 1)
    if add_or_subtract == "SUBTRACT":
        vote = parent_vote - (random.randint(1,abs(min - parent_vote) + 1) - 1)
    return vote
# take the voter's parent's vote and turn that into a guideline by turning the 1-100 compass into one of its corners
def exe_parent_vote_math(voter, leg_corner):
    if voter.parent_vote <= 25: parent_corner = "AL"
    if voter.parent_vote > 25 and voter.parent_vote <= 50: parent_corner = "AR"
    if voter.parent_vote > 50 and voter.parent_vote <= 75: parent_corner = "LL"
    if voter.parent_vote > 75 and voter.parent_vote <= 100: parent_corner = "LR"
    if leg_corner == "AL": add = 75
    if leg_corner == "AR": add = 50
    if leg_corner == "LL": add = 25
    if leg_corner == "LR": add = 0
    pv_in_corner = FULL_COMPASS_TO_CORNER.get(voter.parent_vote) + add
    parent_vote_math(pv_in_corner, voter.will_follow_parent, parent_corner)
# running the simulation
# create the voters/electors
def generate_gen1_voters(voters):
    for _ in range(50):
        for _ in range(VOTERS_PER_STATE):
            voter = Voter(False, None, None, None)
            voters.append(voter)
# legislative voting
# if there's a tie in voting for the people of congress:
def leg_tiebreaker(winners_list, voters, state):
    votes_for_state = []
    votes_counts = [0]
    for i in range(len(winners_list)):
        for voter in range(1,VOTERS_PER_STATE + 1):
            voters[(state*VOTERS_PER_STATE-(VOTERS_PER_STATE-voter))-1].leg_voting()
            votes_for_state.append(voters[(state*VOTERS_PER_STATE-(VOTERS_PER_STATE-voter))-1].leg_vote)
    for i in range(1,101):
        votes_counts.append(votes_for_state.count(i))
    leg_max_indices_count = max(votes_counts)
    leg_max_indices = [i for i in range(len(votes_counts)) if votes_counts[i] == leg_max_indices_count]
    return leg_max_indices
# part of voting for either part of congress
def leg_each_state(state, voters):
    votes_for_state = []
    votes_counts = [0]
    for voter in range(1,VOTERS_PER_STATE + 1):
        voters[(state*VOTERS_PER_STATE-(VOTERS_PER_STATE-voter))-1].leg_voting()
        votes_for_state.append(voters[(state*VOTERS_PER_STATE-(VOTERS_PER_STATE-voter))-1].leg_vote)
    for i in range(1,101):
        votes_counts.append(votes_for_state.count(i))
    leg_max_indices = [i for i in range(len(votes_counts)) if votes_counts[i] == max(votes_counts)]    
    while len(leg_max_indices) > 1:
        leg_max_indices = leg_tiebreaker(leg_max_indices,voters, state)
    return leg_max_indices[0]
# voting for the senate
def senate_voting(voters):
    senate_positions = []
    senate_members = []
    for state in range(1,51):
        for _ in range(1,3):
            senate_positions.append(leg_each_state(state,voters))
            senator = Legislator(STATES.get(state), senate_positions[-1], "senate")
            senate_members.append(senator)
    return senate_positions, senate_members
# voting for the house of representatives
def h_o_r_voting(voters):
    h_o_r_positions = []
    h_o_r_members = []
    for state in range(1,51):
        for _ in range(1,REPS_PER_STATE.get(STATES.get(state - 1)) + 1):
            h_o_r_positions.append(leg_each_state(state,voters))
            representative = Legislator(STATES.get(state), h_o_r_positions[-1], "house")
            h_o_r_members.append(representative)
    return h_o_r_positions, h_o_r_members
# executive voting
# tiebreaker - house of reps will vote to break a tie in the contra domus and contrum senatum elections
def exe_tiebreaker(max_indices,chamber_members):
    votes = []
    counts = []
    for i in chamber_members:
        i.break_exe_tie(max_indices)
        votes.append(i.exe_tiebreaker_vote)
    for i in range(1,101):
        counts.append(votes.count(i))
    max_indices = [i for i in range(len(counts)) if counts[i] == max(counts)]
    return max_indices
# find chamber of congress' average position and corner
def avg_pos(chamber_positions):
    chamber_avg_pos = 0
    for i in chamber_positions:
        chamber_avg_pos += i
    chamber_avg_pos = int(chamber_avg_pos / len(chamber_positions))
    if chamber_avg_pos > 100: chamber_avg_pos = 100
    if chamber_avg_pos <= 25: leg_corner = "AL"
    if chamber_avg_pos > 25 and chamber_avg_pos <= 50: leg_corner = "AR"
    if chamber_avg_pos > 50 and chamber_avg_pos <= 75: leg_corner = "LL"
    if chamber_avg_pos > 75 and chamber_avg_pos <= 100: leg_corner = "LR"
    return chamber_avg_pos, leg_corner
# voting for the contra domus
def c_d_voting(voters, h_o_r_members, h_o_r_pos, h_o_r_corner):
    c_d_votes = []
    c_d_counts = [0]
    for i in voters:
        i.exe_voting(h_o_r_corner, h_o_r_pos)
        c_d_votes.append(i.exe_vote)
    for i in range(1,101):
        c_d_counts.append(c_d_votes.count(i))
    c_d_max_indices = [i for i in range(len(c_d_counts)) if c_d_counts[i] == max(c_d_counts)]
    while len(c_d_max_indices) > 1:
        c_d_max_indices = exe_tiebreaker(c_d_max_indices, h_o_r_members)
    c_d_pos = c_d_max_indices[0]
    contra_domus = Executive(c_d_pos)
    return contra_domus, c_d_pos
# voting for the contrum senatum
def c_s_voting(voters, senate_members, senate_pos, senate_corner):
    c_s_votes = []
    c_s_counts = [0]
    for i in voters:
        i.exe_voting(senate_corner, senate_pos)
        c_s_votes.append(i.exe_vote)
    for i in range(1,101):
        c_s_counts.append(c_s_votes.count(i))
    c_s_max_indices = [i for i in range(len(c_s_counts)) if c_s_counts[i] == max(c_s_counts)]
    while len(c_s_max_indices) > 1:
        c_s_max_indices = exe_tiebreaker(c_s_max_indices, senate_members)
    c_s_pos = c_s_max_indices[0]
    contrum_senatum = Executive(c_s_pos)
    return contrum_senatum, c_s_pos
# the CD chooses 4 of the nine justices
justices = []
def c_d_jchoice(executive):
    global justices
    for i in range(4):
        bias = random.randint(1,5)
        if executive.corner == "AL": jpos = 25 - bias
        if executive.corner == "AR": jpos = 46 - bias
        if executive.corner == "LL": jpos = 55 + bias
        if executive.corner == "LR": jpos = 76 + bias
        justice = Justice(jpos, bias)
        justices.append(justice)
# the CS chooses 4 of the nine justices
def c_s_jchoice(executive):
    global justices
    for i in range(4):
        bias = random.randint(1,5)
        if executive.corner == "AL": jpos = 25 - bias
        if executive.corner == "AR": jpos = 46 - bias
        if executive.corner == "LL": jpos = 55 + bias
        if executive.corner == "LR": jpos = 76 + bias
        justice = Justice(jpos, bias)
        justices.append(justice)
# the CS and CD have to agree on the position of the final justice
def combined_jchoice(CD, CS):
    global justices
    bias = random.randint(1,5)
    if CD.corner == "AL": jpos = 25 - bias
    if CD.corner == "AR": jpos = 46 - bias
    if CD.corner == "LL": jpos = 55 + bias
    if CD.corner == "LR": jpos = 76 + bias
    CDjustice = Justice(jpos, bias)
    bias = random.randint(1,5)
    if CS.corner == "AL": jpos = 25 - bias
    if CS.corner == "AR": jpos = 46 - bias
    if CS.corner == "LL": jpos = 55 + bias
    if CS.corner == "LR": jpos = 76 + bias
    CSjustice = Justice(jpos, bias)
    justice = Justice(int((CSjustice.pos + CDjustice.pos) / 2), int((CDjustice.bias + CSjustice.bias) / 2))
    justices.append(justice)

# lawmaking
def congress_lawmaking(congress_members, h_o_r_members, senate_members):
    last_number = 0
    committee_votes = []
    house_votes = []
    senate_votes = []
    final_votes = []
    sum_vote = 0
    bill = congress_members[random.randint(1,len(congress_members)-1)].introduce_bill(last_number)
    original_bill_pos =  bill.pos
    committee_center = random.randint(2,len(congress_members)-2)
    for i in range(-2, 2):
        committee_votes.append(congress_members[committee_center + i].committee_vote(bill))
    for i in committee_votes:
        sum_vote += i
    if sum_vote / 5 < 0.5:
        bill.alive = False
    if bill.alive == True:
        house_bill_pos = 0
        senate_bill_pos = 0
        if random.randint(0,6) < 4:
            for i in h_o_r_members:
                i.debate(bill)
            supermajority = False
        else: supermajority = True
        for i in h_o_r_members:
            if abs(bill.pos - i.pos) > 10:
                house_votes.append(False)
            else:
                house_votes.append(True)
        if max(house_votes) == False: bill.alive = False
        if supermajority == True and round(len(house_votes)/house_votes.count(True), 2) < 0.67: bill.alive = False
        if bill.alive == True:
            house_bill_pos = bill.pos
            bill.pos = original_bill_pos
        if random.randint(0,6) < 4:
            for i in senate_members:
                i.debate(bill)
        else: supermajority = True
        for i in senate_members:
            if abs(bill.pos - i.pos) > 10:
                senate_votes.append(False)
            else:
                senate_votes.append(True)
        if max(senate_votes) == False: bill.alive = False
        if senate_votes.count(True) > 0:
            if supermajority == True and round(len(senate_votes)/senate_votes.count(True), 2) < 0.67: bill.alive = False
        if bill.alive == True:
            senate_bill_pos = bill.pos
            bill.pos = original_bill_pos
        if house_bill_pos != 0 and senate_bill_pos != 0:
            bill.pos = int(house_bill_pos + senate_bill_pos / 2)
        elif house_bill_pos == 0:
            bill.pos = senate_bill_pos
        elif senate_bill_pos == 0:
            bill.pos = house_bill_pos
        for i in congress_members:
            final_votes.append(i.vote_on_final_bill(bill))
    return bill

def executive_lawmaking(executive, bill):
    if abs(bill.pos - executive.pos) > 25:
        executive.veto(bill)
    else:
        executive.sign_bill(bill)
    if bill.alive == False: vetoed = True
    else: vetoed = False
    return bill, vetoed
    
def congress_override(bill, congress_members):
    congress_pos = 0
    override_votes = []
    for i in congress_members:
        congress_pos += i.pos
    congress_pos /= len(congress_members)
    if abs(bill.pos - congress_pos) < 10:
        if random.randint(1,1000) > 994:
            for i in congress_members:
                override_votes.append(i.override(bill))
            if int(override_votes.count(True) / len(override_votes) * 10) >= 6:
                bill.alive = True
    return bill

def judicial_review(bill, justices):
    global PERCENTAGES
    votes = []
    for i in justices:
        if bill.corner == i.corner:
            if random.randint(1,100) < PERCENTAGES.get(bill.distance) + i.bias:
                i.vote = True
            else: i.vote = False
        if bill.corner == i.opp_corner:
            if random.randint(1,100) < PERCENTAGES.get(bill.distance) - i.bias:
                i.vote = True
            else: i.vote = False
        votes.append(i.vote)
    if votes.count(True) > votes.count(False):
        i.declare_constitutional()
    else: i.declare_unconstitutional()
    return bill

congress_members = []
generate_gen1_voters(voters)
if year % 2 == 0:
    h_o_r_positions, h_o_r_members = h_o_r_voting(voters)
    h_o_r_pos, h_o_r_corner = avg_pos(h_o_r_positions)
if year % 6 == 0:
    senate_positions, senate_members = senate_voting(voters)
    senate_pos, senate_corner = avg_pos(senate_positions)
if year % 4 == 0:
    contra_domus, c_d_pos = c_d_voting(voters, h_o_r_members, h_o_r_pos, h_o_r_corner)
    contrum_senatum, c_s_pos = c_s_voting(voters, senate_members, senate_pos, senate_corner)
    c_d_jchoice(contra_domus)
    c_s_jchoice(contrum_senatum)
    combined_jchoice(contra_domus, contrum_senatum)
for i in h_o_r_members:
    congress_members.append(i)
for i in senate_members:
    congress_members.append(i)
justice_bias = []
judicial_bias = 0
for i in justices:
    justice_bias.append(i.bias)
    judicial_bias += i.bias

while year <= RUNTIME:
    while day <= 365:
        for i in range(0, 44):
            bill = congress_lawmaking(congress_members, h_o_r_members, senate_members)
            if bill.alive == True: bill, vetoed = executive_lawmaking(contra_domus, bill)
            else: vetoed = False
            if bill.alive == False and vetoed == True: bill = congress_override(bill, congress_members)
            if bill.alive == True: bill = judicial_review(bill, justices)
            if bill.alive == True and bill.constitutionality == True:
                results.append(0)
            elif bill.alive == False or bill.constitutionality == None:
                results.append(1)
            elif bill.constitutionality == False:
                results.append(2)
        day += 1
    day = 1
    year += 1
    print("Year", year)

print("Bills passed this run:", results.count(0))
print("Bills that died before constitutionality check:", results.count(1))
print("Bills that were found unconstitutional:", results.count(2))
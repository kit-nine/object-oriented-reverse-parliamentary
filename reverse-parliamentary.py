import random

# ADDITIONAL NOTES
#   - two executives
#   - a set amount of laws per generation - manual input or a set amount can be built in
#   - go through entire legislative process rather than just simple voting
#   - full political compass; left-right and libertarian-authoritarian (array)
#   - get rid of global variables
#   - object-oriented legislature
#   - the parents will survive 1 generation.
#   - media influence can skew the voting by a certain amount - manual input
#   - law creation is skewed toward the position of the legislative, not just random from their side
#   - VP instead of a randint for the tiebreaker
#   - if there are not 100 candidates for each position, the number a voter chooses will change into that of the candidate with the smallest absolute difference from the original vote. If multiple share the same absolute difference, the voter will choose randomly (plus media influence) from the multiple.
#   - reproduction is yearly, for simplicity of elections

# variables
voters = []
year = 0
new_voters = []
old_voters = []
# CONSTANTS
VOTERS_PER_STATE = 200 # Default: 200
STATES = {0:"AK",1:"AL",2:"AR",3:"AZ",4:"CA",5:"CO",6:"CT",7:"DE",8:"FL",9:"GA",10:"HI",11:"IA",12:"ID",13:"IL",14:"IN",15:"KS",16:"KY",17:"LA",18:"MA",19:"MD",20:"ME",21:"MI",22:"MN",23:"MO",24:"MS",25:"MT",26:"NC",27:"ND",28:"NE",29:"NH",30:"NJ",31:"NM",32:"NV",33:"NY",34:"OH",35:"OK",36:"OR",37:"PA",38:"RI",39:"SC",40:"SD",41:"TN",42:"TX",43:"UT",44:"VA",45:"VT",46:"WA",47:"WI",48:"WV",49:"WY"}
REPS_PER_STATE = {"AK":1,"AL":7,"AR":4,"AZ":9,"CA":53,"CO":7,"CT":5,"DE":1,"FL":27,"GA":14,"HI":2,"IA":4,"ID":2,"IL":18,"IN":9,"KS":4,"KY":6,"LA":6,"MA":9,"MD":8,"ME":2,"MI":14,"MN":8,"MO":8,"MS":4,"MT":1,"NC":13,"ND":1,"NE":3,"NH":2,"NJ":12,"NM":3,"NV":4,"NY":27,"OH":16,"OK":5,"OR":5,"PA":18,"RI":2,"SC":7,"SD":1,"TN":9,"TX":36,"UT":4,"VA":11,"VT":1,"WA":10,"WI":8,"WV":3,"WY":1}
FULL_COMPASS_TO_CORNER = {1:1,2:1,6:1,7:1,3:2,4:2,8:2,9:2,5:3,26:3,10:3,31:3,27:4,28:4,32:4,33:4,29:5,30:5,34:5,35:5,11:6,12:6,16:6,17:6,13:7,14:7,18:7,19:7,15:8,36:8,20:8,41:8,37:9,38:9,42:9,43:9,39:10,40:10,44:10,45:10,21:11,22:11,51:11,52:11,23:12,24:12,53:12,54:12,25:13,46:13,55:13,76:13,47:14,48:14,77:14,78:14,49:15,50:15,79:15,80:15,56:16,57:16,61:16,62:16,58:17,59:17,63:17,64:17,60:18,81:18,65:18,86:18,82:19,83:19,87:19,88:19,84:20,85:20,89:20,90:20,66:21,67:21,71:21,72:21,68:22,69:22,73:22,74:22,70:23,91:23,75:23,96:23,92:24,93:24,97:24,98:24,94:25,95:25,99:25,100:25}
RUNTIME = 6
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
    def introduce_bill(self):
        pass
    def subcommittee_vote(self):
        pass
    def committee_vote(self):
        pass
    def schedule_bill(self):
        pass
    def debate(self):
        pass
    def veto_override(self):
        pass
    def send_bill(self):
        pass
    # only reps
    def break_exe_tie(self, exe_options):
        diff = 101
        for i in exe_options:
            if abs(i-self.pos) < diff:
                diff = abs(i-self.pos)
                self.exe_tiebreaker_vote = i
    # only senators
    def filibuster():
        pass
    def envoke_closure():
        pass
    def conference_committee_meeting():
        pass
# Executive class
class Executive: # The executive class will have methods of signing bills into law, vetoing and sending the bill back to congress, and pocket vetoing.
    def __init__(self, pos):
        self.pos = pos
    def sign_bill():
        pass
    def veto():
        pass
    def pocket_veto():
        pass
# Judiciary class
class Judiciary: # The Judiciary class will have methods of declaring laws constitutional and declaring laws unconstitutional.
    def __init__():
        pass
    def declare_constitutional():
        pass
    def declare_unconstitutional():
        pass

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
def c_d_voting(voters, h_o_r_positions, h_o_r_members):
    c_d_votes = []
    c_d_counts = [0]
    h_o_r_pos, h_o_r_corner = avg_pos(h_o_r_positions)
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
    return contra_domus, c_d_pos, h_o_r_pos
# voting for the contrum senatum
def c_s_voting(voters, senate_positions, senate_members):
    c_s_votes = []
    c_s_counts = [0]
    senate_pos, senate_corner = avg_pos(senate_positions)
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
    return contrum_senatum, c_s_pos, senate_pos
# testing
generate_gen1_voters(voters)
for i in range(RUNTIME):
    if year == 0 or year % 2 == 0:
        h_o_r_positions, h_o_r_members = h_o_r_voting(voters)
    if year == 0 or year % 6 == 0:
        senate_positions, senate_members = senate_voting(voters)
    if year == 0 or year % 4 == 0:
        contra_domus, c_d_pos, h_o_r_pos = c_d_voting(voters, h_o_r_positions, h_o_r_members)
        contrum_senatum, c_s_pos, senate_pos = c_s_voting(voters, senate_positions, senate_members)
    year += 1
    old_voters.clear()
    for i in range(len(voters)):
        new_voters.append(voters[i].reproduce())
        old_voters.append(voters[i])
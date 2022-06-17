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

# CONSTANTS
VOTERS_PER_STATE = 200 # Default: 200
states = {0: "AK",1: "AL",2: "AR",3: "AZ",4: "CA",5: "CO",6: "CT",7: "DE",8: "FL",9: "GA",10: "HI",11: "IA",12: "ID",13: "IL",14: "IN",15: "KS",16: "KY",17: "LA",18: "MA",19: "MD",20: "ME",21: "MI",22: "MN",23: "MO",24: "MS",25: "MT",26: "NC",27: "ND",28: "NE",29: "NH",30: "NJ",31: "NM",32: "NV",33: "NY",34: "OH",35: "OK",36: "OR",37: "PA",38: "RI",39: "SC",40: "SD",41: "TN",42: "TX",43: "UT",44: "VA",45: "VT",46: "WA",47: "WI",48: "WV",49: "WY"}
reps_per_state = {"AK": 1,"AL": 7,"AR": 4,"AZ": 9,"CA": 53,"CO": 7,"CT": 5,"DE": 1,"FL": 27,"GA": 14,"HI": 2,"IA": 4,"ID": 2,"IL": 18,"IN": 9,"KS": 4,"KY": 6,"LA": 6,"MA": 9,"MD": 8,"ME": 2,"MI": 14,"MN": 8,"MO": 8,"MS": 4,"MT": 1,"NC": 13,"ND": 1,"NE": 3,"NH": 2,"NJ": 12,"NM": 3,"NV": 4,"NY": 27,"OH": 16,"OK": 5,"OR": 5,"PA": 18,"RI": 2,"SC": 7,"SD": 1,"TN": 9,"TX": 36,"UT": 4,"VA": 11,"VT": 1,"WA": 10,"WI": 8,"WV": 3,"WY": 1}


# Classes
# Voter class
class Voter: # The voter class will have methods of voting for the position for the legislature, voting for the executive, and reproduction 
    def __init__(self, leg_corner, parent, parent_vote, parent_corner, will_follow_parent): #(self, str, bool, int, str, bool)
        self.which_leg = "NULL"                         # which chamber of congress the voter is currently voting legislators into - str
        self.which_exe = "NULL"                         # which executive the voter is currently voting for                        - str
        self.leg_vote = 0                               # the vote the voter will place for the legislative branch.                - int
        self.exe_vote = 0                               # the vote the voter will place for the executive branch                   - int
        self.leg_corner = leg_corner                    # the corner of the chamber of congress the executive is associated with   - str
        self.exe_corner = "NULL"                        # the corner the voter must choose from for the executive                  - str
        self.parent = parent                            # whether or not this voter has a parent                                   - bool
        self.parent_vote = parent_vote                  # the parent of this voter's previous vote                                 - int
        self.parent_corner = parent_corner              # the parent of this voter's previous corner                               - str
        self.will_follow_parent = will_follow_parent    # whether or not this voter will follow their parent                       - bool
    def leg_voting(self): # Each voter will place their vote, an integer 1-100, representing a coordinate on the political compass, for 2 senators and for the number of representatives their state is allotted. Voting procedure depends on the generation. Happens every 2 years.
        if self.parent == True: self.leg_vote = parent_vote_math(self.parent_vote, self.will_follow_parent, self.parent_corner)
        else: self.leg_vote = random.randint(1,100)
        return self.leg_vote
    def exe_voting(): # Each voter will place their vote, an integer either 1-25, 26-50, 51-75, or 76-100, (these corners are named AL, AR, LL, and LR, respectively) representing a coordinate on the political compass. Which corner they choose from for each executive depends on the average position of the legislators in each chamber of congress.
        pass
    def reproduce(): # Each voter will reproduce by creating a new voter and deciding whether the voter will vote the same or the opposite as this voter. In this simulation, each person has one child and has full authority on the way that they treat this child. Any outside environmental factors that may affect the child's voting decisions are ignored for variable control.
        pass
# Legislator class
class Legislator: # The legislator class will have methods of introducing a bill, vote on a bill as a member of a subcommittee, vote on a bill as a member of a committee, schedule a bill's consideration, debate on a bill, override a veto with a 2/3 vote of each chamber, and send a bill to the executive for reviewing
    def __init__(self, state, pos): # (self, str, int)
        self.state = state
        self.pos = pos
    def introduce_bill():
        pass
    def subcommittee_vote():
        pass
    def committee_vote():
        pass
    def schedule_bill():
        pass
    def debate():
        pass
    def veto_override():
        pass
    def send_bill():
        pass
# Senator subclass
class Senator(Legislator): # The senator subclass of the legislator class will have all the methods of the legislator class, along with filibustering and envoking a closure with a supermajority of 60 votes.
    def __init__():
        pass
    def filibuster():
        pass
    def envoke_closure():
        pass
# Conference Committee subclass
class ConferenceCommittee(Legislator): # The conference committee subclass will have all the methods of the legislator class, along with meeting to bring the bills into alignment.
    def __init__():
        pass
    def meet():
        pass
# Executive class
class Executive: # The executive class will have methods of signing bills into law, vetoing and sending the bill back to congress, and pocket vetoing.
    def __init__():
        pass
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
# running the simulation
# create the voters/electors
def generate_gen1_voters(voters):
    for state in range(50):
        for _ in range(VOTERS_PER_STATE):
            voter = Voter(states.get(state), "NULL", False, 0, "NULL", False)
            voters.append(voter)
# if there's a tie in voting for the people of congress:
def leg_tiebreaker(winners_list, voters, votes_for_state,votes_counts,state):
    for i in range(len(winners_list)):
        for voter in range(1,VOTERS_PER_STATE + 1):
            voters[(state*VOTERS_PER_STATE-(VOTERS_PER_STATE-voter))-1].leg_voting()
            votes_for_state.append(voters[(state*VOTERS_PER_STATE-(VOTERS_PER_STATE-voter))-1].leg_vote)
    for i in range(1,101):
        votes_counts.append(votes_for_state.count(i))
    winner_or_winners_count = max(votes_counts)
    winner_or_winners = [i for i in range(len(votes_counts)) if votes_counts[i] == winner_or_winners_count]
    return winner_or_winners
# part of voting for either part of congress
def leg_each_state(state, voters):
    votes_for_state = []
    votes_counts = [0]
    for voter in range(1,VOTERS_PER_STATE + 1):
        voters[(state*VOTERS_PER_STATE-(VOTERS_PER_STATE-voter))-1].leg_voting()
        votes_for_state.append(voters[(state*VOTERS_PER_STATE-(VOTERS_PER_STATE-voter))-1].leg_vote)
    for i in range(1,101):
        votes_counts.append(votes_for_state.count(i))
    winner_or_winners = [i for i in range(len(votes_counts)) if votes_counts[i] == max(votes_counts)]    
    while len(winner_or_winners) > 1:
        winner_or_winners = leg_tiebreaker(winner_or_winners,voters,votes_for_state, votes_counts, state)
    return winner_or_winners[0]
# voting for the senate
def senate_voting(voters):
    senate_members = []
    for state in range(1,51):
        for _ in range(2):
            senate_members.append_(leg_each_state(state,voters))
    return senate_members
# voting for the house of representatives
def h_o_r_voting(voters):
    h_o_r_members = []
    for state in range(1,51):
        for _ in range(1,reps_per_state.get(states.get(state - 1)) + 1):
            h_o_r_members.append(leg_each_state(state,voters))
    return h_o_r_members
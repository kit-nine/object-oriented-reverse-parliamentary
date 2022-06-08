# mommys_cat = Voter("FL", 76, False, 0, "NULL", False)

import random

# ADDITIONAL NOTES
#   - two executives
#   - a set amount of laws per generation - manual input or a set amount can be built in
#   - go through entire legislative process rather than just simple voting
#   - full political compass; left-right and libertarian-authoritarian (array)
#   - get rid of global variables
#   - object-oriented legislature
#   - more_gens() will have parameter gens, set it equal to the number of gens to test minus one - manual input
#   - the parents will survive 2 generations.
#   - the parents will have a 2 out of 3 chance of voting the same every generation.
#   - otherwise they will randomly choose every time.
#   - media influence can skew the voting by a certain amount - manual input
#   - law creation is skewed toward the position of the legislative, not just random from their side
#   - another voting session instead of a randint for the tiebreaker
#   - if there are not 100 candidates for each position, the number a voter chooses will change into that of the candidate with the smallest absolute difference from the original vote. If multiple share the same absolute difference, the voter will choose randomly (plus media influence) from the multiple.
#   - reproduction is yearly, for simplicity of elections

# variables



# CONSTANTS



# Classes
# Voter class
class Voter: # The voter class will have methods of voting for the legislature, voting for the executive, and reproduction 
    def __init__(self, state, leg_corner, parent, parent_vote, parent_corner, will_follow_parent): #(self, str, str, bool, int, str, bool)
        self.which_leg = "NULL"                         # which chamber of congress the voter is currently voting legislators into - str
        self.which_exe = "NULL"                         # which executive the voter is currently voting for                        - str
        self.leg_vote = 0                               # the vote the voter will place for the legislative branch.                - int
        self.state = state                              # the state the voter represents                                           - str
        self.exe_vote = 0                               # the vote the voter will place for the executive branch                   - int
        self.leg_corner = leg_corner                    # the corner of the chamber of congress the executive is associated with   - str
        self.exe_corner = "NULL"                        # the corner the voter must choose from for the executive                  - str
        self.parent = parent                            # whether or not this voter has a parent                                   - bool
        self.parent_vote = parent_vote                  # the parent of this voter's previous vote                                 - int
        self.parent_corner = parent_corner              # the parent of this voter's previous corner                               - str
        self.will_follow_parent = will_follow_parent    # whether or not this voter will follow their parent                       - bool
    def leg_voting(self): # Each voter will place their vote, an integer 1-100, representing a coordinate on the political compass, for 2 senators and for the number of representatives their state is allotted. Voting procedure depends on the generation. Happens every 2 years.
        if self.parent == True:
            self.leg_vote = parent_vote_math(self.parent_vote, self.will_follow_parent, self.parent_corner)
        else: self.leg_vote = random.randint(1,100)
        print(self.leg_vote)
    def exe_voting(): # Each voter will place their vote, an integer either 1-25, 26-50, 51-75, or 76-100, (these corners are named AL, AR, LL, and LR, respectively) representing a coordinate on the political compass. Which corner they choose from for each executive depends on the average position of the legislators in each chamber of congress.
        pass
    def reproduce(): # Each voter will reproduce by creating a new voter and deciding whether the voter will vote the same or the opposite as this voter. In this simulation, each person has one child and has full authority on the way that they treat this child. Any outside environmental factors that may affect the child's voting decisions are ignored for variable control.
        pass
# Legislator class
class Legislator: # The legislator class will have methods of introducing a bill, vote on a bill as a member of a subcommittee, vote on a bill as a member of a committee, schedule a bill's consideration, debate on a bill, override a veto with a 2/3 vote of each chamber, and send a bill to the executive for reviewing
    def __init__():
        pass
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
    if corner == "AL":
        min = 1
        max = 25
    if corner == "AR":
        min = 26
        max = 50
    if corner == "LL":
        min = 51
        max = 75
    if corner == "LR":
        min = 76
        max = 100
    add_or_subtract = random.choice(operation_options)
    return vote_from_parent_vote(parent_vote, min, max, add_or_subtract)

def vote_from_parent_vote(parent_vote, min, max, add_or_subtract):
    if add_or_subtract == "ADD":
        vote = parent_vote + (random.randint(1,1) - 1)
    if add_or_subtract == "SUBTRACT":
        vote = parent_vote - (random.randint(1,1) - 1)
    return vote

test = Voter("FL", "NULL", True, 75, "LL", True)
test.leg_voting()
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
    def __init__(self, state, leg_corner, parent_corner, parent):
        self.which_leg = 0                  # which chamber of congress the voter is currently voting legislators into 
        self.which_exe = 0                  # which executive the voter is currently voting for
        self.leg_vote = 0                   # the vote the voter will place for the legislative branch.
        self.state = state                  # the state the voter represents
        self.exe_vote = 0                   # the vote the voter will place for the executive branch
        self.leg_corner = leg_corner        # the corner of the chamber of congress the executive is associated with
        self.exe_corner = 0                 # the corner the voter must choose from for the executive
        self.parent_corner = parent_corner  # the parent of this voter's previous corner
        self.parent = parent                # whether or not this voter will follow their parent
    def leg_voting(self): # Each voter will place their vote, an integer 1-100, representing a coordinate on the political compass, for 2 senators and for the number of representatives their state is allotted. Voting procedure depends on the generation. Happens every 2 years.
        if self.parent == False:
            if self.parent_corner == "AL":
                self.leg_vote = random.randint(76,100)
            if self.parent_corner == "AR":
                self.leg_vote = random.randint(51,75)
            if self.parent_corner == "LL":
                self.leg_vote = random.randint(26,50)
            if self.parent_corner == "LR":
                self.leg_vote = random.randint(1,25)
        if self.parent == True:
            if self.parent_corner == "AL":
                self.leg_vote = random.randint(1,25)
            if self.parent_corner == "AR":
                self.leg_vote = random.randint(26,50)
            if self.parent_corner == "LL":
                self.leg_vote = random.randint(51,75)
            if self.parent_corner == "LR":
                self.leg_vote = random.randint(76,100)
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



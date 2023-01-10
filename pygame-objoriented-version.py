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
#variables
fps_clock = pygame.time.Clock()
WINDOW = pygame.display.set_mode((1109,515))
YEARS = 1000
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
senators = []
reps = []
font = pygame.font.Font(None, 50)
loop = True
year = 0
DISPLAY_BG = pygame.image.load('display background.png')
DISPLAY_KEY = pygame.image.load('display key.png')
congress_avgpos_o, senate_avgpos_o, house_avgpos_o, conciduorum_avgpos_o, contrumsenatum_avgpos_o, contradomus_avgpos_o, with_parent_o, against_parent_o = 0, 0, 0, 0, 0, 0, 0, 0
YEARLY_SENATE_POS_COORDS = ()
YEARLY_HOUSE_POS_COORDS = ()
YEARLY_CONGRESS_POS_COORDS = ()
YEARLY_CS_POS_COORDS = ()
YEARLY_CD_POS_COORDS = ()
YEARLY_CONCID_POS_COORDS = ()
OVERALL_SENATE_POS_COORDS = ()
OVERALL_HOUSE_POS_COORDS = ()
OVERALL_CONGRESS_POS_COORDS = ()
OVERALL_CS_POS_COORDS = ()
OVERALL_CD_POS_COORDS = ()
OVERALL_CONCID_POS_COORDS = ()
YEARLY_WITH_PARENT_COORDS = ()
YEARLY_AGAINST_PARENT_COORDS = ()
OVERALL_WITH_PARENT_COORDS = ()
OVERALL_AGAINST_PARENT_COORDS = ()
# output_coords = None
# put the object-oriented reverse parliamentary system code here
# congress
class Senator():
    def __init__(self, pos):
        self.pos = pos
class Representative():
    def __init__(self, pos):
        self.pos = pos
# conciduorum
class ContraDomus():
    def __init__(self, pos):
        self.pos = pos
class ContrumSenatum():
    def __init__(self, pos):
        self.pos = pos
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
        self.parent = None # whether this voter votes with or against their parent
    def s_voting(self): # vote for the senators from the voter's state
        self.s_vote = skew(self.pos - 1, self.pos + 1)
    def cs_voting(self): # vote for the contrum senatum
        self.cs_vote = skew(self.pos - 1, self.pos + 1)
    def r_voting(self): # vote for the reps from the voter's state
        self.r_vote = skew(self.pos - 1, self.pos + 1)
    def cd_voting(self): # vote for the contra domus
        self.cd_vote = skew(self.pos - 1, self.pos + 1)
# FUNCTIONSs
# randomness skew function
def skew(min, max): # both min and max are inclusive
    output = random.randint(min, max)
    output * (1 + SKEW)
    return int(output)
# create the compass
for cols in range(11):
    for rows in range(11): temp.append((rows - 5, cols + (10 - 5 - (2 * cols))))
    grid.append(temp)
    temp = []
# output_coords = grid[(6 - Y) - 1][(6 + X) - 1]
# create the voters
for i in range(50):
    for i_1 in range(VOTERS_PER_STATE): voter = Voter(i, grid[(6 - skew(-5, 5)) - 1][(6 + skew(-5, 5)) - 1])
# the display, using pygame
WINDOW.blit(DISPLAY_KEY, (0,0))

while loop == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_s: WINDOW.blit(DISPLAY_BG, (0,0))
            if event.key == K_k: WINDOW.blit(DISPLAY_KEY, (0,0))
            if event.key == K_SPACE:
                year += 1
                if year > 1: pygame.draw.rect(WINDOW, (174,67,255), year_rect)
                year_obj = font.render(str(year), False, (255,255,255))
                year_rect = year_obj.get_rect()
                year_rect.topleft = (25,40)
                WINDOW.blit(year_obj, year_rect)
                # every 2 years
                if i % 2 == 0:
                    # voters vote for the senators from their state
                    for i_1 in voters:
                        for i_2 in range(2):
                            avgvote = 0
                            s_votes.append(i_1.s_voting())
                            for i_3 in s_votes: avgvote += i_3
                            avgvote = int(avgvote / len(s_votes))
                            senator = Senator(avgvote)
                            senators.append(senator)
                            s_votes.clear
                # every 4 years
                if i % 4 == 0:
                    # voters vote for the conciduorum members
                    for i_1 in voters:
                        cs_votes.append(i_1.cs_voting())
                        avgvote = 0
                        for i_2 in cs_votes: avgvote += i_2
                    avgvote = int(avgvote / len(s_votes))
                    contrum_senatum = ContrumSenatum(avgvote)
                    for i_1 in voters:
                        cd_votes.append(i_1.cd_voting())
                        for i_2 in cd_votes: avgvote += i_2
                    avgvote = int(avgvote / len(s_votes))
                    contra_domus = ContraDomus(avgvote)
                # every 6 years
                if i % 6 == 0:
                    # voters vote for the HOR reps from their state
                    for i_1 in voters:
                        for i_2 in range(REPS_PER_STATE.get(STATES.get(i_1.state))):
                            avgvote = 0
                            r_votes.append(i_1.r_voting())
                            for i_3 in r_votes: avgvote += i_3
                            avgvote = int(avgvote / len(s_votes))
                            representative = Representative(avgvote)
                            reps.append(representative)
                            r_votes.clear()
                # every year
                    # lawmaking
                        # house voting
                        # senate voting
                        # conciduorum voting
                        # judicial ruling
                    # if year > 1 make new voters
                    if year > 1:
                        for i in voters:
                            temp = skew(0,1)
                            if temp == 0:
                                new_voter_pos = i.pos
                                i.parent = "w"
                            else:
                                new_voter_pos = (-(i.pos[0]), -(i.pos[1]))
                                i.parent = "a"
                            Voter(i.state, new_voter_pos)
                    # display:
                        # yearly/overall congress avgpos
                        congress_avgpos_y = 0
                        # yearly/overall senate avgpos
                        senate_avgpos_y = 0
                        for i in senators:
                            congress_avgpos_y += i.pos
                            senate_avgpos_y += i.pos
                            congress_avgpos_o += i.pos
                            senate_avgpos_o += i.pos
                        senate_avgpos_y = int(senate_avgpos_y / 100)
                        temp = int(senate_avgpos_o / (100 * year))
                        ysenatepos_obj = font.render(str(senate_avgpos_y), False, (255,255,255))
                        ysenatepos_rect = ysenatepos_obj.get_rect()
                        ysenatepos_rect.topleft = YEARLY_SENATE_POS_COORDS
                        osenatepos_obj = font.render(str(temp), False, (255,255,255))
                        osenatepos_rect = osenatepos_obj.get_rect()
                        osenatepos_rect.topleft = OVERALL_SENATE_POS_COORDS
                        # yearly/overall house avgpos
                        house_avgpos_y = 0
                        for i in reps:
                            congress_avgpos_y += i.pos
                            house_avgpos_y += i.pos
                            congress_avgpos_o += i.pos
                            house_avgpos_o += i.pos
                        house_avgpos_y = int(house_avgpos_y / 435)
                        temp = int(house_avgpos_o / (435 * year))
                        yhousepos_obj = font.render(str(house_avgpos_y), False, (255,255,255))
                        yhousepos_rect = yhousepos_obj.get_rect()
                        yhousepos_rect.topleft = YEARLY_HOUSE_POS_COORDS
                        ohousepos_obj = font.render(str(temp), False, (255,255,255))
                        ohousepos_rect = ohousepos_obj.get_rect()
                        ohousepos_rect.topleft = OVERALL_HOUSE_POS_COORDS
                        congress_avgpos_y = int(congress_avgpos_y / 535)
                        temp = int(congress_avgpos_o / (535 * year))
                        ycongresspos_obj = font.render(str(congress_avgpos_y), False, (255,255,255))
                        ycongresspos_rect = ycongresspos_obj.get_rect()
                        ycongresspos_rect.topleft = YEARLY_CONGRESS_POS_COORDS
                        ocongresspos_obj = font.render(str(congress_avgpos_o), False, (255,255,255))
                        ocongresspos_rect = ocongresspos_obj.get_rect()
                        ocongresspos_rect.topleft = OVERALL_CONGRESS_POS_COORDS
                        # yearly/overall conciduorum avgpos
                        conciduorum_avgpos_y = 0
                        # yearly/overall contrum senatum avgpos
                        contrumsenatum_avgpos_y = contrum_senatum.pos
                        conciduorum_avgpos_y += contrum_senatum.pos
                        conciduorum_avgpos_o += contrum_senatum.pos
                        contrumsenatum_avgpos_o += contrum_senatum.pos
                        ycontrumsenatum_obj = font.render(str(contrumsenatum_avgpos_y), False, (255,255,255))
                        ycontrumsenatum_rect = ycontrumsenatum_obj.get_rect()
                        ycontrumsenatum_rect.topleft = YEARLY_CS_POS_COORDS
                        ocontrumsenatum_obj = font.render(str(contrumsenatum_avgpos_o), False, (255,255,255))
                        ocontrumsenatum_rect = ocontrumsenatum_obj.get_rect()
                        ocontrumsenatum_rect.topleft = OVERALL_CS_POS_COORDS
                        # yearly/overall contra domus avgpos
                        contradomus_avgpos_y = contra_domus.pos
                        conciduorum_avgpos_y += contra_domus.pos
                        conciduorum_avgpos_o += contra_domus.pos
                        contradomus_avgpos_o += contra_domus.pos
                        ycontradomus_obj = font.render(str(contradomus_avgpos_y), False, (255,255,255))
                        ycontradomus_rect = ycontradomus_obj.get_rect()
                        ycontradomus_rect.topleft = YEARLY_CD_POS_COORDS
                        ocontradomus_obj = font.render(str(contradomus_avgpos_o), False, (255,255,255))
                        ocontradomus_rect = ocontradomus_obj.get_rect()
                        ocontradomus_rect.topleft = YEARLY_CD_POS_COORDS
                        conciduorum_avgpos_y = int(conciduorum_avgpos_y / 2)
                        temp = int(conciduorum_avgpos_o / (2 * year))
                        yconciduorum_obj = font.render(str(conciduorum_avgpos_y), False, (255,255,255))
                        yconciduorum_rect = yconciduorum_obj.get_rect()
                        yconciduorum_rect.topleft = YEARLY_CONCID_POS_COORDS
                        oconciduorum_obj = font.render(str(temp), False, (255,255,255))
                        oconciduorum_rect = oconciduorum_obj.get_rect()
                        oconciduorum_rect.topleft = OVERALL_CONCID_POS_COORDS
                        # if not year 1:
                        if year > 1:
                            # what % of voters voted with their parent yearly/overall
                            with_parent_y = 0
                            # what % of voters voted against their parent yearly/overall
                            against_parent_y = 0
                            for i in voters:
                                if i.parent == "w": with_parent_y += 1
                                else: against_parent_y += 1
                            with_parent_o += with_parent_y
                            against_parent_o += against_parent_y
                            with_parent_y = int(with_parent_y / len(voters))
                            temp = int(with_parent_o / (len(voters) * year))
                            ywithparent_obj = font.render(str(with_parent_y), False, (255,255,255))
                            ywithparent_rect = ywithparent_obj.get_rect()
                            ywithparent_rect.topleft = YEARLY_WITH_PARENT_COORDS
                            owithparent_obj = font.render(str(temp), False, (255,255,255))
                            owithparent_rect = owithparent_obj.get_rect()
                            owithparent_rect.topleft = OVERALL_WITH_PARENT_COORDS
                            against_parent_y = int(against_parent_y / len(voters))
                            temp = int(against_parent_o / (len(voters) * year))
                            
                        # how many laws went through yearly/overall
                        # how many laws passed yearly/overall
                        # how many laws failed yearly/overall
                        # how many laws were in the LL corner yearly/overall
                        # how many laws were in the LR corner yearly/overall
                        # how many laws were in the AL corner yearly/overall
                        # how many laws were in the AR corner yearly/overall
                        # how centrist (%) were the laws yearly/overall
                    


    pygame.display.update()
    fps_clock.tick(30)
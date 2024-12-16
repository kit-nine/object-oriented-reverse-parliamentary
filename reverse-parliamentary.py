import random
# variables and constants
PER_STATE = 10
AVERAGE_BIRTH_AGE = 27
AVERAGE_CHILDREN_PER_MOTHER = 1
MEDIA_SKEW = (0,0)
gen_n_list = []
# create grid
def create_grid():
    grid = [[i for i in range(21)] for i in range(21)]
    for i,j in enumerate(range(-10,11)):
        for k,l in enumerate(range(-10,11)): grid[i][k] = (j,l)
# create person class
class Person():
    def __init__(self, pos):
        self.age = 0
        for i in range(len(pos)):
            if pos[i] > 10: self.pos[i] = 10
            elif pos[i] < -10: self.pos[i] = -10
            else: self.pos = pos
        self.children = []
    def can_vote(self):
        if self.age >= 18: self.votes = True
        else: self.votes = False
    def vote(self):
        pass
    def reproduce(self):
        if self.age >= AVERAGE_BIRTH_AGE:
            for i in range(AVERAGE_CHILDREN_PER_MOTHER): self.children.append(gen_n((self.pos[0]/abs(self.pos[0]),self.pos[1]/abs(self.pos[1]))))
        for i in self.children: gen_n_list.append(i) 
# create first generation
def gen_1():
    gen_1_list = []
    for _ in range(50*PER_STATE):
        temp = Person((random.randint(-10,10)+MEDIA_SKEW[0], random.randint(-10,10)+MEDIA_SKEW[1]))
        gen_1_list.append(temp)
    return gen_1_list
# create future generations
def gen_n(parent_skew):
    temp = Person((random.randint(-10,10)+MEDIA_SKEW[0]+parent_skew[0], random.randint(-10,10)+MEDIA_SKEW[1]+parent_skew[1]))
    return temp
# create timeskip function
def time(years):
    for i in range(years):
        for j in gen_1_list:
            j.age += 1
            j.can_vote()
            if j.votes:
                j.vote()
            j.reproduce()
# testing

import random

RACE_ALL = 0
RACE_WHITE = 1
RACE_BLACK = 2
RACE_API = 3
RACE_AIAN = 4
RACE_2RACE = 5
RACE_HISPANIC = 6

GENDER_ALL = 0
GENDER_MALE = 1
GENDER_FEMALE = 2

class Names:
    def __init__(self):
        self.names = []
        self.totals = []

    def load(self, filename):
        self.names = []
        self.totals = [0, 0, 0, 0, 0, 0, 0]
        with open(filename) as f:
            f.readline()
            for line in f:
                name = line.strip().split(',')
                entry = [name[0].capitalize(), int(name[1])] + [int(int(name[1]) * (float(prob)/100)) for prob in name[2:]]
                self.names.append(entry)

                for i in range(0, 7):
                    self.totals[i] += entry[i+1]
        print(self.totals)

    def random(self, race=RACE_ALL):
        roll = random.randint(0, int(self.totals[race]))
        sum = 0
        for name in self.names:
            sum += name[1+race]
            if sum > roll:
                return name[0]

firstnames = Names()
firstnames.load('firstnames.data')
malenames = Names()
malenames.load('malenames.data')
femalenames = Names()
femalenames.load('femalenames.data')
lastnames = Names()
lastnames.load('lastnames.data')

def random_name(race=RACE_ALL, gender=GENDER_ALL):
    if gender == GENDER_ALL:
        return firstnames.random(race), lastnames.random(race)
    elif gender == GENDER_MALE:
        return malenames.random(race), lastnames.random(race)
    elif gender == GENDER_FEMALE:
        return femalenames.random(race), lastnames.random(race)

def randeom_first_name(race=RACE_ALL, gender=GENDER_ALL):
    if gender == GENDER_ALL:
        return firstnames.random(race)
    elif gender == GENDER_MALE:
        return malenames.random(race)
    elif gender == GENDER_FEMALE:
        return femalenames.random(race)

def random_last_name(race=RACE_ALL):
    return lastnames.random(race)

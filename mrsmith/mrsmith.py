import random
import importlib.resources

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

first_names = None
male_names = None
female_names = None
last_names = None


class NameList:
    def __init__(self, filename=None):
        self.names = []
        self.totals = []
        if filename is not None:
            self.load(filename)

    def load(self, filename):
        self.names = []
        self.totals = [0, 0, 0, 0, 0, 0, 0]
        with importlib.resources.open_text('mrsmith', filename) as f:
            f.readline()
            for line in f:
                name = line.strip().split(',')
                entry = [name[0].capitalize(), int(name[1])] + [int(int(name[1]) * (float(prob)/100)) for prob in name[2:]]
                self.names.append(entry)
                for i in range(0, 7):
                    self.totals[i] += entry[i+1]

    def random(self, race=RACE_ALL):
        roll = random.randint(0, int(self.totals[race]))
        sum = 0
        for name in self.names:
            sum += name[1+race]
            if sum > roll:
                return name[0]

def load_names():
    global first_names
    global male_names
    global female_names
    global last_names
    first_names = NameList('firstnames.data')
    male_names = NameList('malenames.data')
    female_names = NameList('femalenames.data')
    last_names = NameList('lastnames.data')


def random_name(race=RACE_ALL, gender=GENDER_ALL):
    if first_names is None:
        load_names()
    if gender == GENDER_ALL:
        return first_names.random(race), last_names.random(race)
    elif gender == GENDER_MALE:
        return male_names.random(race), last_names.random(race)
    elif gender == GENDER_FEMALE:
        return female_names.random(race), last_names.random(race)


def first_name(race=RACE_ALL, gender=GENDER_ALL):
    if first_names is None:
        load_names()
    if gender == GENDER_ALL:
        return first_names.random(race)
    elif gender == GENDER_MALE:
        return male_names.random(race)
    elif gender == GENDER_FEMALE:
        return female_names.random(race)


def last_name(race=RACE_ALL):
    if first_names is None:
        load_names()
    return last_names.random(race)

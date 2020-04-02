from enum import Enum
from collections import defaultdict
import random
import importlib.resources


class Race(Enum):
    ALL = 0
    WHITE = 1
    BLACK = 2
    API = 3
    AIAN = 4
    TWORACE = 5
    HISPANIC = 6


class Gender(Enum):
    ALL = 0
    MALE = 1
    FEMALE = 2


class NameList:
    def __init__(self, filename=None):
        self.names = defaultdict(lambda: defaultdict(int))
        self.totals = defaultdict(int)
        if filename is not None:
            self.load(filename)

    @staticmethod
    def parse_line(line):
        split = line.strip().split(',')
        return split[0].capitalize(), int(split[1]), float(split[2]), float(split[3]), float(split[4]), float(split[5]), float(split[6]), float(split[7])

    def load(self, filename):
        self.names = defaultdict(lambda: defaultdict(int))
        self.totals = defaultdict(int)
        with importlib.resources.open_text('mrsmith', filename) as f:
            for line in f:
                name, total, per_white, per_black, per_api, per_aian, per_tworace, per_hispanic = NameList.parse_line(line)
                self.names[name][Race.ALL] = total
                self.names[name][Race.WHITE] = int(total * per_white/100)
                self.names[name][Race.BLACK] = int(total * per_black/100)
                self.names[name][Race.API] = int(total * per_api/100)
                self.names[name][Race.AIAN] = int(total * per_aian/100)
                self.names[name][Race.TWORACE] = int(total * per_tworace/100)
                self.names[name][Race.HISPANIC] = int(total * per_hispanic/100)
                for r in Race:
                    self.totals[r] += self.names[name][r]

    def random(self, race=Race.ALL):
        roll = random.randint(0, int(self.totals[race]))
        sum = 0
        for name in self.names.keys():
            sum += self.names[name][race]
            if sum > roll:
                return name


first_names = None
male_names = None
female_names = None
last_names = None


def load_names():
    global first_names
    global male_names
    global female_names
    global last_names
    first_names = NameList('firstnames.data')
    male_names = NameList('malenames.data')
    female_names = NameList('femalenames.data')
    last_names = NameList('lastnames.data')


def random_name(gender=Gender.ALL, race=Race.ALL):
    if first_names is None:
        load_names()
    if gender == Gender.ALL:
        return first_names.random(race), last_names.random(race)
    elif gender == Gender.MALE:
        return male_names.random(race), last_names.random(race)
    elif gender == Gender.FEMALE:
        return female_names.random(race), last_names.random(race)


def first_name(gender=Gender.ALL, race=Race.ALL):
    if first_names is None:
        load_names()
    if gender == Gender.ALL:
        return first_names.random(race)
    elif gender == Gender.MALE:
        return male_names.random(race)
    elif gender == Gender.FEMALE:
        return female_names.random(race)


def last_name(race=Race.ALL):
    if first_names is None:
        load_names()
    return last_names.random(race)

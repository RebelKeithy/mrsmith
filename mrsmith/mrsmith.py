from dataclasses import dataclass
from enum import Enum
from collections import defaultdict, namedtuple
from typing import Optional, List, Tuple, Dict
import random
import importlib.resources


class Race(str, Enum):
    ALL = "all"
    WHITE = "white"
    BLACK = "black"
    API = "api"
    AIAN = "aian"
    TWORACE = "tworace"
    HISPANIC = "hispanic"


class Gender(str, Enum):
    ALL = "all"
    MALE = "male"
    FEMALE = "female"


@dataclass
class Name:
    name: str
    gender: Gender
    total: int
    demographics: Dict[Race, int]


class NameList:
    def __init__(self, filename: Optional[str] = None, gender: Gender = Gender.ALL):
        self.names: List[Name] = []
        self.totals = defaultdict(int)
        if filename is not None:
            self.load(filename, gender)

    @staticmethod
    def parse_line(line: str) -> Tuple:
        split = line.strip().split(',')
        return split[0].capitalize(), int(split[1]), float(split[2]), float(split[3]), float(split[4]), float(split[5]), float(split[6]), float(split[7])

    def load(self, filename: str, gender: Gender):
        self.names: List[Name] = []
        self.totals = defaultdict(int)
        with importlib.resources.open_text('mrsmith', filename) as f:
            for line in f:
                name, total, per_white, per_black, per_api, per_aian, per_tworace, per_hispanic = NameList.parse_line(line)
                name_item = Name(
                    name=name,
                    gender=gender,
                    total=total,
                    demographics={
                        Race.ALL: total,
                        Race.WHITE: int(total * per_white/100),
                        Race.BLACK: int(total * per_black/100),
                        Race.API: int(total * per_api/100),
                        Race.AIAN: int(total * per_aian/100),
                        Race.TWORACE: int(total * per_tworace/100),
                        Race.HISPANIC: int(total * per_hispanic/100),
                    }
                )
                self.names.append(name_item)
                for r in Race:
                    self.totals[r] += name_item.demographics[r]

    def random(self, race: Race = Race.ALL) -> Name:
        roll = random.randint(0, int(self.totals[race]))
        roll_sum = 0
        for name in self.names:
            roll_sum += name.demographics[race]
            if roll_sum > roll:
                return name


first_names = None
male_names = None
female_names = None
last_names = None


def load_names():
    """
    This can take a few seconds to run. Call this if you want to pre-load the names, otherwise it will be called when
    you first try to generate a name.
    """
    global first_names
    global male_names
    global female_names
    global last_names
    first_names = NameList('firstnames.data')
    male_names = NameList('malenames.data', Gender.MALE)
    female_names = NameList('femalenames.data', Gender.FEMALE)
    last_names = NameList('lastnames.data')


def full_name(gender: Gender = Gender.ALL, race: Race = Race.ALL) -> Tuple[Name, Name]:
    if first_names is None:
        load_names()
    if gender == Gender.ALL:
        return first_names.random(race), last_names.random(race)
    elif gender == Gender.MALE:
        return male_names.random(race), last_names.random(race)
    elif gender == Gender.FEMALE:
        return female_names.random(race), last_names.random(race)


def first_name(gender: Gender = Gender.ALL, race: Race = Race.ALL) -> Name:
    if first_names is None:
        load_names()
    if gender == Gender.ALL:
        return first_names.random(race)
    elif gender == Gender.MALE:
        return male_names.random(race)
    elif gender == Gender.FEMALE:
        return female_names.random(race)


def last_name(race: Race = Race.ALL) -> Name:
    if first_names is None:
        load_names()
    return last_names.random(race)

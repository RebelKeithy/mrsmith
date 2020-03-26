import random
import constants
from namelist import NameList

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


def random_name(race=constants.RACE_ALL, gender=constants.GENDER_ALL):
    if first_names is None:
        load_names()
    if gender == constants.GENDER_ALL:
        return first_names.random(race), last_names.random(race)
    elif gender == constants.GENDER_MALE:
        return male_names.random(race), last_names.random(race)
    elif gender == constants.GENDER_FEMALE:
        return female_names.random(race), last_names.random(race)


def first_name(race=constants.RACE_ALL, gender=constants.GENDER_ALL):
    if first_names is None:
        load_names()
    if gender == constants.GENDER_ALL:
        return first_names.random(race)
    elif gender == constants.GENDER_MALE:
        return male_names.random(race)
    elif gender == constants.GENDER_FEMALE:
        return female_names.random(race)


def last_name(race=constants.RACE_ALL):
    if first_names is None:
        load_names()
    return last_names.random(race)

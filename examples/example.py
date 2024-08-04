import mrsmith
from mrsmith.mrsmith import Name


def print_full_name(first_name: Name, last_name: Name):
    print(f'{first_name.name} {last_name.name}')


print_full_name(*mrsmith.full_name())
print_full_name(*mrsmith.full_name(gender=mrsmith.Gender.MALE))
print_full_name(*mrsmith.full_name(race=mrsmith.Race.BLACK))
print_full_name(*mrsmith.full_name(gender=mrsmith.Gender.FEMALE, race=mrsmith.Race.AIAN))

print(mrsmith.first_name(gender=mrsmith.Gender.FEMALE).name)
print(mrsmith.first_name(race=mrsmith.Race.HISPANIC).name)
print(mrsmith.first_name(gender=mrsmith.Gender.FEMALE).name)
print(mrsmith.first_name(gender=mrsmith.Gender.MALE, race=mrsmith.Race.API).name)

print(mrsmith.last_name().name)
print(mrsmith.last_name(race=mrsmith.Race.TWORACE).name)

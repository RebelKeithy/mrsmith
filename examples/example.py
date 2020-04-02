import mrsmith

print(' '.join(mrsmith.random_name()))
print(' '.join(mrsmith.random_name(gender=mrsmith.Gender.MALE)))
print(' '.join(mrsmith.random_name(race=mrsmith.Race.BLACK)))
print(' '.join(mrsmith.random_name(gender=mrsmith.Gender.FEMALE, race=mrsmith.Race.AIAN)))

print(mrsmith.first_name(gender=mrsmith.Gender.FEMALE))
print(mrsmith.first_name(race=mrsmith.Race.HISPANIC))
print(mrsmith.first_name(gender=mrsmith.Gender.FEMALE))
print(mrsmith.first_name(gender=mrsmith.Gender.MALE, race=mrsmith.Race.API))

print(mrsmith.last_name())
print(mrsmith.last_name(race=mrsmith.Race.TWORACE))

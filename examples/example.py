import mrsmith

print(' '.join(mrsmith.random_name()))
print(' '.join(mrsmith.random_name(gender=mrsmith.GENDER_MALE)))
print(' '.join(mrsmith.random_name(race=mrsmith.RACE_BLACK)))
print(' '.join(mrsmith.random_name(gender=mrsmith.GENDER_FEMALE, race=mrsmith.RACE_AIAN)))

print(mrsmith.first_name(mrsmith.GENDER_FEMALE))
print(mrsmith.first_name(race=mrsmith.RACE_HISPANIC))
print(mrsmith.first_name(gender=mrsmith.GENDER_FEMALE))
print(mrsmith.first_name(gender=mrsmith.GENDER_MALE, race=mrsmith.RACE_API))

print(mrsmith.last_name())
print(mrsmith.last_name(race=mrsmith.RACE_2RACE))

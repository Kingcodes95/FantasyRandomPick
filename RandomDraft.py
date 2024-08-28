import random

UserRoster = ['Ronnie', 'Carmen', 'Eric', 'Amelia', 'Ethan', 'Erics Mom', 'Eddie', 'Danny']
RandomizedRoster = []
n = len(UserRoster)

for users in range(n):
    random_choice = random.choice(UserRoster)
    RandomizedRoster.append(random_choice)
    UserRoster.remove(random_choice)

print(", ".join(RandomizedRoster))

import random

UserRoster = ['Ronnie', 'Carmen', 'Eric', 'Amelia', 'Ethan', 'Erics Mom']
RandomizedRoster = []

for users in range(6):
    random_choice = random.choice(UserRoster)
    RandomizedRoster.append(random_choice)
    UserRoster.remove(random_choice)

print(", ".join(RandomizedRoster))

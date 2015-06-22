"""
Dan Hopkins
Pokemon classes
"""

import random

class Pokemon:
	def __init__(self, name, number, health, attack, speed, moves):
		self.name = name
		self.num = number
		self.hp = health
		self.atk = attack
		self.spd = speed
		self.move1 = moves[0]
		self.move2 = moves[1]
		self.move3 = moves[2]
		self.move4 = moves[3]

	def use(self, move): # as in pikachu.use(pikachu.move2)
		pass

class Trainer:
	def __init__(self, name, party, items, cash):
		self.name = name
		self.party = party
		self.items = items
		self.cash = cash

Bulbasaur = Pokemon('Bulbasaur', 1, 20, 5, 3, ['Tackle', 'OATK Down', 'ATK Up', 'Leaf Whip'])
Charmander = Pokemon('Charmander', 2, 19, 6, 4, ['Scratch', 'OATK Down', 'ATK Up', 'Ember'])
Squirtle = Pokemon('Squirtle', 3, 21, 4, 5, ['Tackle', 'OATK Down', 'ATK Up', 'Water Gun'])

print "Hello, I'm Professor Oak. Let's have a Pokemon battle between the two of you!"
p1 = raw_input("Player 1, I know you're my grandson, but I've forgotten your name. What is it again? ")
print "Okay, good to see you again, uh..." + p1 + "."
p2 = raw_input("Player 2, I know you're my neighbor, but I've forgotten your name. What is it again? ")
print "Alright, " + str(p1) + " and " + str(p2) + ". Got it. Choose your Pokemon!"

# use random to assign new Pokemon.number for each Pokemon

p1choice = raw_input(str(p1) + ", to make this fair, pick a number between 1 and 3: ")
p1choice = int(p1choice)
print "Okay " + str(p1) + ", your Pokemon for this battle is " # + str(pokemon) + "!"

# randomize second player's pokemon too
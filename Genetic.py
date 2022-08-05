"""
x ----------------------------------- problem to solve : reach the [0,0,0,0] ------------------------------------------ x
"""
from numpy import random
from random import choice
import random as rnd
class indv(object):
	def __init__(self,gen):
		self.gen = gen
		self.fitscore = self.fit_score()
	def fit_score(self):
		fit = [0,0,0,0g]
		fitscore = 0
		for i,j in zip(self.gen,fit):
			if i != j:
				fitscore += 1
		return fitscore
	@classmethod
	def gen_create(self):
		return [random.randint(0,999),random.randint(0,999),random.randint(0,999),random.randint(0,999)]
def mate(parentos,parentes):
	offspring_gen = []
	for padre,madre in zip(parentos,parentes):
		c = choice([0,1,2])
		if c == 0:
			offspring_gen.append(padre)
		elif c == 1:
			offspring_gen.append(madre)
		else:
			offspring_gen.append(random.randint(0,999))
	offspring = indv(offspring_gen)
	return offspring
def main():
	population_size = 100
	population = []
	for i in range(population_size):
		gene = indv.gen_create()
		population.append(indv(gene))
	while True:
		population = sorted(population,key=lambda y:y.fitscore)
		if population[0].fitscore <= 0:
			print("Solved!")
			print(f"Target = [0,0,0,0], Current = {population[0].gen} ")
			break
		new_pops = []
		new_pops.extend(population[:int((population_size*10)/100)])
		for i in range(int((population_size*90)/100)):
			offspring = mate(choice(population[:50]).gen,choice(population[:50]).gen)
			new_pops.append(offspring)
			#print(offspring.gen)
		population = new_pops
		print(new_pops[0].gen)
		print(f"Target = [0,0,0,0], Current = {population[0].gen} ")
if __name__ == "__main__":
	main()
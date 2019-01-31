from Gene import Gene
from Equation import Equation
import random

def RouletteWheel(nums):
    listSum = sum(nums)
    rand = random.randint(0,listSum)
    inc = 0
    for i in range(0,nums.__len__()):
        inc += nums[i]
        if inc >= rand:
            chosen = i
            break
    return chosen

class GeneticAlgorithm():
    def __init__(self, mutChance):
        self.population = []
        self.mutateChance = mutChance

    '''Generates a population of genes that have random values. Takes in the length of the population, length of genes,
    and the equation string'''
    def generatePop(self, popLen, geneLen, eqString):
        length = geneLen
        for i in range(0, popLen):
            geneValues = []
            for x in range(0,length):
                geneValues.append(random.randint(0,1))
            self.population.append(Gene(geneValues, eqString))
    
    '''Calls determine fitness on each gene in the population.'''
    def determinePopFitness(self):
        for gene in self.population:
            gene.determineFitness()
    


doc = open("text.txt",'r')
eq = Equation(doc.read())
ga = GeneticAlgorithm(25)
ga.generatePop(4, eq.LiteralDictionary.__len__(), eq.string)
answer = None
numGens = 0
mutChance = 25
pivot = 5
while(True):
    '''Determine the fitness of each member of the population'''
    ga.determinePopFitness()
    fitnessList = []
    '''Goes through each gene and checks their fitness. If their fitness is equal to the number of 
    caluses then they are a perfect gene and are set as the answer to the equation otherwise the loop continues'''
    for gene in ga.population:
        if gene.fitness == eq.ClauseArray.__len__():
            answer = gene
        fitnessList.append(gene.fitness)
    if answer is not None:
        break
    '''Gets 2 random numbers using the roulette wheel selection type. The numbers are used for indexes in the population to select the parents.
    The second number keep getting new numbers until it is no longer the same as the first number to avoid problems with the same index being
    modified twice.'''
    roulette = RouletteWheel(fitnessList)
    parentA = ga.population[roulette]
    roulette2 = RouletteWheel(fitnessList)
    while(roulette == roulette2):
        roulette2 = RouletteWheel(fitnessList)
    parentB = ga.population[roulette2]
    '''Loops through each value in the genes values and changes the value to the opposite numbers based on a random chance'''
    parentA.mutate(mutChance)
    parentB.mutate(mutChance)
    '''Splits the genes apart at the index of the number passed in. The left part of the first gene and the right part of the second gene
    are combined to make the kid which is returned by the function.'''
    kidA = parentA.crossover(parentB,pivot)
    kidB = parentB.crossover(parentA,pivot)
    '''Removes the parents from the population and then adds the kids in their place.'''
    ga.population.remove(parentA)
    ga.population.remove(parentB)
    ga.population.append(kidA)
    ga.population.append(kidB)
    numGens+=1
print(str(answer.values))
print("Answer found after " + str(numGens) + " generations")

'''feedback 1:
-replace all constants with variables 
-comments explaining the flow, a simple return description would suffice
-'''
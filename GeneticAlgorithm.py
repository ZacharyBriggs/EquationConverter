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
    def __init__(self):
        self.population = []

    def generatePop(self, popLen, geneLen, eqString):
        length = geneLen
        for i in range(0, popLen):
            geneValues = []
            for x in range(0,length):
                geneValues.append(random.randint(0,1))
            self.population.append(Gene(geneValues, eqString))
    
    def determinePopFitness(self):
        for gene in self.population:
            gene.determineFitness()
    


doc = open("text.txt",'r')
eq = Equation(doc.read())
ga = GeneticAlgorithm()
ga.generatePop(4, eq.LiteralDictionary.__len__(), eq.string)
ga.determinePopFitness()
while(True):
    answer = None
    fitnessList = []
    for gene in ga.population:
        if gene.fitness == eq.ClauseArray.__len__():
            answer = gene
        fitnessList.append(gene.fitness)
    if answer is not None:
        break
    parentA = ga.population[RouletteWheel(fitnessList)]
    parentB = ga.population[RouletteWheel(fitnessList)]
    parentA.mutate(25)
    parentB.mutate(25)
    kidA = parentA.crossover(parentB,5)
    kidB = parentB.crossover(parentA,5)
    ga.population.remove(parentA)
    ga.population.remove(parentB)
    ga.population.append(kidA)
    ga.population.append(kidB)

print(str(answer.values))
a=1
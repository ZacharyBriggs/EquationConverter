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
            chosen = nums[i]
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
ga.generatePop(6, eq.LiteralDictionary.__len__(), eq.string)
ga.determinePopFitness()
fitnessList = []
for gene in ga.population:
    fitnessList.append(gene.fitness)
h = RouletteWheel(fitnessList)
a=1
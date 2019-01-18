import random
from Equation import Equation
from Converter import Converter
class Gene():
    def __init__(self, values, eqString):
        self.values = values
        self.eq = Equation(eqString)
        self.eq.setLiterals(values)
        self.eq.convert()
        self.fitness = 0

    def mutate(self, chance):
        inc = 0
        for number in self.values:
            rand = random.randint(0,100)
            if chance > rand:
                self.values[inc] = 0 if number != 0 else 1
            inc += 1

    def crossover(self, other, pivot):
        i = 0
        newGene = []
        for item in self.values:
            newGene.append(item)
            i+=1
            if i == pivot:
                break
        for x in range(pivot, other.values.__len__()):
            newGene.append(other.values[x])
        return newGene

    def determineFitness(self):
        self.fitness = self.eq.solve()
        return self.fitness

'''doc = open("text.txt",'r')
eq = Equation(doc.read())
eq.findClauses()
eq.findUniques()
numbers = [1,0,1,1,1,0]
numbers2 = [0,1,0,1,0,1]
literals = []
gene = Gene(numbers, eq)
gene.determineFitness()
gene2 = Gene(numbers2, eq)
gene2.determineFitness()
gene.mutate(25)
crossGene = gene.crossover(gene2,2)
a=1'''
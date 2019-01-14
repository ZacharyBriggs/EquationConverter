import random
class Gene():
    def __init__(self, values):
        self.values = values
        self.fitness = 0

    def mutate(self, chance):
        inc = 0
        for number in self.values:
            rand = random.randint(0,101)
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

numbers = [1,0,1,1]
numbers2 = [0,1,0,1]
gene = Gene(numbers)
gene2 = Gene(numbers2)
gene.mutate(25)
corssGene = gene.crossover(gene2,2)
a=1
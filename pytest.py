class Clause():
    def __init__(self):
        self.array = []
    def Append(self,info):
        self.array.append(info)

class Equation():
    def __init__(self):
        self.LiteralDictionary = []
        self.ClauseArray = []
    def AddLiteral(self, tup):
        self.LiteralDictionary.append(tup)
    def AddCaluse(self):
        self.ClauseArray.append(Clause())

doc = open("text.txt",'r')
docList = list(doc.read())
uniqueLiterals = []
for item in docList:
    for i in range(97,123):
        if item is chr(i):
            uniqueLiterals.append(item)

for currentLiteral in uniqueLiterals:
    num = 0
    for literal in uniqueLiterals:
        if currentLiteral == literal:
            num+=1
    for i in range(0,num-1):
        uniqueLiterals.remove(currentLiteral)

eq = Equation()
for i in range(97, 97 + uniqueLiterals.__len__()-1):
    value = input("Enter the value of" + " " + chr(i) + " ")
    eq.AddLiteral([chr(i), value])

docLength = docList.__len__()
inc = -1
for x in docList:
    inc += 1
    if x == "(":
        '''begin clause'''
        eq.AddCaluse()
        for y in range(inc,docLength):
            eq.ClauseArray[eq.ClauseArray.__len__()-1].Append(docList[y])
            if(y == ")"):
                '''end caluse'''
                break
inc2 = -1
for letter in docList:
    inc2 += 1
    for literal in eq.LiteralDictionary:
        if letter is literal[0]:
            docList[inc2] = str(literal[1])
newEq = ''.join(docList)
print(newEq)
'''Stuff to do:
    1. Allow the user to input the values of the literals
    2. Seperate classes into their own files and import them into a main
    3. Find out if there's a way to do a proper incrementing for loop
    4. '''
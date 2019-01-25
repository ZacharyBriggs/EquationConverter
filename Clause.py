class Clause():
    def __init__(self, clause):
        self.value = clause
        self.numLiterals = 0
        self.converted = []

    def append(self,info):
        self.value.append(info)

    def convert(self,literals):
        inc2 = -1
        for letter in self.value:
            inc2 += 1
            for literal in literals:
                if letter is literal[0]:
                    self.value[inc2] = str(literal[1])
                    self.numLiterals += 1
                    if(self.value[inc2-1] == "!"):
                        self.value[inc2-1] = ""
                        self.value[inc2] = "0" if self.value[inc2] != "0" else "1"
                        
        self.converted = ''.join(self.value)

    def solve(self):
        numT = 0
        hasAnd = False
        for num in self.converted:
            if num == "1":
                numT += 1
            if num == "*":
                hasAnd = True
        if(numT > 0 and hasAnd == False):
            return True
        elif(numT == self.numLiterals and hasAnd == True):
            return True
        else:
            return False
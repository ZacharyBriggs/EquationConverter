class Clause():
    def __init__(self, clause):
        self.value = clause
        self.numLiterals = 0
        self.converted = []

    def append(self,info):
        self.value.append(info)
    '''Converts all the the characters in the clause into values based on the literals passed in'''
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

    '''Checks the converted clause string for any ones. If any ones are found in the string then it return true else it will return false.'''
    def solve(self):
        numT = 0
        for num in self.converted:
            if num == "1":
                numT += 1
        if(numT > 0):
            return True
        else:
            return False
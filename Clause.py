class Clause():
    def __init__(self, clause):
        self.value = clause
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
                    if(self.value[inc2-1] == "!"):
                        self.value[inc2-1] = ""
                        self.value[inc2] = "0" if self.value[inc2] != "0" else "1"
                        
        self.converted = ''.join(self.value)

    def solve(self):
        numT = 0
        for num in self.converted:
            if num == "1":
                numT += 1
        if(numT > 0):
            return True
        else:
            return False

'''literals = []
literal1 = ["a",0]
literal2 = ["c",1]
literals.append(literal1)
literals.append(literal2)
string = "(!a+c)"
clu = Clause(list(string))
clu.convert(literals)
boolean = clu.solve()
a=1'''
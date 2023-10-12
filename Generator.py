class FamilyIter:
    def __init__(self):
        self.members=[]
        self.currentPos =0

    def addMember(self, name):
        self.members.append(name)
    
    def __iter__(self):
        return self.members.__iter__()

    def __next__(self):
        if self.currentPos > len(self.members):
            raise StopIteration
        self.currentPos += 1
        return self.members[self.currentPos]
        
fit = FamilyIter()
fit.addMember("test")
fit.addMember("test1")

for x in fit:
    print(x)

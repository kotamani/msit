
class Number:

    def __init__(self,number):
        self.number = str(number)
        self.digit = [int(item) for item in list(self.number)]
        print(self.digit)

    def __str__(self):
        print("{}".format(self.number))

    def isUnique(self):
        if len(self.digit) == len(set(self.digit)):
            return True
        return False

    def isConsequitive(self):
        if self.isUnique():
            if min(self.digit) == 1 and max(self.digit) == len(self.digit):
                return True
        return False

    def makeMatrix(self):
        #if self.isConsequitive():
        row = [[0 for item in range(len(self.digit))] for item in self.digit]
        print(row)
        for row,index in zip(row,self.digit):
            print(row,index)
            row[index-1] = 1
            #print(row)
            
    


n = Number(2342)
#print(n.isUnique())
#print(n.isConsequitive())
#n.makeMatrix()

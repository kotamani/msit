class Number:
    def __init__(self,number):
        self.number = number
        self.result = {}
        for number in str(self.number):
            if number in self.result:
                self.result[number] += 1
            else:
                self.result[number] = 1

    def isUnique(self):
        maximun = max(self.result.values())
        if maximun != 1:
            return False
        else:
            return True
            
    def isConsequitive(self):
        result = []
        num = 1
        for number in str(self.number):
            result.append(int(number))
            result.sort()
        minimum = int(min(result))
        maximun = int(max(result))+1
        range_list = list(range(minimum,maximun))
        if num in result:
            if result == range_list:
                return True
            else:
                return False    
        else:
            return False
    
    def makeMatrix(self):
        
        matrix = []
        maximum = int(max(str(self.number)))
        for number in str(self.number):
            val = [0]*(maximum-1)
            val.insert(int(number)-1, 1)
            matrix.append(val)
        return matrix   
        

    def show(self):
        print(self.number)

n = Number(input("enter number:"))
n.show()
print("isUnique",n.isUnique())
print("isConsequitive",n.isConsequitive())
print("makeMatrix",n.makeMatrix())


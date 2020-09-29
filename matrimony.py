
class Matrimony:

    def __init__(self):
        self.males = {}
        self.females = {}
        fobj=open("records.txt","r")
        for line in fobj:
            fields = line.split()
            name = fields[0]
            gender = fields[1]
            age = int(fields[2])
            salary = int(fields[3])

            if gender == "m":
                self.males[name] = {"gender":gender,"age":age,"salary":salary}
            

            else:
                self.females[name]={"gender":gender,"age":age,"salary":salary}
            

    def show(self):
        for name in self.males:
            print(name+" ",end="")
            prin
        print()

        for name in self.females:
            print(name+" ",end="")
            print(self.females[name]["age"],end=" ")
            print(self.females[salary])


    def distance(self,male,female):
        age_m=self.males[male]["age"]
        sal_m=self.males[male]["norm"]

        age_j=self.females[female]["age"]
        sal_j=self.females[female]["norm"]
       

        from math import sqrt

        return sqrt ( (age_m - age_j)**2 + (sal_m - sal_j)**2 )

    def recommendFemale(self,male):
        distances=[]

        for female in self.females:
            distance=self.distance(male,female)
            distances.append((distance,female))
        distances.sort()
        return distances[0][-1]

    def norm(self):
        salaries = []
        for name in self.males:
            salary = self.males[name]["salary"]
            salaries.append(salary)

        for name in self.females:
            salary = self.females[name]["salary"]
            salaries.append(salary)

        min_salary = min(salaries)
        max_salary = max(salaries)
        sal_range = max_salary - min_salary

        for name in self.males:
            salary = self.males[name]["salary"]
            norm_salary = (salary -  min_salary)/sal_range
            self.males[name]["norm"]=norm_salary

        for name in self.females:
            salary = self.females[name]["salary"]
            norm_salary = (salary -  min_salary)/sal_range
            self.females[name]["norm"]=norm_salary

       
m1 = Matrimony()
#print(m1.distance("murali","jane"))
m1.norm()
print(m1.recommendFemale("murali"))


print('welcome')
class Vendor:

    def __init__(self,number):
        self.number = str(number)
        self.sim = {'1':"BSNL",'2':"IDEA",'3':"JIO",'4':"AIRTEL"}
        #print(self.sim)
        for key,value in self.sim.items():
            if self.number in key:
                print("Thank you for selecting ",value)
        

    def Plan(self):
        #self.sim[self.number] = {"Calls":[],"Data":[],"sms":[]}

        if self.sim["1"]:
                bsnl = {"1":"Calls","2":"Data","3":"sms"}
                print('\n')
                print("1.Call package 2.Data package 3.sms package")
                number = str(input('enter no '))
                for key,value in bsnl.items():
                    if number in key:
                        print("====",value,"=====")
                    if number == '1':
                        print(">Month >six_Months >Yearly : ")
                        package=input("enter you package : ")
                        pakage=["Month","six_Months","Yearly"]
                        if package == pakage[0]:
                            print("Your bal Plan Is Activated for month 150")
                        elif package == pakage[1]:
                            print("Your bal Plan Is Activated for six-month 900")
                        elif package == pakage[2]:
                            print("Your bal Plan Is Activated for one-year 1990")
                        
                        break
    
                    elif number == '2':
                        print(">Month >six_Months >Yearly : ")
                        package=input("enter you package : ")
                        pakage=["Month","six_Months","Yearly"]
                        if package == pakage[0]:
                            print("Your data Plan Is Activated for month 250")
                        elif package == pakage[1]:
                            print("Your bal Plan Is Activated for six-month 1000")
                        elif package == pakage[2]:
                            print("Your bal Plan Is Activated for one-year 2990")
                        break
                    
                    elif number == '3':
                        print(">Month >six_Months >Yearly : ")
                        package=input("enter you package : ")
                        pakage=["Month","six_Months","Yearly"]
                        if package == pakage[0]:
                            print("Your sms Plan Is Activated for month 50")
                        elif package == pakage[1]:
                            print("Your sms Plan Is Activated for six-month 150")
                        elif package == pakage[2]:
                            print("Your sms Plan Is Activated for one-year 290")
                        break
                    break

        elif self.sim["2"]=="2":
                idea = {"1":"Calls","2":"Data","3":"sms"}
                print('\n')
                print("1.Call package 2.Data package 3.sms package")
                number = str(input('enter no '))
                for key,value in idea.items():
                    if number in key:
                        print("====",value,"=====")
                    if number == '1':
                        print(">Month >six_Months >Yearly : ")
                        package=input("enter you package : ")
                        pakage=["Month","six_Months","Yearly"]
                        if package == pakage[0]:
                            print("Your bal Plan Is Activated for month 250")
                        elif package == pakage[1]:
                            print("Your bal Plan Is Activated for six-month 1000")
                        elif package == pakage[2]:
                            print("Your bal Plan Is Activated for one-year 1999")
                        
                        break
    
                    elif number == '2':
                        print(">Month >six_Months >Yearly : ")
                        package=input("enter you package : ")
                        pakage=["Month","six_Months","Yearly"]
                        if package == pakage[0]:
                            print("Your data Plan Is Activated for month 260")
                        elif package == pakage[1]:
                            print("Your bal Plan Is Activated for six-month 1100")
                        elif package == pakage[2]:
                            print("Your bal Plan Is Activated for one-year 2890")
                        break
                    
                    elif number == '3':
                        print(">Month >six_Months >Yearly : ")
                        package=input("enter you package : ")
                        pakage=["Month","six_Months","Yearly"]
                        if package == pakage[0]:
                            print("Your sms Plan Is Activated for month 60")
                        elif package == pakage[1]:
                            print("Your sms Plan Is Activated for six-month 160")
                        elif package == pakage[2]:
                            print("Your sms Plan Is Activated for one-year 280")
                        break
                    break
        

        

        elif self.sim["3"]:
    
                jio = {"1":"Calls","2":"Data","3":"sms"}
                print('\n')
                print("1.Call package 2.Data package 3.sms package")
                number = str(input('enter no '))
                for key,value in jio.items():
                    if number in key:
                        print("====",value,"=====")
                    if number == '1':
                        print(">Month >six_Months >Yearly ")
                        package=input("enter you package : ")
                        pakage={"Month":198,"six_Months":699,"Yearly":2399}
                        if pakage[package]:
                            print("Your Plan Is Activated for month",pakage["Month"])
                        elif  pakage[package]:
                            print("Your Plan Is Activated for month",pakage["six_Months"])
                        elif pakage[package]:
                            print("Your Plan Is Activated for month",pakage["Yearly"])
                        else:
                            print("Try Next Time")
                    break

        elif self.sim['4']:

                airtel = {"1":"Calls","2":"Data","3":"sms"}
                print('\n')
                print("1.Call package 2.Data package 3.sms package")
                number = str(input('enter no '))
                for key,value in airtel.items():
                    if number in key:
                        print("====",value,"=====")
                        if number == '1':
                            print(">Month >six_Months >Yearly ")
                            package=input("enter you package : ")
                            pakage={"Month":200,"six_Months":799,"Yearly":2599}
                            if pakage[package]:
                                print("Your Plan Is Activated for month",pakage["Month"])
                            elif  pakage[package]:
                                print("Your Plan Is Activated for month",pakage["six_Months"])
                            elif pakage[package]:
                                print("Your Plan Is Activated for month",pakage["Yearly"])
                            else:
                                print("Try Next Time")
                    break
                
    

print("1.BSNL 2.IDEA 3.JIO 4.Airtel")
v = Vendor(input('Choose no : '))
v.Plan()

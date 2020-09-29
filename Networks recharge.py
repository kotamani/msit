class Networks:
    def __init__(self):
        self.networks={1:"AIRTEL",2:"VODAFONE",3:"JIO",4:"IDEA"}
        
    def vendor(self):
        for network in self.networks:
            print(network, self.networks[network])

        +self.choosenvalue=int(input("choose your vendor: "))
        print("Thank you for choosing",self.networks[self.choosenvalue])
        

    def plans(self):
        self.sms=int(input("enter your sms requiement: "))
        self.data=int(input("enter your data requirement: "))
        self.calls=int(input("enter your call requirement: "))
        
        self.cost1=self.sms*1+self.data*2+self.calls*1
        self.cost2=self.sms*1+self.data*1+self.calls*1
        self.cost3=self.sms*2+self.data*1+self.calls*2
        self.cost4=self.sms*1+self.data*2+self.calls*1
        
        if self.choosenvalue==1:
            print("cost value per month: ",self.cost1)
        if self.choosenvalue==2:
            
            print("cost value per month: ",self.cost2)
        if self.choosenvalue==3:
            
            print("cost value per month: ",self.cost3)
        if self.choosenvalue==4:
            
            print("cost value per month: ",self.cost4)

    def compare(self):
        costs=[]
        costs.append((self.cost1,self.networks[1]))
        costs.append((self.cost2,self.networks[2]))
        costs.append((self.cost3,self.networks[3]))
        costs.append((self.cost4,self.networks[4]))
        print("1:Okay,2:Not okay,3: Compare")
        choice=int(input("enter your choice:"))
        if choice==1:
            print("Thank you for choosing our plan")
            self.vendor()
            
        if choice==2:
            print("1. change data plan, 2. change vendor")
            option=int(input("enter your choice: "))
            if option==1:
                self.plans()
            if option==2:
                self.vendor()
                
        if choice==3:
            for cost in costs:
                print(cost[1],cost[0])
            costs.sort()
            print("Best network is: ",costs[0][1])    


n=Networks()
n.vendor()
n.plans()
n.compare()

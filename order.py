class Foodorder_system :
    def __init__(self) :
        self.foodorder={1.:"Pizza=10000MMK",
                        2.:"Burger=7000MMK",
                        3.:"Juice=5000MMK"}
        self.price={1:10000,
                    2:7000,
                    3:5000}
        self.queue=[]
        self.total=0
        
        
        
    def item(self,choice,qty) :
        self.queue.append(self.foodorder[choice])
        self.total+=self.price[choice]*qty
        print("Choiced Order item: ",self.queue)
        print("Total Bill : ",self.total)
        
        
    def serving(self) :
        print("Food Order Serveing Part!")
        if self.queue :
            while self.queue :
                serve_order=self.queue.pop(0)
                print("Served Food Order : ",serve_order)
                print("Remain Food Order : ",self.queue)
        else :
            print("No Food Order to serve!")
            
            
            
            
    def order(self) :
        print(self.foodorder)
        while True :
            n=int(input("Choose Food order item(1 or 2 or 3 or 0 to exit) : "))
            if n==0 :
                break
            elif n not in self.foodorder:
                print("Invalid choose!")
                continue
            
            m=int(input("Enter item quantities :"))
            self.item(n,m)
            a=input("Do you want to another items(y/n) :")
            if a=="n" :
                
                break
            
        self.serving()
        print("Finally Total Bill :",self.total)
        
        
def main():
        Order_system=Foodorder_system()
        Order_system.order()
main()    
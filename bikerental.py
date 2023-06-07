class Bikeshop:
    def __init__(self,stock):
        self.stock = stock
    
    def display(self):
        print("Total Bike ", self.stock)
    def rentforbike(self, q):
        if q<=0:
            print("enter the positive value")
        elif q>self.stock:
            print("Enter the value less than stock")
            
        else:
            self.stock-=q;
            print("Total prices:",q*100)
            print("Total Bikes" ,self.stock)
          

while True:
    obj=Bikeshop(100)
    uc=int(input('''
1.Display Stocks
2.Rent a Bike
3.Exit
            '''))
    if uc==1:
        obj.display()
    elif uc==2:
        obj.rentforbike(int(input("Enter the NO. of Bikes")))
    else:
        break

           
            

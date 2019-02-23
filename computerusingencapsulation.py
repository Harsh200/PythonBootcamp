class computer:
 def __init__(self):
     self._maxprice=1000

     def sell(self):
         print("selling price",format(self._maxprice))
     def setmaxprice(self,price):
         self._maxprice=price


c=computer()
c.sell()

c.__maxprice=1100
c.sell()
c.setmaxprice(1200)
c.sell()


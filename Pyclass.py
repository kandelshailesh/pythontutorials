
 class Cat:
     def __init__(self,name,age):
         self.name=name
         self.age=age
    
     def __str__(self):
          return "Name of cat is %s"%self.name
    
    
     def __repr__(self):
         return "name of cat is %s"%self.name[0]
    
     def __len__(self):
         return len(self.name)
    
    

 c=Cat(["Jocky","Pop","Sagar"],"21")

 print(c) #calls __str__(self)
 
 print([c]) #calls __str__(self)

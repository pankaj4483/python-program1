#number cube
cube = lambda x : x**3
print (cube(4))

#%10
numbers=[5,10,15,20,25,30]
result=list(filter(lambda x: x > 10,numbers))
print(result)

#list double
numbers=[5,10,15,20,25,30]
result=list(map(lambda x: x * 2 ,numbers))
print(result)

products=[("pen",50),("pencil",10),("book",200),("bag",800)]
result=sorted(products,key=lambda x: x[1])
print(result)


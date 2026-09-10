add= lambda a, b: a+b
print(add(3,5))

#lambda with sorted () function
students=[("pankaj,90",("rahul",58),("aman",50))]
sorted_students= sorted(students, key=lambda x: x[1])
print(sorted_students)

#lambda with filter()
numbers=[1,2,3,4,5,6,7,8,9,10]
even_number= list(filter(lambda x: x%2==0, numbers))
print(even_number)

#lamda with map() functipn
numbers=[1,2,3,4]
squared= list(map(lambda x: x*x, numbers))
print(squared)

































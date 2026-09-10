numbers=[1,2,3,4,5,6,7,8,9,10]
cubes=[num**3 for num in numbers]
print(cubes)

print()

numbers=[10,15,20,25,30,35,40]
result=[num for num in numbers if
num % 5==0 and num % 10 !=0]
print(result)

print()

words=["python","java","c","javascript","go"]
result=[word for word in words if len(word)>4]
print(result)

print()

numbers=[1,2,3,4,5,6,7,8,9,10]
result=[num * 2 for num in numbers if num % 2==0]
print(result)

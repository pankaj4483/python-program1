# normal loop
numbers = [1,2,3,4,5,]
square = []
for n in numbers:
    square.append(n*n)
    print(square)

print()

# using list comprehensive
numbers=[1,2,3,4,5]
square = [n*n for n in numbers]
print(square)

print()

# condition
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers= [n for n in numbers if n%2==0]
print(even_numbers)

print()

# using string
words = ["apple","bababa","kiwi","mango"]
lengths=[len(word) for word in words]
print(lengths)

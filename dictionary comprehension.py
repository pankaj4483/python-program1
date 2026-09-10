#noraml way
number=[1,2,3,4,5,6,90]
square={}
for n in number:
    square[n]=n**2
    print(square)

print()

square={n: n**2 for n in number}

print(square)

print()

words=["python","java","c","javascript"]
word_lengths= {word:len(word)for word in words}
print(word_lengths)

print()

words=["python","java","c","javascript"]
word_lengths= {word:len(word)for word in words if  len(word) > 4}
print(word_lengths)

print()

numbers=[1,2,3,4,5,6,8,9,10,20,30,40,50,60,70,80,9,0]
even_squares={num: num**2 for num in numbers  if num % 2==0}
print(even_squares)

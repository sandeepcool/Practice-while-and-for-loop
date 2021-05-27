#while loop
#1.Example

counter = 5

while counter >= 2:
  
  print(counter)
  
  counter -= 1
print()

#for loop
#2.Example

word = "sandeep"

for letter in word:
  
  print(letter, end="*")
print()

#3.Example

for I in range (1,10):
  
  if I % 2 == 0:
    
    print(I)
print()

#use break condition 

text = "sandeep"

for letter in text:


  if letter == "d":

    break

  print(letter,end = "")
print()

#4.patterns example

for i in range (4):

  for j in range (3):

    print("#", end= "")
 
print()  


#5.Binary left shift and binary right shift
#ex-1

var = 10

var_right = var >>1

var_left = var <<2

print(var, var_right, var_left)

#ex-2

x = 1
y = 0

z = ( (x == y) and (x == y) ) or not (x == y)

print( z )

#ex-3

x = 4
y = 3

a = x & y
b = x | y
c = ~x
d = x ^ y
e = x >> y
f= x << y

print(a, b, c, d, e, f)
print()

#6.Indexing lists - indexing

numbers = [10, 5, 7, 2, 1]
print("List content:", numbers)  # Printing original list content.

numbers[3] = 111
print("\nPrevious list content: ", numbers)

numbers[0] = numbers[3]
print("\nNew list content:", numbers)

print("\nLenght of the list:", len(numbers))

#Removing elements from a list
del numbers[1]

print("\nNew list content:", numbers)
print("\nNew length of the list:", len(numbers))

#practise
a = 11
b = 12
c = 13
d = 14
print(a+b+c)
print(d)
print()

#7.

import turtle
col = ('red', 'yellow', 'green', 'cyan', 'pink', 'white')
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(5)

for i in range(100) :
  
  t.color(col[i % 6])
  t.forward(i*1.5)
  t.left(59)
  t.width(3)
print()

#8.

screen = turtle.Screen()
screen.setup(600,600)
spiral = turtle.Turtle()
spiral.speed(10)
screen.bgcolor('black')
col = ("yellow", "blue", "white", "green")
c = 0

for i in range(50):

  spiral.forward(i*10)
  spiral.right(200)
  spiral.color(col[c])
  if c == 3:
    c = 0
  else:
    c+=1
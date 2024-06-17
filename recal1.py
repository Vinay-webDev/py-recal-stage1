#recalling every thing that i've learnt!!

variable = a container for a value it behaves as the value that it contains

#DATA TYPES
#STRINGS = a variable or  container for a series or collection of characters
name = "dude"
x = "1"  print(x),print("hello")
z = '3'
#INEGERS = variable which contains numbers only
x = 1
z = 10
y = -2

#FLOAT(float point numbers) = contains decimals or decimal numbers
z = 2.4
d = 33.00

#BOOLEAN = tells only true or false
are you human? = True
are you girl? = False

#MULTIPLE ASSIGNMENT = reprensenting multiple variables in single line of code

name = "dude"
x = 2
f = 200.9

#name,x,f = "dude",2,200.9

name = 1000
age = 1000
year = 1000
name, age , year = 1000

#slicing python

#      indexing[]
#      slicing()
#      [start:stop:step]
#\\\indexing///
string = "hello bro how are you?"

string1 = string[0:9]
string2 = string[:9]
#print(string)
string3 = string[10:16]
string3 = string[10:]
print(string3)

funcky_string = string[:9:2]
print(funky_string)
funky_string3 = string[10::2]
print(funky_string3)

#**** HOW TO REVERSE A STRING USING SLICING IN PYTHON ****

location = "bangalore"
reversed_location = location[::-1]
print(reversed_location)

#slicing

movie = "new jailer (2023)"
slice = slice(4,-7)
# **** here you need to change print statement in order obtain out put ***
print(movie[slice])

#IF STATEMENTS (and,or,not)
q = int(input("what is your age?: "))
if q<=18:
    print(" you are in 2nd year pu!")
elif q <=0:
    print("you haven't been born yet! ")
elif q <= 13:
    print("you are in primary school!")
else:
    print("you are too old to be in school lol")

# while loop = a statement which executes it's block of code, as long as it's condition remains true!

while 1==1:
    print("lol")

name = ""
while len(name) == 0:
    name = input("enter your name: ")
print("hello "+name)

# slicing

#name = "manjummel"
#x = slice(0,7)
#print(name[x])



#import time
#for seconds in range(10,0,-1):
 #   print(seconds)
 #   time.sleep(1)
#print("happy new year!")

#food = ["idli","dose","poori","vade","pakoda"]

#print(food)

#for x in food:
#   print(x,end=" ")
#print(food[-2])

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#quick problem on list!!!
#c = [20,40,60,80]
#c[1:4] = []
#print(c)

#def fun():
#    for x in range(22, 23, 24):
#        print(x)
#fun()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

rows = int(input("enter number of rows: "))
coloumns = int(input("enter number of coloumns: "))
symbol = input("enter the symbol: ")

for x in range(rows):
    for z in range(coloumns):
        print(symbol,end="")
    print()

rows = 3
coloumns = 5
symbol = input("enter the symbol: ")

for x in range(rows):
    for v in range(coloumns):
        print(symbol,end="")
    print()


#BASIC QUIZ GAME IN PYTHON!!!
#IT should display all questions!!!
# it should display all options for each questions!!!
#each question can only take one answer!!!
#
#nested conditions


rows = 4
coloumn = 4
symbol = "$"
special_character = "%"
for x in range(rows):
    print("_________________")
    print(symbol)
    for y in range(coloumn):
        print(special_character)

for i in range(rows):
    for j in range(coloumn):
        print(symbol)
    print(special_character)
    print("-----------------")
for i in range(rows):
    print(symbol)
    for j in range(coloumn):
        print(special_character)






























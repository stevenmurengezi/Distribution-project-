print ("hello world")
a,y,b=5,"john","stg"

print(a)
print(y)
print(b)
a="  my name, is yusuf "
print(len(a))
print (a.strip().upper()) #lenght
print(a.replace("world","everyone"))
print(a.split(","))
fruits=["orange","cherry","mango","banana"]
print(fruits)
print(fruits[3])
fruits.remove("orange")
fruits.append("avocado")
fruits[0]="watermelon"
print(fruits)
numbers=[45,65,78,32,46]
numbers.sort(reverse = True)
fruits.sort()
print(fruits)
fruits={"apple","banana","orange"}

vegetables={"carrotrs","cabbages"}

fruits.update(vegetables)

fruits.clear()
print(fruits)
car = {
   "brand" :"ford",
   "model" : "mustang",
   "year" :1967
}
print(["brand"])
print(car.keys())
print(car.items())
x = input("enter x:")
y= input("enter y:")

if x > y:
   print(f'{x}is greater than {y}')
else:

       print(f'{y} is greater than {x}')
fruits =["apple","banana","cherry"]
for x in fruits:

  print(x)
def my_function():

 print("hello from a function")

my_function()
def my_function(fname):
 print(fname+" "+"cloudine")
my_function("Email")
my_function("Tobias")
my_function("Louis")
def my_function(*kids): 
 print("the youngest child is:"+kids[2]) 
my_function("Email","Tobias","linus")
def my_function(country="Norway"):
 print("am from"+country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
def my_function(food):
  for x in food:
  print (x)
fruits=("apple","banana","cherry")
my_function(fruits)
def my_function(x):
 return 5*x
print(my_function(3))
print(my_function(5)) 
print(my_function(9))
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))
 
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))
cars=["ford","volvo","bmw"]
x=cars[0]
print(x)

cars=["ford","volvo","bmw"]
x=len(cars)
print(x)
cars=["ford","volvo","bmw"]
for x in cars:
  print(x)
class MYclass:
  x=5
p1=MYclass()
print(p1.x)
class person:
  def __init__ (self,name,age):
    self.name = name
    self.age = age

p1=person("john",36)

print(p1.name)
print(p1.age)
class person:
    def __init__ (self,fname,lname):
      self.firstname=fname
      self.lastname=lname
    def printname(self):
     print(self.firstname,self.lastname)
x=person("john","doe")
x.printname()
question 1
numbers=[1,2,3,4,5]
print(numbers[2])

this is quesition 2
structures=["stg","mango","dg"]
structures.append("hugo")
print(structures)
q3
cars=["mnb","tygg","popo"]
cars.sort(reverse = True)
print(cars)
q4
clors=["blue","green","yellow"]
y=len(clors)
print(y)
mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
class MyNumbers:
  def __itel__(self):
    self.a=1
    return self
  def __next__(self):
    x=self.a
    self.a+=1
    return x
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
x=400

def myfunc():
  global x
  x=300 

myfunc()
print(x)






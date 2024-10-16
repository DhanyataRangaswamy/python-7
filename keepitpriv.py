class Myclass:
     
 __privateVar=27;

def __privateMeth(self):
  print("Im in class Myclass")

def hello(self):
  print("The private variable is: ",Myclass.privateVar)

foo=Myclass()
foo.hello
foo.__privateMeth

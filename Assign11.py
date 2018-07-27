 Assignment-11
           -------------------


#Q.1- Create a class Animal as a base class and define method animal_attribute.

#Create another class Tiger which is inheriting Animal and access the base class method.

Ans.


class Animal():

    def animal_attribute(self):

        self.age=int(input("enter age of animal:-"))

        b=self.age

        print("Age of animal is:- ",b)

class Tiger(Animal):

    def __init__(self):

        print("inherted class:-")

g=Tiger()

g.animal_attribute()


----------------------------------------------------------------------------------------------------------------

#Q2.What will be output of following code.



class A:

    def f(self):
        return self.g()


    def g(self):
        return 'A'


class B(A):

    def g(self):
        return 'B'


a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()


Output will be- 


A B

A B


------------------------------------------------------------------------------------------------------------------



#Q.3- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission. 

Ans.


class Cop:

  name=""
  work=""
  experince=1
  designation=""
  

  def add(self,name,work,experience,designation):
    self.name=name
    self.work=work
    self.experience=experience
    self.designation=designation


  def display(self):
    print("Name: ",self.name) 
    print("Work: ",self.work)
    print("Experience(in months): ",self.experience,"months")
    print("Designation: ",self.designation)
 


class Mission(Cop):
  def add_mission_details(self,c):
      print("Mission: ",c)


x = Mission()
x.add("Raju Rastogi","Cyber Crime Branch",22,"ASP")
x.display()
x.add_mission_details("Computer Vandalism")




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area. 

Ans.

class Shape:

    def __init__(self,length,breadth):

        self.l=length
        self.b=breadth


    def Area(self):
            print("Area  is %d"%(self.l*self.b))



class Rectangle(Shape):

    def __init__(self,ln,bd):
        self.lengthh=ln
        self.brd=bd




    def Area(self):
        print("Area of rectangle is : %d"%(self.lengthh*self.brd))


class Square(Shape):

    def __init__(self,s):
        self.side=s


    def Area(self):
        print("Area of Square is :%d"%(self.side*self.side))



x=Rectangle(5,6)
y=Square(4)
x.Area()
y.Area()



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
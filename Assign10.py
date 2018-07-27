  Assignment-10
             -----------------


Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

Ans.

class Circle:
    pi = 3.14



    def __init__(self,rad):

        self.r=rad



    def getArea(self):

        area = Circle.pi * self.r * self.r

        print ("area of the circle is-> %d"%(area))

    def getCircumference(self):

        cir = 2 * Circle.pi * self.r

        print ("Circumference of the circle is-> %d"%(cir))



radius = int(input("enter radius of the circle-> "))



c1= Circle(radius)

c1.getCircumference()

c1.getArea()



----------------------------------------------------------------------------------------------------------


Q.2 Create a Student class and initialize it with name and roll number. Make methods to :

#1. Display - It should display all informations of the student.

Ans.

class Student:



    def __init__(self,na,rn):

        self.name=na

        self.rollno=rn

    def disp(self):

        print ("Name-> %s\nRoll No-> %d"%(self.name,self.rollno))



name = input("Enter your name-> ")

rollno = int(input("Enter your roll no.-> "))



s1=Student(name,rollno)

s1.disp()



-------------------------------------------------------------------------------------------------------------


Q.3 Create a Temprature class. Make two methods :

#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.

#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.


Ans.

class Temperature:
            

    def convtoF(self,cel_temp):

        self.ctemp = cel_temp

        Ftemp = (self.ctemp*1.8) + 32

        print("Temperature in Farenheit is-> ",Ftemp)

    def convtoC(self,fah_temp):

        self.ftemp = fah_temp

        Ctemp = (self.ftemp-32)/1.8

        print("Temperature in Celcius is-> ",Ctemp)



check = int(input("Enter Input(1/2) :\n1.Farenheit to Celsius\n2.Celsius to Farenheit\n"))

con = Temperature()



if (check==1):

    t=float(input("Enter Temperature in Farenheit-> "))

    con.convtoC(t)

elif(check==2):

    t=float(input("Enter Temperature in Celcius-> "))

    con.convtoF(t)

else:

    print("Wrong Input")



---------------------------------------------------------------------------------------------------------------------------------


Q.4 Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .

#Make methods to 

#1. Display-Display the details.

#2. Update- Update the movie details.


Ans.

class MovieDetails:

    def __init__(self,MN,AN,YOR,R):

        self.MovieName = MN

        self.ArtistName = AN

        self.YearOfRelease = YOR

        self.Ratings = R

    def display(self):

        print("Movie Name-> %s\nArtist Name-> %s\nYear Of Release-> %d\nRatings-> %d"%(self.MovieName,self.ArtistName,self.YearOfRelease,self.Ratings))

    def update(self,MNa,ANa,YR,Ra):

        self.MovieName = MNa

        self.ArtistName = ANa

        self.YearOfRelease = YR

        self.Ratings = Ra



movie = MovieDetails("3 Idiots","Aamir Khan",2009,9)

movie.display()

movie.update("Zindagi Na Milegi Dobara","Hrithik Roshan",2011,10)

movie.display()



----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q.5 Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 

#1. Display expenditure and savings 

#2. Calculate total salary

#3. Display salary

Ans.

class Expenditure:

    def __init__(self,ex,sav):

        self.expend=ex

        self.savings=sav

    def display(self):

        print("Expenditure= %d\nSavings= %d"%(self.expend,self.savings))

    def calculateSalary(self):

        self.sal=self.expend+self.savings

    def dispSal(self):

        print("Total Salary= %d"%(self.sal))



exp=Expenditure(1000,15000)

exp.display()

exp.calculateSalary()

exp.dispSal()



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
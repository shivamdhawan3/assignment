    Assignment-14
                     -----------------


Q.1 Name and handle the exception occured in the following program: 

a=3
if a<4:
     a=a/(a-3)
     print(a)

Ans.     

#ZeroDivisionError: division by zero 



--------------------------------------------------------------------------------------


Q.2 Name and handle the exception occurred in the following program: 

l=[1,2,3]
print(l[3])

Ans.


try:

    l=[1,2,3]
    print(l[3])#index 3 is out of range as l has max index 2


except Exception as e:
    print(e)



--------------------------------------------------------------------------------------------------


Q.3 What will be the output of the following code:

# Program to depict Raising Exception 

try:

    raise NameError("Hi Everyone")  # Raise Error

except NameError:

    print("An exception")

    raise  # To determine whether the exception was raised or not

    

Output:-  NameError: Hi Everyone 



-----------------------------------------------------------------------------------------------------



Q.4 What will be the output of the following code:



 # Function which returns a/b

def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
	    print(c)


# Driver program to test above function

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


Output:- -5.0

#a/b result in 0



------------------------------------------------------------------------------------------


Q.5 Write a program to show and handle following exceptions: 

#1. Import Error

#2. Value Error

#3. Index Error



#1. Import error



try:

    import sys
    import gw_utility.Book
except Exception as e:
    print(e)


#2.Value Errror



try:

    number = int("hello")
except ValueError as f:
    print (f,"\tEnter numbers only")



#3. Index Error



l=[5,6,8]

try:

    print(l[5])
except Exception as e:
    print(e)



----------------------------------------------------------------------------------------------------------------------------------



Q.6 Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.

#The code must keep taking input till the user enters the appropriate age number(less than 18).


Ans.


class AgeTooSmallError(Exception):
    pass
age=0


while age<18:
    age = int(input("enter your age"))

    try:

        if age<18:
            raise AgeTooSmallError("age to small")
    except Exception as e:

        print(e)



---------------------------------------------------------------------------------------------------------------------------------------

 Assignment-15
           ------------------


#Q.1 Write a Python program to read last n lines of a file.


Ans.


f = open("main.txt",'r')

last = f.readlines()

f.close()

n = input("enter no. of lines")

while n>0:

    print(last[n])

    c=-1



-----------------------------------------------------------------------------


#Q.2 Write a Python program to count the frequency of words in a file.


Ans.


file=open("abc.txt","r")

wordcount={}

for word in file.read().split():

    if word not in wordcount:

        wordcount[word] = 1

    else:

        wordcount[word] += 1

for k,v in wordcount.items():

    print(k,v)



----------------------------------------------------------------------------------



#Q.3 Write a Python program to copy the contents of a file to another file


Ans.


with open("abc.txt","r") as f1:

    with open("test.txt","w") as f2:

        for line in f1:

            f2.write(line)

    

-----------------------------------------------------------------------------------------------------------------



#Q.4 Write a Python program to combine each line from first file with the corresponding line in second file.

Ans.


with open("abc.txt","r") as f1:

    with open("test.txt","r") as f2:

        with open("new.txt","w") as f3:

            f1_list=f1.readlines()

            f2_list=f2.readlines()

            for x in range(len(f1_list)):

                f3.write(f1_list[x]+f2_list[x])





--------------------------------------------------------------------------------------------------------------------



#Q.5 Write a Python program to write 10 random numbers into a file. 

#Read the file and then sort the numbers and then store it to another file.

Ans.


import random

with open("random.txt", "w") as f:
    for i in range(int(input('How many random numbers? '))):
        line = str(random.randint(1, 100))
        f.writelines(line + '\n')
        print(line)

with open("test.txt") as f1 ,open("new.txt", "w") as f2:
       lines = f1.read().splitlines()
    lines.sort()
    
    for l in lines:
        f2.write(str(l) + '\n')


-----------------------------------------------------------------------------------------------------------------------------
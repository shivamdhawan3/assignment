   Assignment-18
                      -----------------



Q.1  Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.

import pandas as pd


myinfo = pd.DataFrame([['Ayush',20,'abc@gmail.com','7410852963']],
columns = ['name','age','email','phone_no'])

friendsinfo = pd.DataFrame([['Yash',21,'xyz@gmail.com','8520147963']],columns = ['name','age','email','phone_no'])

df = pd.concat([myinfo,friendsinfo])

print(df)

#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html#pandas.concat

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Q.2  Download the dataset
#Import the data and print the following :
#a.) First 5 rows of Dataframe 
#b.) First 10 rows of the Dataframe 
#c.) find basic statistics on the particular dataset. 
#d.) Find the last 5 rows of the dataframe 
#e.) Extract the 2nd column and find basic statistics on it.

import pandas as pd
import numpy as np

df = pd.read_csv("/Users/ayush/Desktop/data.csv")

print("First 5 rows of Data are:",df.head())

print("First 10 rows of Data are:",df.head(10))

print(df.describe())

print("last five rows\n",df.tail(5))

print("statistics on MaxTemp\n",df.MaxTemp.describe())

print("statistic on 2nd column\n",df.Location.describe())



--------------------------------------------------------------------------------------------------------------------------------------------------------
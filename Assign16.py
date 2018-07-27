 Assignment-16
            ---------------------



#Q.1 Extract the user id, domain name and suffix from the following email addresses. 

#emails = "zuck26@facebook.com" "page33@google.com""jeff42@amazon.com"

#desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]


Ans.


import re

s = re.split('[@.]',"zuck26@facebook.com")

print (s)

s = re.split('[@.]',"page33@google.com")

print (s)

s = re.split('[@.]',"jeff42@amazon.com")

print (s)



-----------------------------------------------------------------------------------------------------------------------



#Q.2 Retrieve all the words starting with ‘b’ or ‘B’ from the following text.

#text = "Betty bought a bit of butter, But the butter was so bitter, 

#So she bought some better butter, To make the bitter butter better."


Ans.


import re

text="""Betty bought a bit of butter, But the butter was so bitter,
        So she bought some better butter, To make the bitter butter better."""



p = re.compile(r'\b[bB]\w+')

print(p.findall(text))



--------------------------------------------------------------------------------


#Q.3 Split the following irregular sentence into words 

#sentence = "A, very very; irregular_sentence"

#desired_output = "A very very irregular sentence"


Ans.


import re

sentence="A,very very;irregular_sentence"

p = re.compile(r"[^A-Za-z0-9]")

print(p.sub(" ",sentence))



-------------------------------------------------------------------------------------
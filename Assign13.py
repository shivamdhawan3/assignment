 Assignment 13
          -----------------


Q.1- Difference between JSON & xml files.
Ans. The fundamental difference is that XML is a markup language (as it actually says in its name), whereas JSON is a way of representing objects (as also noted in its name).
A markup language is a way of adding extra information to free-flowing plain text,e.g  Here is some text

With XML (using a certain element vocabulary) you can put:
<Document>
    <Paragraph Align="Center">
        Here <Bold>is</Bold> some text.
    </Paragraph>
</Document>



-----------------------------------------------------------------------------------------------------------------------------------


Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup. 
Ans. 

nslookup google.com

Server:  google-public-dns-a.google.com

Address:  8.8.8.8



Non-authoritative answer:

DNS request timed out.

    timeout was 2 seconds.

Name:    google.com

Address:  172.217.24.238



nslookup facebook.com

Server:  UnKnown

Address:  2405:200:800::1



Non-authoritative answer:

Name:    facebook.com

Addresses:  2a03:2880:f12f:83:face:b00c:0:25de

          157.240.16.35



nslookup twitter.com

Server:  UnKnown

Address:  2405:200:800::1



Non-authoritative answer:

Name:    twitter.com

Addresses:  104.244.42.193
          104.244.42.65



---------------------------------------------------------------------------------------------------------------



Q3. How http works?
Ans. HTTP is a request response protocol to communicate asynchrnously between client and server. Mostly in HTTP a browser acts as a client and a web-server like Apache or IIS acts as server. The server which hosts the files (like html , audio , video files etc) responses to the client. Depending on the request a response contains the status of the request.

Different types of HTTP Requests are:

GET:  This request is Used to get the Response header and the response body!

HEAD: This request is used to get back The response header only (not the response body as returned by the GET request)

POST: This request is used to submit data (eg : for to be used in HTML forms etc..)
?
PUT: Used for uploading resource
?
PATCH: Is used to modify the resource?

DELETE: Used for deleting resource?

TRACE: Simply echoes back the request sent by the client...
       This can be used for testing the servers and Checking weather the server is alive or not.?



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Q4. What is a difference between library and API . Figure it out with examples.
Ans. A library :

	is a collection of functions / objects that serves one particular purpose.
	you could use a library in a variety of projects.


	e.g: JQuery library, is a library of prewritten,
	cross-browser Javascript animations and functions 
	which you will need while making a website.



An API : 

	is an interface for other programs to interact with your program or library 
	without having direct access.


	e.g: with Google Map APIs you can show maps for different places without 
	writing/hosting the whole code on your server, and just use it,
	usually this data transfer is in form of JSON i.e JavaScript Object Notation.



----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
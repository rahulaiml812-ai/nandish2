#creating and writing to a file
 file=open("records,text","w")    
 file.write("file handling in python/n")
 file.write("this file demonstrates write operations/n")
 file.close()
#readingfrom the file 
 file=open("records text","r")
 content=file.read()
 print("file content after with :/n",content)
 file.close()
#appending data to the file 
 file=open("records text","a")
 file write("this line is added usin append rodeln")
 file.close()
#reading again after apend
 file=open("records.text","r")
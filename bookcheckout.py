
import booksearch as r #readfile function imported 

from tkinter import messagebox 

def loan(book_ID,user_ID):
  """
  This function implemnets the Bookloan system.
  The user inputed userID and BookId is pased 
  onto the function as parameters.
  Then the function seraches for the BookID 
  in the database and mark the BookID has been 
  Checked out by the given user and also 
  updates the Log file accordingly.Database is read 
  into a list.counter used to keep 
  track of lines of data that is looped
  therefore can be used as an index when changes to list has to be made
  current_pointer is used so that when that new line is edited
  the old line can be replaced at the exact index
  index which is held in current_pointer
  """
  search=book_ID #parameters assgned to new variables 
  user=user_ID
  data=r.readfile("database") 
  counter=-1 
  current_pointer=0
  newlist=[] #initialise empty list
  for index in data: #data lis is looped to find bookID 
    counter=counter+1 #counter incromented 
    index=index.split(',')
    if index[0]==str(search): #checks if value BookID
      current_pointer=counter #if it matches counter is set to s
      if index[3]=='0':
       index[3]=str(user)
       newlist=index
       newlist=','.join(newlist)
       data[current_pointer]=newlist #newline inserted to index mentioned at s 
       newdata=open("database.txt","w") #database file opened
       for index2 in data: #new and edited list rewritten back to file
         index2=index2+"\n" #all data rewritten along with edited data back to file 
         newdata.write(index2)
       newdata.close()
       readlog(book_ID,"c") #this function updates the log file 
       #print("Book Successfully Checked out")
       messagebox.showinfo(title="Library system",message="Book Successfully Checked out")
      else:
        #print("Book not available due to being out on loan")
        messagebox.showinfo(title="Library system",message="Book not available due to being out on loan")

def readlog(book_ID,type):
  """
  This Function is similar to loan function. 
  It is used to update the log file when a book is 
  checked out or returned.The function gets the BookID 
  and the type which is either 'r'=returned or 'c'=checked out.
  Then the function reads the log file and find the 
  ID and update the record with given type(r or c). 
  the function also does a date stamp to the record 
  in log file so date is recorded when a book is 
  returned or checked out which is required 
  for book weed functionality
  """

  search=book_ID
  t=type
  counter=-1 
  current_pointer=0
  from datetime import date #import date time module to get current date 
  lists=[] #define empty lists 
  newlist=[]
  lists=r.readfile("log") #calls function to read log file to list
  for data in lists: #loops through the list
    counter=counter+1 #counter incromented
    data=data.split(',')
    if data[0]== str(search): #if BookID is in file
      current_pointer=counter #indexed logged
      currentdate=str(date.today()) #current date retreived from date time module 
      data[1]=currentdate #time stamped 
      data[2]=t #type logged 
      newlist=data
      newlist=','.join(newlist) #data editted 
      lists[current_pointer]=newlist #new list wriiten to indexed logged on 's'
      newdata=open("log.txt","w")
      for index2 in lists:
        index2=index2+"\n" #data written back to file  
        newdata.write(index2)
      newdata.close()
     
#-----
#Test script
#-----

if __name__=="__main__":
  #Be advised: Program has to be 'Killed' after each  test is executed
  
  #test 1 for readlog function: the book ID 2 is fed in as parameter
  #type will be 'c'=Checkout 
  #expected output: book id 2 record is changed, r is overwritten to c
  #to imply checkout 
  #date is also stamped
  print("TEST 1")
  readlog("2","c")

  #test 2 for readlog function: the book ID 3 is fed in as parameter
  #type will be 'r'=Return 
  #expected output: book id 3 record is changed, c is overwritten to r
  #to imply return
  #todays date is also stamped
  print("TEST 2")
  readlog("3","r")

  #test 1 for loan function: the user 4928 loans out book ID 1
  #expected output: the databse is updated where book 1 is stored
  #the new user ID is stored and date stamped on log file
  #message box outputted to user
  print("TEST 1")
  loan("1","4928")

  #test 2 for loan function: try to double check out one book
  #expected output: error message box
  print("TEST 2")
  loan("1","4928")

  






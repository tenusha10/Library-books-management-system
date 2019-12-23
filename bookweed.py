
import booksearch as r #import booksearch module 
from tkinter import messagebox
from tkinter import END
booklist=[] #global empty list




def find_books_to_weed():
    """
    This function when called  reads the log file
    and looks for books that havent been checked
    out for 30 days from todays date and returns
    a list of book ids that has matched this criteria.
    This function is called in GUI to show the user
    which books havent beeen checked out for 30 days 
    """
    weededbookid=[] #defines empty list
    import datetime #import date time module 
    weeddate= datetime.datetime.now() + datetime.timedelta(-30) #sets criteria to weed
    data=r.readfile("log") #read log file through imported function
    for record in data: #loops through list
        record=record.split(',')
        itemdate=datetime.datetime.strptime(record[1],"%Y-%m-%d") #gets the date the last time book was returned 
        if itemdate <= weeddate and record[2]=='r': #check conditon if book hasn't been checked out since 30 days drom todays date
            weededbookid.append(record[0]) #if condition met added to the list
 
  
    return weededbookid #list returned 
  
def weed(l_weed):
    """
    This function gets the list of book IDs
    that have to weeded and weed books out 
    from the file. The function ssearches both 
    the database and the log file for the book IDS 
    and if found deletes all attributes 
    associated to that book ID
    """
    listtoweed=l_weed  
    database=r.readfile("database") #reads the databse into a list using imported function
    log=r.readfile("log")#reads the log file into a list using imported function
    newdatabase=open("database.txt","w") #opens database file to be rewritten
    for record in database:
        record=record.split(',')
        n=record[0]
        if n  not in listtoweed:
            #all Book IDs with its related attributes that are not in the list to weed is written to the file
            record[3]=record[3]+"\n"
            record=','.join(record)
            newdatabase.write(record)
    newdatabase.close() #file closed
    newlog=open("log.txt","w") #text file opened and same thing is implemented 
    for bID in log:
        bID=bID.split(',')
        n=bID[0]
        if n not in listtoweed: #Ids that is not in list to weed are rewritten to the file 
            bID[2]=bID[2]+"\n"
            bID=','.join(bID)
            newlog.write(bID)
    newlog.close() #file closed 
    messagebox.showinfo(title="Library system",message="Selected Books Have been successfully weeded") #message to user 

#-----
#Test script
#-----

#Be advised: Program has to be 'Killed' after each  test is executed

if __name__=="__main__":
    #test 1 for find_books_to_weedfunction
    #the function finds books that havent been checked out for more than 30 days 
    #expected output:list of book IDs that fit weed criteria 
    test1=find_books_to_weed()
    print(test1)


    test=input("Do you want to test weed function where all books that match criteria are weeded, if so enter 'yes' if not enter 'no', **this will weed out all the books from database*** and its non reversable!!")
    if test=='yes':
        #test 1 function used along with find weed function
        #expected output: the function weeds out all the books that fit weed criteria
        weed(test1)
    else:
        #test 2 for weed function: list of book IDs will be passed onto 
        #expected output: the function will delete the Book IDs 
        #and its attributes from the file 
        weed(['6','5'])


    
    
    




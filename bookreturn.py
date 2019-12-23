
import booksearch  #import module to readfile to list
import bookcheckout #import module to update log file 
from tkinter import messagebox
from tkinter import END
from tkinter import *
booklist=[] #global empty list


def get_bookIDs(inp,u_input):
    """
    This function gets a series of use 
    inputs and added it to a list and returns the list.
    the function is needed to get a list of book IDs
    so it can be used to return multiple books at the 
    same time or weedout multiple books at once.
    The function keeps adding the input to the 
    list until 0 has been entered then returns the list  
    """
    bookid=u_input
    if bookid==None:
        messagebox.showerror(title="Library system",message="Try again")
    elif bookid=='0' or bookid==0: #break condition stops adding to list 
        messagebox.showinfo(title="Library system",message="BookIDs accepted")
    else:
        if bookid in booklist: #checks if input is already in list before appending 
            messagebox.showinfo(title="Library system",message="BookID already entered")
            inp.delete(0,END)
        else:
            booklist.append(bookid) #input added to the list
            inp.delete(0,END)

    if booklist==[]: #tells user the booklist cannot be empty
        messagebox.showwarning(title="Library system",message="Please enter at least one bookID you wish to checkout")
    else:
        return booklist #returns booklist




def returnbooks(enteredlist):
    """
    function to implement the book checkout. 
    this function gets the users inputed list of book IDS 
    as a parameter passed on. The function then reads the
    database file and serach for the bookIDs and if they
    are a match then the function updates the values 
    back to '0'(book is not checked out by any user).
    the function also calls the imported function to change
    the log file and call that function to update log file 
    """
    booklist=enteredlist #input passed on
    data=booksearch.readfile("database") #database read into list
    counter=-1 #counters to keep track of list index
    current_pointer=0
    newl=[] #initialise empty list
    found=False #boolean to check if BooIds exist in file 
    for item in data:
        counter=counter+1 #list looped 
        item=item.split(',')
        for book_ids in booklist:
            if item[0] == str(book_ids): #checks if BookIDs match
                found=True  #boolean set to true indication IDs were found 
                current_pointer=counter #index is logged 
                if item[3]=='0':
                    messagebox.showinfo(title="Library system",message="Book was never checked out") #checks if BookID trying to return was previously checked out 
                else:
                    item[3]='0'
                    newl=item 
                    newl=','.join(newl)
                    data[current_pointer]=newl  #data edited in list
                    f=open("database.txt","w")
                    for i in data:
                        i=i+"\n" #new data written back to the file
                        f.write(i)
                    f.close()
                    bookcheckout.readlog(book_ids,"r") #log file updates using imported function
                    messagebox.showinfo(title="Library system",message="BookId %d Successfully Returned"%(book_ids))
    if found==False: #if the book Id was not found error outputted 
        messagebox.showerror(title="Library system",message="BookID %s not found in database"%(book_ids))

#-----
#Test script
#-----

if __name__=="__main__":
    #Be advised: Program has to be 'Killed' after each  test is executed
    test=int(input("Please enter which test you would like to run to test return books function or enter 0 to test other function:"))
    if test==1:
        #test 1 of returnbooks function: list of book IDs passed on 
        # expected output: book IDs in list marked as returned 
        returnbooks([35,36,37,38])
    elif test==2:
        #test2 of returnbooks function:list of book IDs passed which 
        #never was checked out
        #expected output: error message
        returnbooks([21,22])
    elif test==3:
        #test 3:Book id thats not found in file is fed 
        #expected result: error message 
        returnbooks([61])
    else:
        test=int(input("Please enter which test you would like to run to test get_bookids function:"))
         #inp parameter is used to clear input box which the data is entred this 
         #is not relavent in this test script but and input box is declared otherwise
         #the test cease to execute 
        window=Tk()
        inp1=Entry(window)
        if test==1:
            #test 1 for get_bookIDs function: the book ID 1 needs to be added to the list
            #expected output: function returns a list containg 1 
            print("TEST 1")
            test1=get_bookIDs(inp1,1)
            print(test1)
    
    
        elif test==2:
            #test 2 for get_bookIDS function: multiple book ids added
            #expected output: list containing all the inputs
            print("TEST 2")
            test2=get_bookIDs(inp1,2)
            test2=get_bookIDs(inp1,3)
            test2=get_bookIDs(inp1,4)
            print(test2)
        

        elif test==3:
            #test 2 for get_bookIDS function: adding same ID again
            #expected output: error message 
            print("TEST 3")
            test3=get_bookIDs(inp1,4)
            test3=get_bookIDs(inp1,2)
            test3=get_bookIDs(inp1,2)
        window.mainloop()


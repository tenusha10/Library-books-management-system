from tkinter import * #importing the tkinter module to design the GUI
from tkinter import ttk
from tkinter import messagebox 

import booksearch #importing the modules where the functions are written
import bookcheckout
import bookreturn
import bookweed

booklist=[] #Global list 

#-----
#Functions
#-----


def valid(inp):
    """ 
    This Function is validation function 
    which checks the users input is in 'INT' format.
    if it is not in format it catches the Error 
    and if the input is in correct format 
    it returns the value. This function 
    is used throughout the program to validate 
    integers for example validate Book IDs 
    """
    while True: 
        try:
            userInput = int(inp.get()) #gets the user input form inputbox
        except ValueError:
            messagebox.showerror(title="Library system",message="Not in valid ID format! Try again.") #if error produced error message created 
            inp.delete(0,END) #inputbox values cleared 
            break #breaks loop
        else:
            return userInput #if no error function returns
            break

def checklen(inp):
    """
    This function is also a validation function. 
    it is used to check the User IDs 
    inputted are valid user ID (1000-9999). 
    if they are not function returns and 
    error to the user if not the function 
    returns the user input
    """
    while True:
        u=valid(inp) #first runs the function to check input in integer format
        if u>=1000 and u<=9999: #checks user id is within range 
            break
        else:
            messagebox.showerror(title="Library system",message="Valid user IDs must be between 1000-9999") #error message for user 
            inp.delete(0,END)
    
    return u #returns the input if all conditions met 

def btn1clicked():
    """
    This function is called when Btn3 is clicked. 
    The module to search books is called within the button
    and a search is performed. 
    the outputs from book search function 
    is then outputted into the tree structre.
    also additional checks are carried out
    for example checks if the searched books/s 
    is available or currently out on loan 
    """
    tree.delete(*tree.get_children()) #clears the data that may already be in tree
    search_word=inp1.get() #gets user input 
    search_word=search_word.lower()
    outpt=booksearch.search(search_word) #imporeted search function executed 
    for l in outpt: #loops through the returned list 
        item=l.split(',') 
        id = tree.insert('', 'end', text="BookID="+item[0]) 
        tree.columnconfigure(1,weight=100) #output added to the tree view structure 
        tree.insert(id, 'end', text="Title:"+item[1])
        tree.insert(id, 'end', text="Author:"+item[2])
        if item[3]=='0': #condition checks if the serached book is available for checkout
            tree.insert(id, 'end', text="Book available for checkout")
        else:
            tree.insert(id, 'end', text="Book currently out on loan")

def btn2clicked():
    """
    Function is called when btn2 is clicked.
    This executes the Book checkout of the GUI. 
    the functions calls the imported bookcheckout 
    module and produce the output into the GUI
    """
    user_ID=checklen(inp2) #calls validation functions 
    book_ID=valid(inp3)
    bookcheckout.loan(book_ID,user_ID) #executes imported functions 
    inp2.delete(0,END) #clears the input boxes 
    inp3.delete(0,END)

def btn3clicked():
    """
    This function is called when Btn3 is clicked.
    This executes the Book Return of the GUI. 
    The Functions calls the imported bookReturn module.
    Firstly the function gets a list of 
    validated BookIDs (using validation functions)using the get_bookIDS function then feeds the book list into function 
    return books in the module to implement the book return 
    """
    userinput=valid(inp4) #validate user input
    entered_list_to_return=bookreturn.get_bookIDs(inp4,userinput) #calls function to get a list of books to checkout 
    if userinput==0: #conditon to break loop in get_book IDs function
        bookreturn.returnbooks(entered_list_to_return) #the list is fed into return books function

def btn4clicked():
    """
    This function is called when btn4 is clicked. 
    This executes the Book Return of the GUI.
    The function calls the imported bookWeed module.
    The GUI displays all the books ids that match the Weeding criteria. 
    this function asks the user, if they would like to weed out all the books that are specifed in the GUI 
    """
    userinput=inp5.get() #gets userinput from input box 
    stringuserinput=str(userinput)#converts the input to string 
    stringuserinput.lower() #convert srtring to lower case
    inp5.delete(0,END) #clears input box 
    if stringuserinput=="yes": # checks if the input ois yes 
        bookweed.weed(books_to_weed) #if yes all books weeded that was returned from find_books_to_weed function (books_to_weed)
    elif stringuserinput=="no": #if not user adviced to enter the list of book ids in the input box directly below 
        messagebox.showinfo(title="Library system",message="Please use the input box and button directly below to add the Book IDs you wish to weed out")

def btn5clicked():
    """
    This function is called when btn5 is clicked. 
    This executes the Book Return of the GUI.
    The function calls the imported bookWeed module.
     As the user doesn't want to weed out all books. 
     user is given the option to input the book IDS that 
     they would like to weed out  
    """
    messagebox.showinfo(title="Library system",message="Please enter the Book_IDs \n of the books you wish to Weed \n (Please input '0' to stop)")
    userinput=valid(inp6) #validate user input
    userinput=str(userinput)
    entered_list_to_weed=bookreturn.get_bookIDs(inp6,userinput) #retrives a list of book IDS using imported function 
    if userinput=='0': #conditon to break loop in get_book IDs function
        bookweed.weed(entered_list_to_weed) #function to weed out called 

# ------
# main program starts
# -------

#-----
#GUI 
#-----

window=Tk() #sets window tkinter
#setting attributes of the window 
window.title("Library System")
window.geometry('650x600')

#defining labels and setting attributes 
Label(window,text="Book Search",font="Verdana 15 bold").grid(row=0)
Label(window, text="Search word").grid(row=1)

#defines entry widget and set attribiutes 
inp1=Entry(window)
inp1.grid(row=1, column=1)

#define button and sets attributs and what function to call when clicked
btn1=Button(window,text="Submit",command=btn1clicked)
btn1.grid(row=1,column=2)

#Defines a tree view structure for serach ouput
tree = ttk.Treeview(window)
tree.grid(column=0, row=2, columnspan=3, sticky=EW)

#defining labels and setting attributes
Label(window,text="Book Checkout",font="Verdana 15 bold").grid(column=0,row=10)
Label(window, text="UserID").grid(row=12)

#defines entry widget and set attribiutes 
inp2=Entry(window)
inp2.grid(row=12, column=1)

#defining labels and setting attributes
Label(window, text="BookID").grid(row=13)

#defines entry widget and set attribiutes 
inp3=Entry(window)
inp3.grid(row=13, column=1)

#define button and sets attributs and what function to call when clicked
btn2=Button(window,text="Submit",command=btn2clicked)
btn2.grid(row=13,column=2)

#defining labels and setting attributes
Label(window,text="Book Return",font="Verdana 15 bold").grid(column=0,row=15)
Label(window, text="Please enter the Book_IDs \n of the books you wish to return \n (Please input '0' to stop)").grid(column=0,row=17)

#defines entry widget and set attribiutes 
inp4=Entry(window)
inp4.grid(row=17, column=1)

#define button and sets attributs and what function to call when clicked
btn3=Button(window,text="Submit",command=btn3clicked)
btn3.grid(row=17,column=2)

#defining labels and setting attributes
Label(window,text="Book Weed",font="Verdana 15 bold").grid(column=0,row=19)
Label(window, text="Would you like to weed all books mentioned below? \n If so enter 'yes' or enter 'no' \nif you only want to weed out specific books").grid(column=0,row=21)

#defines entry widget and set attribiutes 
inp5=Entry(window)
inp5.grid(row=21, column=1)

#defining labels and setting attributes
label1=Label(window)
label1.grid(column=0,row=26,columnspan=3, sticky=EW)

#imported module bookweed and a function in it is called here
#this function finds the books in database and log file that fits weed criteria
#returns a list and this list is diplayed to user
books_to_weed=bookweed.find_books_to_weed()
if books_to_weed==[]: #if returned list is empty then user advised as mentioned 
    label1.configure(text="No books to weed currently")
else:
    line="Books with bookID %s \nhavent been checked out for 30 days"%(str(books_to_weed)) #returned list is outputted 
    label1.configure(text=line)

#define button and sets attributs and what function to call when clicked
btn4=Button(window,text="Submit",command=btn4clicked)
btn4.grid(row=21,column=2)

#defines entry widget and set attribiutes 
inp6=Entry(window)
inp6.grid(row=23, column=1)

#define button and sets attributs and what function to call when clicked
btn5=Button(window,text="Add to list",command=btn5clicked)
btn5.grid(row=23,column=2)

window.mainloop()
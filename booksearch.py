from tkinter import messagebox #importing a tkinter module


def readfile(name):
    """
    This is function which is reused 
    throughout the program. The purpose of this 
    function is to open the specified file and 
    read the contents of the file and add the 
    data to a list and return the list 
    """
    lists=[] #defines empty list
    data=open("%s.txt"%(name),"r") #opens file specified on parameter
    lines=data.readlines() #read every line of file
    for index in lines: 
        index.split(',') #each line is appended into  a list 
        index = index.strip()
        lists.append(index)
    data.close() #file closed 
    return lists #list is returned 


def search(s):
    """
    This function implements the serach functionality.
    Function takes the input as a parameter and search 
    the specified file and if found returns the fields 
    associated with it 
    """
    found=False #Boolean checks if the search was successful
    lists=[] #defines empty list
    data=readfile("database") #file read and added to list
    searchword=s #paramater read into variable
    for item in data: #list looped 
        item=item.split(',')
        for index in range(0,3):
            if item[index]==str(searchword): #checks if cuurent index match serachword
                found=True #boolean set to true implies serach success 
                output=','.join(item)
                lists.append(output) #found value added and attributes added to output list 
    if found==False: #if boolean still false after loop implies search unsuccessful 
        #message outputted 
        messagebox.showwarning(title="Library system",message="Book not Found")
    return lists   #output list returned  



#-----
#Test script
#-----

if __name__=="__main__":
    #test 1 for readfile function: reads the databse file
    #correct output: All data on mentintioned file added to list
    test1=readfile("database")
    print("TEST 1")
    print(test1)

    #test 2 for readfile function: reads the log file
    #correct output: All data on mentintioned file added to list
    print("TEST 2")
    test2=readfile("log")
    print(test2)
    
    #test 1 for serach function: serach for keyword in file:
    #correct output: seraches for the keyword passed on as parameter
    print("TEST 1")
    test1=search("2")
    print(test1)

    #test 2 for serach function: serach for keyword in file:
    #correct output: seraches for the keyword passed on as parameter
    print("TEST 2")
    test2=search("william shakespeare")




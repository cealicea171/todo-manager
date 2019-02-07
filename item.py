import time
import datetime

#Make a class called Item. Objects of this class should have the following attributes:
#A timestamp of when they were created.
#A boolean marking the item as completed or not.
#And the text of the actual to-do item.

class Item():
    def showAll():
        readTask = open("todos.txt", "r")
        ##(file, action)
        #readTask is the variable that is getting assigned to opening the text file, read only... because of the r

        message = readTask.read()
        #reads the file
        print(message)
        readTask.close()
#..
        ##closes the file
    def markComplete():
        edit = open("todos.txt").read()
        ##this is making the variable edit open the text file and read it
        completedTask = input("What Task Did You Complete? ")
        ##then this making the variable completedTask and make it a input and print out the question?
        s = edit.replace( completedTask, completedTask +  " COMPLETE✔️")
        ##(looking , action)
        #(looking, getting it and putting completed beside it.)
        #this is taking the variable s and having it take the user input and add completed next to it.
        f2 = open("todos.txt", 'w+')
        ##f2 overrides (=edit) read and makes it write
        f2.write(s)
        ##it changing the permission from read to write
        f2.close()
        ##closes the file..

        ##this Prints all of the to-do items in the list.
        f = open('todos.txt','r')
         #(file, action)
        #f is the variable that is getting assigned to opening the text file, read only... because of the r
        message = f.read()
        #message is being sent to f.read f is opening file, .read is taking file and reading it. message is the file
        print(message) #then printing the message

        ##exiting it outPsy
        f.close()

    def createTask():
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # add timestamp from imported modules
         #this Adds a new item to the list.
        file1 = open("todos.txt","a+")#append mode
        #file1 is the varaiable that is getting assigned to opening a txt file, reading and adding(appending) whatever you write
        task = input("Create A New Task: ")
        #this is taking variable task and assigning it to an input that prints out create a new task..

        #...
        file1.write("\n" + task + " " + now)

        ##this is saying take the file1, read it and write the new task you just entered on a new line ..
        file1.close()
        ##this closes the text file
Item.showAll()
Item.createTask()
Item.markComplete()

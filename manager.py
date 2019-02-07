from item
# #Make a class called Manager. A single object of this class should be created when you run your script. It should do the following:
# #Print all of the to-do items in the list.
# #Add a new item to the list.
# #Mark an item as completed..
class  Manager(Item):






































# # class Manager
# # def print_all(f):
# #     print(f.read())
# #
# #
# # print("Your tasks for this week are: ", to_do)
# #
# # #mark an item as a completed..
# # tuff = ten_things.split(' ')
# # #The split() method splits a string into a list.
# # print("Adding: ", to_do)
# # stuff.append(to_do)
# # #append Add an item to the end of the list
# # print(f"There are {len(stuff)} items now.")
#
# #this Prints all of the to-do items in the list.
#f = open('todos.txt','r') #(file, action)
# #f is the variable that is getting assigned to opening the text file, read only... because of the r
#message = f.read()
#message is being sent to f.read f is opening file, .read is taking file and reading it. message is the file
#print(message) #then printing the message
#f.close()#exiting it out
#
# #this Adds a new item to the list.
# file1 = open("todos.txt","a+")#append mode
# #file1 is the varaiable that is getting assigned to opening a txt file, reading and adding(appending) whatever you write
# task = input("Create A New Task: ")
# #this is taking variable task and assigning it to an input that prints out create a new task..
 #file1.write("\n"+ task)
# #this is saying take the file1, read it and write the new task you just entered on a new line ..
 #file1.close()
# #this closes the text file
#
#
# #this Marks an item as completed.
# edit = open("todos.txt").read()
# #this is making the variable edit open the text file and read it
# completedTask = input("What Task Did You Complete? ")
# #then this making the variable completedTask and make it a input and print out the question?
 #s = edit.replace( completedTask, completedTask + " completed")#(looking , action)
# #(looking, getting it and putting completed beside it.)
# #this is taking the variable s and having it take the user input and add completed next to it.
#
# f2 = open("todos.txt", 'w+')
# #f2 overrides (=edit) read and makes it write
# f2.write(s)
# #it changing the permission from read to write
# f2.close()
#closes the file

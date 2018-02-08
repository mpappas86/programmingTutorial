# The big revelation of this file is that we can read information in from files. This means, by changing the files,
# we can change the behavior of our code, *without having to change the code itself, nor its inputs*. The file
# "3_filename.txt" that we are using here is an example of a very simple "database".

# We saw this in the previous file - the import keyword says "I want to use the code in the 'os' folder"
import os

# Again, we define a function. This time, it takes 0 arguments.
def load_name_from_file():
    # There's a chain of keywords here that almost always get used together. Roughly, this line in plain english means:
    # "Open the file called '3_filename.txt', and create a variable called "opened_file" whose value is that file."
    with open('3_filename.txt') as opened_file:
        # Now opened_file is a variable whose value is a "file", but we don't care about everything about the file.
        # For instance, we don't care when it was last opened. We just want the text of the file. So we call the
        # "read" function to grab the text from inside the file, and set that as the value of the variable "name".
        name = opened_file.read()
    return name

# Here we see one of the biggest advantages of functions - you can call it twice! That's much less code than if you had
# to write out the instructions to open the file and read the contents multiple times!
print 'Hello ' + load_name_from_file() + ', assuming ' + load_name_from_file() + ' is your real name!'

# name = load_name_from_file()
# print 'Hello ' + name + ', assuming ' + name + ' is your real name!'

# Here we see two new special keywords: "def" and "return". These keywords go hand in hand.
# "def" means "I am creating a function" - that is, a piece of code that we want to be able
# to use repeatedly moving forward. The name of that function is the thing that comes after "def".
# In this case, the function is named "use_specific_name".
# The word, or words, inside the parentheses are called "arguments", and are the inputs to that specific
# function (as opposed to the inputs to the overall program.) So "use_specific_name" takes one argument,
# named "name". This is a variable that can be used in the function.
def use_specific_name(name):
    # The "return" keyword defines the output of the function. In contrast to "print", which is output of the
    # overall program, and so goes straight to Terminal or whatever other application is running python,
    # functions return values *inside your program*, and those values can be reused later. We'll see this
    # below in a moment.
    # We also see here that python is a fairly human-readable programming language. Even with no programming
    # experience, it's hopefully not too hard to tell that the below +'s mean to add the strings together.
    # So if "name" has the value "Fred", the result of the additions will be "Hello Fred!". This is then
    # returned by the function as its output.
    return "Hello " + name + "!"

# Here we see commented code, which shows the other value of comments - if you wrote code you don't want
# to delete, but don't want to use right now, you can "comment it out" so that it gets skipped over.
# If we did run this code, it would involve two steps. The first is to "import" something called sys.
# Import just means "use the code from this directory" - so on my computer, there's a directory called "sys"
# with more python files. One of those python files defines a special function "sys.argv", which returns a
# list of all the inputs to the program. So using this, we could be setting the "my_name" variable to the 1st input to
# the program. Right now we comment this out, because we've defined what we want my_name to be below.

# import sys; my_name = sys.argv[1]


# Set the value of "my_name" to "Bob"
my_name = 'Bob'

# Using print again, we produce an output of this program. In this case, the output is the result of
# calling the function "use_specific_name" on the variable "my_name". So the value of "my_name" - that
# is, Bob, is set as the value of the "name" variable inside the "use_specific_name" function. And
# "use_specific_name" returns "Hello Bob!", so that's what we output here.
print use_specific_name(my_name)

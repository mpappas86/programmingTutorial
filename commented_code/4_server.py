# This is our first example of a "server" - that is, a program that never stops running unless it's explicitly asked.

# Again, it's nice that python is human readable. "While 1 is equal to 1, keep doing this thing" definitely sounds
# like the sort of thing that would keep the code running forever - and indeed it does! In particular, as long as
# 1 is equal to 1, the server will run all the code "inside" the while loop (the indented code), and then it will start
# from the top and repeat again!
while 1 == 1:
    # "raw_input" is a special keyword that means "ask the user this thing, and then return their response!"
    # So when this line is hit, we'll ask the user that they'd like the server to say, and save that value 
    # into the variable "what_the_user_said".
    what_the_user_said = raw_input('What would you like me to say?\n')

    # This is the one way to stop our server - if the user specifically says "STOP", this condition
    # will be satisfied, and we'll run the code inside the "if" block - the indented code. In this
    # case, that code is the keyword "break", which means "stop running the while loop RIGHT NOW, no matter what".
    if what_the_user_said == 'STOP':
        break

    # Assuming we haven't stopped the server, it will say what you asked it to, and then rinse and repeat!
    print 'Per your request, let me just say ' + what_the_user_said
    print '\n\n'

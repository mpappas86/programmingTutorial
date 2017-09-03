while True:
    what_the_user_said = raw_input('What would you like me to say?\n')
    if what_the_user_said == 'STOP':
        break
    print 'Per your request, let me just say ' + what_the_user_said
    print '\n\n'

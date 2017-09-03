import os


def load_name_from_file():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '3_filename.txt'))) as opened_file:
        name = opened_file.read()
    return name

print 'Hello ' + load_name_from_file() + ', assuming ' + load_name_from_file() + ' is your real name!'

# name = load_name_from_file()
# print 'Hello ' + name + ', assuming ' + name + ' is your real name!'

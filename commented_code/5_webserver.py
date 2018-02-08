# We're now going to graduate from "server" to "webserver" - the difference being that a 
# webserver takes input and sends output to your browser! To do this, we're going to rely
# on a python package called "flask", which provides us with the "Flask" object you see below.
# We save the Flask object to a variable called app, and when we call app.run(), it does something
# extremely similar to our while loop from before - except it's sending input and output to our browser now!

# (This is a slight simplification - it's actually sending the input/output to what's called a "port", and
# our browser is then listening to that "port" on our computer - but the end result is what you'd expect!)

from flask import Flask
app = Flask(__name__)


# This "@app.route" command is called a "decorator", and means "use this function in a predifined way".
# In this case, the predefined way is "this function's output is what should be used for the webpage with '/' added onto our URL".
# To see this more clearly, let's pretend we were running this server as example.com, and the route was '/randomexample'. Then
# the output of this function would appear as the webpage "example.com/randomexample".
@app.route("/")
def hello():
    return "Hello World!"

app.run()

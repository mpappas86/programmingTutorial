# This is almost identical to our previous webserver example, except this time, instead of returning
# simple text ("Hello World!"), we're now loading HTML from a file and sending that. 
# I'll comment in the HTML file more about what's going on there.

from flask import Flask
import os

app = Flask(__name__, static_folder=os.path.dirname(__file__))


@app.route("/")
def home():
    print 'Im hit!'
    return app.send_static_file('6_index.html')

app.run()

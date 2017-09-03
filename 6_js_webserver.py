from flask import Flask
import os

app = Flask(__name__, static_folder=os.path.dirname(__file__))


@app.route("/")
def home():
    print 'Im hit!'
    return app.send_static_file('6_index.html')

app.run()

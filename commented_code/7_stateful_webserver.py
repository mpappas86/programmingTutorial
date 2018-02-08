# Lots going on here, but luckily we've already talked through most of it! The key change is that
# we're now trying to track whether or not you've already been to the website and clicked the button.
# We're going to do that with our "database" - a simple text file! 

# When you click the button (see the HTML), the "clicked" function below will be called, which will write
# to our database file the fact that you've clicked the button. Then, even if the user refreshes the page, our
# database file is unharmed! And whenever the user loads the main page (through the "home" function), we no
# longer just return the HTML - we also pass an argument, clicked=read_from_database(). What this means is
# we're giving the HTML a variable, called "clicked", whose value is the result of the read_from_database() function.
# So the HTML now has a variable that tells it whether or not you've clicked the button before - and can display the date accordingly!

from flask import Flask, render_template, jsonify
import os

app = Flask(__name__, template_folder=os.path.dirname(__file__))

DATABASE_FILE = os.path.join(os.path.dirname(__file__), '7_database_file.txt')

BUTTON_WAS_CLICKED = 'clicked'
BUTTON_NOT_YET_CLICKED = 'never_clicked'


@app.route("/")
def home():
    return render_template('7_index.html', clicked=read_from_database())


@app.route("/api/clicked")
def clicked():
    write_to_database()
    return jsonify(success= True)


def write_to_database():
    if not read_from_database():
        print 'writing to file'
        with open(DATABASE_FILE, 'w') as f:
            f.write(BUTTON_WAS_CLICKED)
        print 'wrote to file'


def read_from_database():
    # If we don't have a database file, create it.
    if not os.path.isfile(DATABASE_FILE):
        os.mknod(DATABASE_FILE)
    with open(DATABASE_FILE, 'r') as f:
        current_value = f.read()
        return current_value == BUTTON_WAS_CLICKED

app.run()

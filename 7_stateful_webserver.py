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

**Mike's Simple Programming Tutorial**

The goal of this tutorial is to build up methodically but quickly to an understanding of how webservers work.
This tutorial is intended for non-technical people primarily, as a means to give them the basic understanding and
vocabulary to understand technical work at a high level.
This tutorial uses Python and the Flask webserver, as well as HTML and Javascript on the front end.

You can run all code for the corresponding lessons by simply running `python 1_helloworld.py` (substitute the correctly
numbered python file) from a terminal window. For later lessons, `flask` is required, which can be installed via the
terminal command `pip install flask`.

Finally, it's worth noting that this README is not meant as a full lesson plan, but rather a guide for a technical teacher
to follow.

# Lesson 1: The simplest possible Python script
This script has only one line - a print statement, which is the simplest way Python produces `output` that the user can
see or interact with.

# Lesson 2: Variables and Functions!
Programming is powerful because it's able to process its `inputs` before producing an `output`. This script contains
examples of the most important pieces of that. First, we put our input into a `variable`, which is how we refer to data we
are in the middle of processing. We then pass that variable into a `function`, which manipulates the variable - in this
case, by combining it with some other strings. Finally, we print the output.

# Lesson 3: Storage
Rather than having to pass all your input into your scripts every time, you may want to store your data in a persistent
way. In general, you do this in a `database`, of which there are many types, but by far the simplest type is a simple
file. Here, we see the name to be used as input is stored in a file, and then read from the "database" in order to be
processed.

# Lesson 4: Servers
So far, we've only seen scripts that take input, process it, produce output, and then are finished. This script is our
first example of a `server` - that is, a script that runs indefinitely, always listening in case its given more input
for it to process.

# Lesson 5: Webservers
`Webservers` are servers whose "inputs" are requests coming in from the web, and "outputs" are webpages that should be
shown to those users. This is the simplest possible example - a webserver that servers up the same "Hello World" webpage
to all users who request it.

These things really just load and show files, and the IPs are addresses to other computers's files. See e.g. 172.217.6.206 for google.com.

# Lesson 6: Javascript Webservers
We now add another trick by allowing our webserver to serve up webpages with interesting functionality. This functionality
is described using two different languages, `HTML` and `Javascript`. HTML is used to lay out the different elements of
the webpage, while Javascript, similarly to Python, is a processing language meant to take user inputs and use those to
change the output the user sees. In this example, we see a simple Javascript button that changes what's visible on the
webpage.

# Lesson 7: Stateful Webservers
You might have noticed in Lesson 6 that if you refreshed the webpage, then you'd be forced to click the button again in
order to see the datetime. But since you've already pressed the button once, it should be possible for the webpage to
already know that you've done so. Here we achieve that by combining the Javascript Webserver with the file-based
database from lesson 3. In order to tell Python to write to the database, our webpage sends out an HTTP request to the
Python server - and similarly, in order for Python to tell the webpage what the database knows, it passes data into the
webpage before sending the webpage along to the user.

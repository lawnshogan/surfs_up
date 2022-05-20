from flask import Flask

# Create a new Flask App Instance called app
app = Flask(__name__)

# __name__ variable denotes the name of the current function. 
# You can use the __name__ variable to determine if your code is being run from the command line or if it has been imported into another piece of code. 
# Variables with underscores before and after them are called magic methods in Python.

# Create Flask routes
# Need to define the starting point, also known as the root
@app.route('/')
def hello_world():
    return 'Hello world'

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request

#
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# '/' URL is bound with welcome() function.
def welcome():
    return "Welcome to the Flask Web Server!"

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

    @app.route('/login', methods=['POST'])
    def login():

        data = request.args.get("data", "")
        iterations = int(data)
        for i in range(iterations):
            print(f"Iteration {i}")

        # Rest of the login logic
        ...

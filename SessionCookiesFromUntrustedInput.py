# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, make_response

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

@app.route('/login', methods=['POST'])
def login():

    # Get the UserId from the request arguments
    user_id = request.args.get('UserId')

    if user_id:
        # Create a response object
        resp = make_response(f"Cookie is set for UserId: {user_id}")

        # Set a cookie with the UserId
        resp.set_cookie('UserId', user_id)

        return resp
    else:
        return "UserId not provided", 400

# main driver function
if __name__ == '__main__':
    app.run()

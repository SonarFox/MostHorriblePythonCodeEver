from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user_id = request.form.get('user_id')
    response = make_response("Logged in")
    response.set_cookie('session_id', user_id)  # Vulnerable: setting session cookie from untrusted input
    return response

if __name__ == "__main__":
    app.run(debug=True)

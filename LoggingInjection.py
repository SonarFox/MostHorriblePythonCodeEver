import logging
from flask import Flask, request

app = Flask(__name__)

# Setup logger
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

@app.route('/example')
def log():
    data = request.args.get("data", "")
    app.logger.critical("%s", data)  # Noncompliant
    return "Logged data"

if __name__ == "__main__":
    app.run(debug=True)

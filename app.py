from flask import Flask

app = Flask(__name__)

# First endpoint (Home Page)
@app.route("/")  
def home():
    return "<h1>Welcome to the Home Page!</h1>"

# Second endpoint (/Yuvi Page)
@app.route("/Yuvi")
def yuvi():
    return "<h1>Welcome to the Yuvi Page!</h1>"


#path parameter 
@ app.route("/Welcome/<name>")
def welcome(name):
    return f"<h1> Hi {name.title()}, U are Welcome  !</h1>"
# title make the string first word Captial

#int path parameter 
@ app.route("/addition/<int:num>/<int:num2>")
def addition(num ,num2):
    return f"<h1>Input {num}, U are Output is {num + num2} !</h1>"


if __name__ == "__main__":
    app.run(debug=True)  # Runs the Flask app only once

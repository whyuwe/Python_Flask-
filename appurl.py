from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> Welcome to the Home Page </h1>"

@app.route("/Welcome/<name>")   # Dynamic Url
def welcome_name(name):
    return f"<h1> Hey {name.title()} , How are U ? </h1>"

@app.route("/information/<name>/<int:age>") # Dynamic Url
def information(name, age):
    return f"<h1> Hey {name.title()} , You are {age} years old ? </h1>"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, redirect, url_for
import time 

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> Welcome to the Home Page </h1>"

@app.route("/pass/<name>")   # Dynamic URL
def passed(name):
    return f"<h1>Congrats {name.title()}, You are Passed</h1>"

@app.route("/fail/<name>")   # Dynamic URL
def failed(name):
    return f"<h1>Sorry {name.title()}, You are failed</h1>"

@app.route("/score/<int:num>/<name>")
def score(num, name):
    time.sleep(1)  # Delay for 1 second

    if num > 30:
        return redirect(url_for("passed", name=name))  # Pass 'name' argument
    else:
        return redirect(url_for("failed", name=name))  # Pass 'name' argument

if __name__ == "__main__":
    app.run(debug=True)

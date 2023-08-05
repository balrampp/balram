from flask import Flask,url_for,redirect

app = Flask(__name__)

@app.route("/home")

def home():
    return "wellcome all"

@app.route("/hllo world")
def hello():
    return "hello world"

@app.route("/Hi")
def hi():
    return "How are you"
@app.route("/user/<enter>")
def user(enter):
   if enter=="welcome":
        return redirect(url_for("home"))
   elif enter=="hello":
    return redirect(url_for("hello"))
   else:
       return redirect(url_for("id"))


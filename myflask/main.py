from flask import Flask,render_template
#import flask
#print(flask.__version__)

app=Flask(__name__) #create instance of a Flask


@app.route("/") #@ is the decorator

# def home():
#     return "hello world"
# def bhaskar():
#     return "welcome back"

def home_page():
    return render_template("home.html")


# @app.route("/info")
# def info_page():
#     return "<h2> waiting for new information <h2>"
#
# @app.route("/contact")
# def contact_page():
#     return "<h2> please contact at +91 - 9790815622 <h2>"

@app.route("/<name>")
def user(name):
    #return f"<h1>hello, {name} </h1>"
    return render_template('home.html',myname=name)
@app.route("/info")
def info_page():
    return render_template('info.html')

@app.route("/contact")
def contact_info():
    return render_template('contact.html')



app.run()
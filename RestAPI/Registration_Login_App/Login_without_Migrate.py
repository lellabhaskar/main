from flask import Flask,render_template,request

from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy

#pip install flask-migrate


app= Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:welcome$1234@localhost/regis_login_db"
db=SQLAlchemy(app)

api=Api(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html",validuser=False)
    else:
        if request.method == 'POST':
            print('your in login page')
            username=request.form["username"]
            password = request.form["password"]
            print(username)
            check_user=User.user_check(username=username,password=password)
            print(check_user)
            if check_user:
                return render_template("application.html")
            else:
                #dicdata = {'message': username, 'status': 404}
                return render_template("login.html",validuser=False)


@app.route("/registration", methods=['GET','POST'])
def registration():
    if request.method == 'GET':
        return render_template("registration.html")
    else:
        if request.method == 'POST':
            print('your in registration page')
            username = request.form["username"]
            password = request.form["password"]
            valid_user_check=User.user_check(username=username,password=password)
            if valid_user_check:
                return render_template('registration.html',exist=True)
            else:
                addeduser=User.add_user(username=username,password=password)
                return render_template('registration.html', usercheck=addeduser)

@app.route("/application", methods=['GET','POST'])
def app_page():
    if request.method == 'GET':
        return render_template("application.html")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)

    @staticmethod
    def add_user(username,password):
        new_user=User(username=username,password=password)
        result=db.session.add(new_user)
        db.session.commit()
        return result

    @staticmethod
    def user_check(username,password):
        data=User.query.filter_by(username=username,password=password).first()
        return data


if __name__=="__main__":
    app.run()

# use below commands:
#flask --app Login.py db init
#flask --app Login.py db migrate
#flask --app Login.py db upgrade
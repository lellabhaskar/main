from flask import Flask,render_template,request

from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#pip install flask-migrate
import os

class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://root:1234@localhost/regis_login_db'

class Development_Config(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:1234@localhost/regis_login_db'


class Production_Config(Config):
    uri=os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = uri


env = os.environ.get("ENV","Development")

if env == "Production":
    config_str=Production_Config
else:
    config_str=Development_Config


app= Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:welcome$1234@localhost/regis_login_db"
db=SQLAlchemy(app)
migrate=Migrate(app,db) #new
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
        return render_template("registration.html",flagreg=False)

    else:
        if request.method == 'POST':
            print('your in registration page')
            username = request.form["username"]
            password = request.form["password"]
            valid_user_check=User.user_check(username=username,password=password)
            if valid_user_check:
                return render_template('registration.html',existcheck=True,flagreg=True)
            else:
                addeduser=User.add_user(username=username,password=password)
                return render_template('registration.html', existcheck=False,flagreg=True)

@app.route("/application", methods=['GET','POST'])
def app_page():
    if request.method == 'GET':
        return render_template("application.html")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    #email = db.Column(db.String(80), nullable=False)

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

# deploying to Heroku
#1. create new app name -- bhaskar-registrationlogin
#2. go to terminal  -- heroku login
#type any key for forward and login
#3.git init
#4.git add .
# git status
# git remote add origin bhaskar-registrationlogin
# git commit -m "added new registration"
# git push heroku master


                    ## ssh keys
# go to Terminal and type
#ssh-keygen -t rsa -b 4096 -C "lellabhaskar@gmail.com"
#ls -l ~/.ssh

# got to gitbash and type
#eval $(ssh-agent -s)
#ssh-add      ~/.ssh/id_rsa

#cat ~/.ssh/id_rsa.pub

#go to git and settings --SSH and GPH Keys
# add New SSH Key -- Title and paste key from gitbash using cat command

# ssh -T git@github.com
# and type yes and enter

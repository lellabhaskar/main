from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_restful import Api,Resource
from http import HTTPStatus

app= Flask(__name__)
api=Api(app)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:welcome$1234@localhost/moviedatabase"
db=SQLAlchemy(app)
        #1
# class user(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(80),unique=True,nullable=False)
#     email=db.Column(db.String(120),unique=True,nullable=False)


        #1 run through python console
# from flasksqlalchemy_test import db
# db.create_all()



# class profile(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(80),unique=True,nullable=False)
#     email=db.Column(db.String(120),unique=True,nullable=False)

        # 2 run through python console
    # from flasksqlalchemy_test import profile
    # admin=profile(username='bhaskar',email='lellabhaskar@gmail.com')
    # db.session.add(admin)
    # db.session.commit()

       #3
# from flasksqlalchemy_test import db
# db.create_all()

        #4
# from flasksqlalchemy_test import profile
# admin=profile(username='teja',email='teja@gmail.com')
# db.session.add(admin)
# db.session.commit()


        #5

#profile.query.all()
# [<profile 1>, <profile 3>, <profile 4>, <profile 5>]

# profile.query.filter_by(username='bhaskar').first()
# <profile 1>
# profile.query.filter_by(username='teja').first()
# <profile 5>
# profile.query.filter_by(username='siris').first()
# <profile 3>
# profile.query.filter_by(username='devaansh').first()
# <profile 4>


#             # 6 new movie
# class movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)


      # task 1
#from flasksqlalchemy_test import profile
#db.create_all()



                     # 7 new movie using classes

# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)
#
#     @staticmethod
#     def add_movie(title, year, genre):
#         new_movie=Movie(title=title,year=year,genre=genre)
#         db.session.add(new_movie)
#         db.session.commit()
#
#     @staticmethod
#     def get_movies():
#         data=Movie.query.all()
#         return data
#
#
#
# class AllMovies(Resource):
#     def post(self):
#         data=request.get_json()
#         print(data)
#
#         Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
#         return ""
#
#
#     def get(self):
#         data=Movie.get_movies()
#         print(data)
#         movielst=[]
#
#         for moviedata in data:
#             dictmove={'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
#             movielst.append(dictmove)
#         return movielst
#
#

# api.add_resource(AllMovies,"/movies")
# app.run()




 # task 1
#from flasksqlalchemy_test import db
#db.create_all()

# task 2

# from flasksqlalchemy_test import movie
# add_movie=profile(title='aditya 365',year='1995',genre='')
# db.session.add(add_movie)
# db.session.commit()


                    # 8 get_id based on ID
# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)
#
#     @staticmethod
#     def add_movie(title, year, genre):
#         new_movie=Movie(title=title,year=year,genre=genre)
#         db.session.add(new_movie)
#         db.session.commit()
#
#     @staticmethod
#     def get_movies():
#         data=Movie.query.all()
#         return data
#


# class AllMovies(Resource):
#     def post(self):
#         data=request.get_json()
#         print(data)
#
#         Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
#         return ""
#
#
#     def get(self):
#         data=Movie.get_movies()
#         print(data)
#         movielst=[]
#
#         for moviedata in data:
#             dictmove={'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
#             movielst.append(dictmove)
#         return movielst



#api.add_resource(AllMovies,"/movies")

# run postman
#http://127.0.0.1:5000/movies

# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)
#
#     @staticmethod
#     def add_movie(title, year, genre):
#         new_movie=Movie(title=title,year=year,genre=genre)
#         db.session.add(new_movie)
#         db.session.commit()
#
#     @staticmethod
#     def get_movies():
#         data=Movie.query.all()
#         return data
#
#
# class AllMovies(Resource):
#     def post(self):
#         data=request.get_json()
#         print(data)
#         Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
#         return ""
#
#     def get(self):
#         data=Movie.get_movies()
#         print(data)
#         movielst=[]
#
#         for moviedata in data:
#             dictmove={'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
#             movielst.append(dictmove)
#         return movielst
#
#
# class OneMovie(Resource):
#     def get(self,id):
#         data=Movie.get_movies()
#         for movieone in data:
#             dicmovie={}
#             print(movieone)
#             if movieone.id == id:
#                 dicmovie['title']=movieone.title
#                 dicmovie['year'] = movieone.year
#                 dicmovie['genre'] = movieone.genre
#                 return jsonify(dicmovie)
#         else:
#              return jsonify({'message':'ID not found','status':404})

#
# api.add_resource(AllMovies,"/movies")
# api.add_resource(OneMovie,"/movies/<int:id>")
# app.run()

                # filter by option instead of for loop

# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # this is the primary key
#     title = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     genre = db.Column(db.String(80), nullable=False)
#
#     @staticmethod
#     def add_movie(title, year, genre):
#         new_movie=Movie(title=title,year=year,genre=genre)
#         db.session.add(new_movie)
#         db.session.commit()
#
#     @staticmethod
#     def get_movies():
#         data=Movie.query.all()
#         return data
#
#     @staticmethod
#     def get_movie_id(id):
#         data=Movie.query.filter_by(id=id).first()
#         return data
#
#     @staticmethod
#     def get_movie_delete_id(id):
#         delmovie = Movie.query.filter_by(id=id).delete()
#         db.session.commit()
#         return delmovie
#
#
# class AllMovies(Resource):
#     def post(self):
#         data=request.get_json()
#         print(data)
#         Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
#         return "Sucessfully added the Movie"
#
#     def get(self):
#         data=Movie.get_movies()
#         print(data)
#         movielst=[]
#
#         for moviedata in data:
#             dictmove={'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
#             movielst.append(dictmove)
#         return movielst
#
#
# class OneMovie(Resource):
#     def get(self,id):
#         dicdata = {}
#         data=Movie.get_movie_id(id)
#         if data:
#             dicdata['title'] = data.title
#             dicdata['year'] = data.year
#             dicdata['genre'] = data.genre
#
#             return jsonify((dicdata),{'status':HTTPStatus.OK})
#         else:
#             #return jsonify({'message':'ID not found','status':404})
#             return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})
#
#     def delete(self,id):
#         onemovie=Movie.get_movie_delete_id(id)
#         print(onemovie)
#         if onemovie:
#             return "sucessfully deleted the movie id {0}".format(id)
#         else:
#             return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})
#
#
# api.add_resource(AllMovies,"/movies")
# api.add_resource(OneMovie,"/movie/<int:id>")
# app.run()

                # filter by option update
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    @staticmethod
    def add_movie(title, year, genre):
        new_movie=Movie(title=title,year=year,genre=genre)
        db.session.add(new_movie)
        db.session.commit()

    @staticmethod
    def get_movies():
        data=Movie.query.all()
        return data

    @staticmethod
    def get_movie_id(id):
        data=Movie.query.filter_by(id=id).first()
        return data

    @staticmethod
    def get_movie_delete_id(id):
        delmovie = Movie.query.filter_by(id=id).delete()
        db.session.commit()
        return delmovie

    @staticmethod
    def update(id,title,year,genre):
        updatemovie = Movie.query.filter_by(id=id).first()

        updatemovie.title=title
        updatemovie.year = year
        updatemovie.genre = genre

        db.session.commit()

class AllMovies(Resource):
    def post(self):
        data=request.get_json()
        print(data)
        Movie.add_movie(title=data["title"],year=data['year'],genre=data['genre'])
        return "Sucessfully added the Movie"

    def get(self):
        data=Movie.get_movies()
        print(data)
        movielst=[]

        for moviedata in data:
            dictmove={'id':moviedata.id,'title':moviedata.title,'year':moviedata.year,'genre':moviedata.genre}
            movielst.append(dictmove)
        return movielst


class OneMovie(Resource):
    def get(self,id):
        dicdata = {}
        data=Movie.get_movie_id(id)
        if data:
            dicdata['title'] = data.title
            dicdata['year'] = data.year
            dicdata['genre'] = data.genre

            return jsonify((dicdata),{'status':HTTPStatus.OK})
        else:
            return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})

    def delete(self,id):
        onemovie=Movie.get_movie_delete_id(id)
        print(onemovie)
        if onemovie:
            return "sucessfully deleted the movie id {0}".format(id)
        else:
            return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})

    def put(self,id):
        moviedata = request.get_json()
        Movie.update(id,moviedata['title'],moviedata['year'],moviedata['genre'])
        if moviedata:
            return "sucessfully updated the movie id {0}".format(id)
        else:
            return jsonify({'message': 'ID not found', 'status': HTTPStatus.NOT_FOUND})


api.add_resource(AllMovies,"/movies")
#api.add_resource(OneMovie,"/movie/<int:id>")
api.add_resource(OneMovie,"/movies/<int:id>")
app.run()

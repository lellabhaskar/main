# from flask import Flask,request,jsonify
# app = Flask(__name__)
#
# # @app.route("/",methods=['GET'])
# # def home():
# #     return "<h2>Bhaskar</h2>"
# #
# # app.run()
# user_list=[{'name':'Bhaskar','age':26},{'name':'Sirisha','age':28}]
# # user_list[0].update({'name':'Bhaskar','age':27})
# # print(user_list)
#
# @app.route("/",methods=['GET'])
# def home():
#     if request.method =='GET':
#         json_data=jsonify(user_list)
#     return json_data
#
#
# @app.route("/",methods=['POST'])
# def home_post():
#     if request.method =='POST':
#         data=request.get_json()
#         user_list.append(data)
#     return user_list
#
#
# @app.route("/",methods=['DELETE'])
# def home_delete():
#     if request.method=='DELETE':
#         user_list.clear()
#     return user_list
#
#
# @app.route("/<int:age>",methods=['PUT'])
# def home_update(age):
#     print('prasham')
#     print(age)
#     if request.method =='PUT':
#         for lst in user_list:
#             lst.update({'age':27})
#     return user_list
#     # if request.method == 'PUT':
#     #     for lst in user_list
#     #
#     #     return user_list
#
#
# app.run()



    #2

from flask import Flask,request,jsonify
app = Flask(__name__)
import json

recipes=[
    { 'id': 1, 'name': 'Salad',  'description': 'This is a lovely Greek salad recipe.'   },
    { 'id': 2, 'name': 'Rava Masala Dosa', 'description': 'This is recipe for Rava Masala Dosa.'  }
        ]

@app.route("/recipes",methods=['GET'])
def home():
        if request.method =='GET':
            recipes_data=jsonify(recipes)
        return recipes_data


@app.route("/recipes/<int:id>",methods=['GET'])
def home_id(id):
        if request.method =='GET':
            newrecipelst = []
            for recipe in recipes:
                if id==recipe['id']:
                    newrecipelst.append(recipe)
                    return newrecipelst
            else:
                return "please enter matches ID's only"
            # return newrecipelst


@app.route("/recipes/<int:id>",methods=['DELETE'])
def home_delete_id(id):
        if request.method =='DELETE':
            newrecipelst = []
            for recipe in recipes:
                if id==recipe['id']:
                    print(recipe)
                    recipes.remove(recipe)
                    return recipes
            else:
                return "ID not match"

@app.route("/recipes/<int:id>",methods=['PUT'])
def home_update_id(id):
        if request.method =='PUT':
            for recipe in recipes:
                if id==recipe['id']:
                    print(recipe)
                    recipesdata=request.get_json()
                    # input 1
                    # {
                    #     "description": " Masala Dosa ...."
                    #  }
                    #recipe.update(recipesdata)
                    #return recipes

                    #input 2
                    # {"id": 2,
                    #  "name": "DOSA",
                    #  "description": " Masala Dosa ...."
                    #  }
                    recipe.update({'id':recipesdata['id'],'name':recipesdata['name'],'description':recipesdata['description']})
                    return jsonify(recipes)
            else:
                return "please enter proper input "


app.run()
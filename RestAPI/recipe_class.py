from flask import Flask,jsonify,request
from flask_restful import Api, Resource

app = Flask(__name__)
api=Api(app)

# json data
recipes=[
    {
        'id': 1,
        'name': 'Salad',
        'description': 'This is a lovely Greek salad recipe.'
    },
    {
        'id': 2,
        'name': 'Rava Masala Dosa',
        'description': 'This is recipe for Rava Masala Dosa.'
    }
        ]

# Classes -- allRecipes and oneRecipe

class allRecipes(Resource):
    def get(self):
        return recipes
        #return jsonify(recipes)

        # input of post

        # {"id": 3,
        #  "name": "special Dosa",
        #  "description": " Masala Dosa ...."
        #  }
    def post(self):
        recipe_data = request.get_json()
        recipes.append(recipe_data)
        return recipes

class oneRecipe(Resource):
    # def get(self):
    #     pass

    def get(self,recipe_id):
        for recipe in recipes:
            if recipe['id'] ==recipe_id:
                return recipe
                #return jsonify(recipe)
        else:
            return jsonify({'message':'ID not found'})


        #input of put
        # {
        #     "description": " Masala Dosa ...."
        #  }

    def put(self,recipe_id):
        for recipe in recipes:
            if recipe_id == recipe['id']:
                print(recipe)
                recipesdata = request.get_json()
                recipe.update(recipesdata)
                return recipes
        else:
            return "please enter proper input "

    def delete(self,recipe_id):
        for recipe in recipes:
            if recipe_id == recipe['id']:
                recipes.remove(recipe)
                return recipes

api.add_resource(allRecipes,"/recipes")
api.add_resource(oneRecipe,"/recipes/<int:recipe_id>")
app.run()


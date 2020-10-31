from flask import Flask, request, redirect
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Echo(Resource):
    def get(self, message):
        return {'message':message}

api.add_resource(Echo, '/echo/<string:message>')

if __name__ == "__main__":
    app.run(debug=True)

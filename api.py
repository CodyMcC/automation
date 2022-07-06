from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

class ExampleEndpoint(Resource):
    def get(self):
        return {'data': "sample data"}, 200

    def post(self):
        data = request.data

        parser = reqparse.RequestParser()
        parser.add_argument('sample', required=False)

        args = parser.parse_args()

        data = {'sample': args["sample"] + " is awesome!"}

        return data

api.add_resource(ExampleEndpoint, "/example")

if __name__ ==  "__main__":
    app.run()
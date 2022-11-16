from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

class Temperature(Resource):
    def get(self):
        print("Got a request!!!")
        return {"data": "sample data"}, 200

    def post(self):
        data = request.data
        parser = reqparse.RequestParser()

        parser.add_argument("room", required=False)
        parser.add_argument("temperature", required=False)
        args = parser.parse_args()

        print(f"Stuff {data}")

api.add_resource(Temperature, "/temp")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)
import os
import json

from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime


def CtoF(x):
    return (x * 9 / 5) + 32


class Data:

    def __init__(self):
        self.values = []

    def add(self, room, value):
        template = {
            "measurement": "environment",
            "tags": {
                "room": room
            },
            "time": datetime.utcnow(),
            "fields": {
                "temperature": CtoF(value)
            }
        }
        self.values.append(template)






bucket = "home"
print(os.environ.get('INFLUXDB_TOKEN'))
client = InfluxDBClient(url="http://192.168.1.231:8086", token='HITBo8sQN86Deo2mjAJJxBdxSYiLwSfYQfCVDoSg1x2QUQWvQLHB7cixfMHmy0Lb7k0rxGMsaiRX4u0DtUPhHw==', org="mccomber")


write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
from random import randint
json_payload = []
data1 = {
    "measurement": "environment",
    "tags": {
        "room": "office"
    },
    "time": datetime.utcnow(),
    "fields": {
        "temperature": 70 + randint(-5, 5)
    }
}
data2 = {
    "measurement": "environment",
    "tags": {
        "room": "bedroom"
    },
    "time": datetime.utcnow(),
    "fields": {
        "temperature": 60 + randint(-5, 5)
    }
}
print(datetime.now())
json_payload.append(data1)
json_payload.append(data2)
# write_api.write(bucket=bucket, record=json_payload)

def fix_json(x):
    x.replace('"', "!Q!Q")
    x.replace("'", '"')
    x.replace("!Q!Q", "'")
    return json.loads(x)


app = Flask(__name__)
api = Api(app)

class Temperature(Resource):
    def get(self):
        print("Got a request!!!")
        return {"data": "sample data"}, 200

    def post(self):
        data = request.data
        parser = reqparse.RequestParser()

        # parser.add_argument("room", required=False)
        # parser.add_argument("temperature", required=False)
        parser.add_argument("data", required=False)
        args = parser.parse_args()

        print(data.decode())
        print(args)
        influx_data = Data()
        for item in json.loads(data.decode()).get('data'):
            print(item)
            # item = json.loads(item)
            influx_data.add(item.get('room'), item.get('temperature'))


        # print(json_payload)
        print(influx_data.values)
        write_api.write(bucket=bucket, record=influx_data.values)


api.add_resource(Temperature, "/temp")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)
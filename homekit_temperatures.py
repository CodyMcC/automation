from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "my-bucket"

client = InfluxDBClient(url="http://192.168.1.231:8086", token="my-token", org="my-org")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)

write_api.write(bucket=bucket, record=p)

## using Table structure
tables = query_api.query('from(bucket:"my-bucket") |> range(start: -10m)')

for table in tables:
    print(table)
    for row in table.records:
        print (row.values)


## using csv library
csv_result = query_api.query_csv('from(bucket:"my-bucket") |> range(start: -10m)')
val_count = 0
for row in csv_result:
    for cell in row:
        val_count += 1


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

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=1234)
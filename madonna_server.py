from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from random import randint

from songs import getASong

app = Flask(__name__)
api = Api(app)


class Madonna_Song(Resource):
    def get(self):

        song = getASong()

        return jsonify(song)

api.add_resource(Madonna_Song, '/madonna_song') #Route_4

#if __name__ == '__main__':
#     app.run(port='5002')
if __name__ == '__main__':
     app.run(host='0.0.0.0')

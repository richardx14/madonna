from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from random import randint

from songs import getASong, getAllSongs

app = Flask(__name__)
api = Api(app)


class Madonna_Song(Resource):
    def get(self):

        song = getASong()

        return jsonify(song)

class All_Madonna_Songs(Resource):
	def get(self):

		songs = str(getAllSongs())

		return jsonify(getAllSongs())

api.add_resource(Madonna_Song, '/madonna_song') #Route_4
api.add_resource(All_Madonna_Songs, '/all_madonna_songs')

#if __name__ == '__main__':
#     app.run(port='5002')
if __name__ == '__main__':
     app.run(host='0.0.0.0')

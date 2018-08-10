from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from random import randint

from get_a_song import *

app = Flask(__name__)
api = Api(app)

# n API's

# get_all_Songs - shows all available songs
# get_a_Song - gets a song of the day (That has not been shown before)
# get_all_my_songs - shows all of my songs to date
# get_my_day_count - show my day count
# reset_my_songs - delete all trace of me so I can start again

class Get_A_Song(Resource):
	def get(self):

		song = getASong()

		# get user id
        # provide song
        # update songs to date and day count

		return jsonify(song)


class Get_All_Songs(Resource):
	def get(self):

		songs = getAllSongs()

		return jsonify(songs)


class Get_All_My_Songs(Resource):
	def get(self):

		songs = getAllMySongs("richardx14-1")

		return jsonify(songs)


class Get_My_Day_Count(Resource):
	def get(self):

		song = getASong()

		return jsonify(song)


class Reset_My_Songs(Resource):
	def get(self):

		song = resetMySongs("richardx14-1")

# Old API's below

class Madonna_Song(Resource):
    def get(self):

        song = getASong()

        # get user id
        # provide song
        # update songs to date and day count

        return jsonify(song)

class All_Madonna_Songs(Resource):
	def get(self):

		songs = str(getAllSongs())

		return jsonify(getAllSongs())

api.add_resource(Get_All_Songs, '/get_all_songs')
api.add_resource(Get_A_Song, '/get_a_song')
api.add_resource(Get_All_My_Songs, '/get_all_my_songs')
api.add_resource(Get_My_Day_Count, '/get_my_day_count')
api.add_resource(Reset_My_Songs, '/reset_my_songs')



# get_all_Songs - shows all available songs
# get_a_song - gets a song of the day (That has not been shown before)
# get_all_my_songs - shows all of my songs to date
# get_my_day_count - show my day count
# reset_my_songs - delete all trace of me so I can start again

# Old API's below

#api.add_resource(Madonna_Song, '/madonna_song') #Route_4
#api.add_resource(All_Madonna_Songs, '/all_madonna_songs')

#if __name__ == '__main__':
#     app.run(port='5002')
if __name__ == '__main__':
     app.run(host='0.0.0.0')

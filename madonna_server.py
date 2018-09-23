import os
import sys

from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from random import randint

#from get_a_song import *
from madonna_methods import *

app = Flask(__name__)
api = Api(app)

 # which port to use

if (len(sys.argv)>1) :

	portNumber = sys.argv[1]
	print ("port number by argument =", portNumber)

else:
	portNumber = 5000
	print ("port number by default =", portNumber)

get_all_songs_endpoint = False
get_a_song_endpoint = False
get_all_my_songs_endpoint = False
get_my_day_count_endpoint = False
reset_my_songs_endpoint = False
create_new_user_endpoint = False


# which endpoints to expose

if "get_all_songs_endpoint" in sys.argv:
	get_all_songs_endpoint = True
	print("get_all_songs_endpoint enabled")

if "get_a_song_endpoint" in sys.argv:
	get_a_song_endpoint = True
	print("get_a_song_endpoint enabled")

if "get_all_my_songs_endpoint" in sys.argv:
	get_all_my_songs_endpoint = True
	print("get_all_my_songs_endpoint enabled")

if "get_my_day_count_endpoint" in sys.argv:
	get_my_day_count_endpoint = True
	print("get_my_day_count_endpoint enabled")

if "reset_my_songs_endpoint" in sys.argv:
	reset_my_songs_endpoint = True
	print("reset_my_songs_endpoint enabled")

if "create_new_user_endpoint" in sys.argv:
	create_new_user_endpoint = True
	print("create_new_user_endpoint enabled")


if ((len(sys.argv) <= 2) or ("all_endpoints" in sys.argv)) :
	get_all_songs_endpoint = True
	get_a_song_endpoint = True
	get_all_my_songs_endpoint = True
	get_my_day_count_endpoint = True
	reset_my_songs_endpoint = True
	create_new_user_endpoint = True

	print("All endpoints enabled")

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

#portNumber = 5000
#print ("port number by default = ", portNumber)

# n API's

# get_all_Songs - shows all available songs
# get_a_Song - gets a song of the day (That has not been shown before)
# get_all_my_songs - shows all of my songs to date
# get_my_day_count - show my day count
# reset_my_songs - delete all trace of me so I can start again

class Get_A_Song(Resource):
	def get(self):

		song = getASong("richardx14-1")

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

		dayCount = getMyDayCount("richardx14-1")

		return (dayCount)

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

class Create_New_User(Resource):

	def get(self):

		return jsonify(createNewUser())

class Get_Health(Resource):

	def get(self):

		return jsonify("Health = OK")


if (get_all_songs_endpoint):
	api.add_resource(Get_All_Songs, '/get_all_songs')

if(get_a_song_endpoint):
	api.add_resource(Get_A_Song, '/get_a_song')

if(get_all_my_songs_endpoint):
	api.add_resource(Get_All_My_Songs, '/get_all_my_songs')

if (get_my_day_count_endpoint):
	api.add_resource(Get_My_Day_Count, '/get_my_day_count')

if (reset_my_songs_endpoint):
	api.add_resource(Reset_My_Songs, '/reset_my_songs')

if (create_new_user_endpoint):
	api.add_resource(Create_New_User, '/create_new_user')

# Health

api.add_resource(Get_Health,'/')

# get_all_Songs - shows all available songs
# get_a_song - gets a song of the day (That has not been shown before)
# get_all_my_songs - shows all of my songs to date
# get_my_day_count - show my day count
# reset_my_songs - delete all trace of me so I can start again

#if __name__ == '__main__':
#     app.run(port='5002')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=portNumber)

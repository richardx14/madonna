from __future__ import print_function # Python 2/3 compatibility
from random import randint
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from dynamodb.madynamodb.madynamodb import *

# get a song
# get list from item
# add song to list
# increase day count TO DO
# write item back to db
# show db item

def createSongList():

	songs = [
	"4 Minutes",
	"American Life",
	"B-Day Song",
	"Bad Girl",
	"Beat Goes On",
	"Beautiful Killer",
	"Beautiful Stranger",
	"Bedtime Story",
	"Best Friend",
	"Bitch I'm Madonna",
	"Body Shop",
	"Borderline",
	"Burning Up",
	"Candy Store",
	"Celebration",
	"Cherish",
	"Crazy For You",
	"Dance Tonight",
	"Dear Jessie",
	"Deeper and Deeper",
	"Devil Pray",
	"Devil Wouldn't Recognize You",
	"Die Another Day",
	"Don't Tell Me",
	"Dress You Up",
	"Erotica",
	"Everybody",
	"Express Yourself",
	"Falling Free",
	"Frozen",
	"Future Lovers",
	"Gang Bang",
	"Get Together",
	"Ghosttown",
	"Girl Gone Wild",
	"Give it 2 Me",
	"Give Me All Your Luvin'",
	"Holiday",
	"Holy Water",
	"Human Nature",
	"Hung Up",
	"I Don't Give A",
	"I Fu--ed Up",
	"I Love New York",
	"I'll Remember",
	"I'm a Sinner",
	"I'm Addicted",
	"Iconic",
	"Illuminati",
	"Incredible",
	"Into The Groove",
	"Joan Of Arc",
	"Justify My Love",
	"La Isla Bonita",
	"Like A Prayer",
	"Like A Virgin",
	"Live To Tell",
	"Living For Love",
	"Love Song",
	"Love Spent",
	"Lucky Star",
	"Masterpiece",
	"Material Girl",
	"Miles Away",
	"Mother and Father",
	"Music",
	"Nothing Really Matters",
	"Oh, Father",
	"One More Chance",
	"Open Your Heart",
	"Papa Don't Preach",
	"Promise To Try",
	"Rain",
	"Ray Of Light",
	"Rebel Heart",
	"Rescue Me",
	"Revolver",
	"She's Not Me",
	"Some Girls",
	"Spanish Lessons",
	"Substitute For Love",
	"Superstar",
	"Take A Bow",
	"The Power Of Goodbye",
	"This Used To Be My Playground",
	"True Blue",
	"Turn Up the Radio",
	"Unapologetic Bitch",
	"Veni Vidi Vici",
	"Vogue",
	"Voices",
	"Wash All Over Me",
	"What It Feels Like For A Girl",
	"Who's That Girl",
	"You'll See"]

	return(songs)

def getASong():

	print("Getting a song.")

	songList = createSongList()

	if songList:
		foo2 = randint(0,len(songList)-1 )
		songOfTheDay = songList[foo2]
		print("Song of the day is " + songOfTheDay + ".")

		# write to db.

		addASong("richardx14-1", songOfTheDay)

		#putItem("madonnaSongs", "eu-west-2", "richardx14-3", "http://localhost:8000")
		
		return(songOfTheDay)

	else:
		return ("Madonna has run out of songs!")

def setUpDB(region, endpoint=''):
	if(endpoint):
		dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
	else:
		dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)

	return(dynamodb)


def addASong(user, song):

# variables

	region = "eu-west-2"
	table = "previousSongs"
	endpoint = "http://localhost:8000"
	#userID = "richardx14-1" # need to look this up in future

	dynamodb = setUpDB(region, endpoint)

	#foo = getItem(table, region, userID, endpoint)
	#item = getItem(table, region, userID, endpoint)['Item']

	#songs = item['songSoFar']

	songs = getItem(table, region, user, endpoint)['Item']['songSoFar']

	songs.append(song)

	# now put item back

	table = dynamodb.Table(table)

	response = table.put_item(
		Item={
			'userID': user,
			'dayCount': 0,
			'songSoFar': songs
			}
		)

	print("addASong succeeded:")

	#print(json.dumps(response, indent=4, cls=DecimalEncoder))

	# test

	foo = getItem("previousSongs", "eu-west-2", "richardx14-1", "http://localhost:8000")

def getAllSongs():

	print("Getting all songs.")

	songList = createSongList()

	return(songList)

def getAllMySongs(user):

# variables

	region = "eu-west-2"
	table = "previousSongs"
	endpoint = "http://localhost:8000"
	#userID = "richardx14-1" # need to look this up in future

	dynamodb = setUpDB(region, endpoint)

	#foo = getItem(table, region, userID, endpoint)
	#item = getItem(table, region, userID, endpoint)['Item']

	#songs = item['songSoFar']

	allMySongs = getItem(table, region, user, endpoint)['Item']['songSoFar']

	print("get all my songs succeeded:")

	return(allMySongs)

def resetMySongs(user):

# variables

	region = "eu-west-2"
	table = "previousSongs"
	endpoint = "http://localhost:8000"
	#userID = "richardx14-1" # need to look this up in future

	dynamodb = setUpDB(region, endpoint)

	table = dynamodb.Table(table)

	response = table.delete_item(
		Key={
			'userID': user,
		}
	)

	print(json.dumps(response, indent=4, cls=DecimalEncoder))

	print("Reset my songs succeeded:")





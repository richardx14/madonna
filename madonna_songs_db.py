from __future__ import print_function # Python 2/3 compatibility
from random import randint
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from dynamodb.madynamodb.madynamodb import *

# get a song
# write a song
# get song attributes
# show item
# song = { ’songID’: “Vogue”, ‘writers’: “Madonna”, ‘album’:  “Vogue”, ‘year’: “1995”}

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
	]

	return(songs)

def getEndpoint():

	#endpoint_url = ''
	#endpoint_url = "http://localhost:8000"
	endpoint_url = "http://127.0.0.1:8000"

	return(endpoint_url)


def setUpDB(region, endpoint=''):

	endpoint = getEndpoint()

	if(endpoint):
		dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
	else:
		dynamodb = boto3.resource('dynamodb', region_name=region)

	return(dynamodb)

def getAMadonnaSong():

	region = "eu-west-2"
	table = "madonnaSongs"
	endpoint = getEndpoint()
	dynamodb = setUpDB(region, endpoint)
	table = dynamodb.Table(table)

	print("Getting a song.")

	response = table.get_item(
		Key={
			'songID' : "Vogue"
			}
		)

	album = response['Item']['album']
	year = response['Item']['year']
	writers = response['Item']['writers']

	print(album)
	print(year)
	print(writers)



def addASong():

# variables

	region = "eu-west-2"
	table = "madonnaSongs"
	endpoint = getEndpoint()
	dynamodb = setUpDB(region, endpoint)
	table = dynamodb.Table(table)

	# put item back

	# song = { ’songID’: “Vogue”, ‘writers’: “Madonna”, ‘album’:  “Vogue”, ‘year’: “1995”}

	songID = "Vogue"
	writers = "Madonna"
	album = "Vogue"
	year = "1995"

	response = table.put_item(
		Item={
			'songID' : songID,
			'writers': writers,
			'album' : album,
			'year' : year
			}
		)

	print("addASong succeeded:")


def getAllMadonnaSongs():

# variables

	region = "eu-west-2"
	table = "madonnaSongs"
	endpoint = getEndpoint()
	dynamodb = setUpDB(region, endpoint)
	table = dynamodb.Table(table)

	allSongs = table.scan()

	print(allSongs)

	for i in allSongs:
		print(i)

def getMyDayCount(user):

# variables

	region = "eu-west-2"
	table = "previousSongs"
	endpoint = getEndpoint()

	#userID = "richardx14-1" # need to look this up in future

	dynamodb = setUpDB(region, endpoint)

	dayCount = getItem(table, region, user, endpoint)['Item']['dayCount']

	print("get my day count succeeded:")

	return(str(dayCount))


addASong()
getAMadonnaSong()
getAllMadonnaSongs()




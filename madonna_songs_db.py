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

def getEndpoint():

	#endpoint_url = ''
	#endpoint_url = "http://localhost:8000"
	endpoint_url = "http://127.0.0.1:8000"

	return(endpoint_url)

def setUpDBTable():

	#endpoint_url = ''
	#endpoint_url = "http://localhost:8000"
	endpoint = "http://127.0.0.1:8000"
	region = "eu-west-2"

	if(endpoint):
		dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
	else:
		dynamodb = boto3.resource('dynamodb', region_name=region)

	table = "madonnaSongs"
	table = dynamodb.Table(table)

	return(table)


def setUpDB(region, endpoint=''):

	endpoint = getEndpoint()

	if(endpoint):
		dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
	else:
		dynamodb = boto3.resource('dynamodb', region_name=region)

	return(dynamodb)

def getAMadonnaSong():

	table = setUpDBTable()

	print("Getting a song TWO.")

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

	table = setUpDBTable()

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

	songID = "True Blue"
	writers = "Madonna"
	album = "True Blue"
	year = "1995"

	response = table.put_item(
		Item={
			'songID' : songID,
			'writers': writers,
			'album' : album,
			'year' : year
			}
		)

	songID = "Holiday"
	writers = "Madonna"
	album = "Madonna"
	year = "1983"

	response = table.put_item(
		Item={
			'songID' : songID,
			'writers': writers,
			'album' : album,
			'year' : year
			}
		)

	songID = "Lucky Star"
	writers = "Madonna"
	album = "Madonna"
	year = "1983"

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

	table = setUpDBTable()

	allSongs = table.scan()

	count = 0
	for i in allSongs:
		count = count+1
		print(count)
		print(i)

	print("No of items on line below")
	print(table.item_count)

def getAttributeForSong(songID, attribute):

	table = setUpDBTable()

	response = table.get_item(
		Key={
			'songID' : songID
			}
		)

	if response == '':
		attribute = "Attribute not found"
	else:
		attribute = response['Item'][attribute]

	return(attribute)

#################

addASong()
getAMadonnaSong()
getAllMadonnaSongs()

print(getAttributeForSong("Vogue", "album") )

print(getAttributeForSong("Vogue", "writers") )

print(getAttributeForSong("Vogue", "year") )

#print(getAttributeForSong("Vogue", "nonsense"))

#print(getAttributeForSong("Vogusdfasdgfdfg", "nonsense"))







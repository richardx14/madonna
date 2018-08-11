from __future__ import print_function # Python 2/3 compatibility
from random import randint
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from dynamodb.madynamodb.madynamodb import *

def getEndpoint():

    # endpoint_url = ''
    endpoint_url = "http://localhost:8000"

    return(endpoint_url)

def getRegion():

    region = "eu-west-2"

    return(region)

def createPreviousSongsTable():

    endpoint = getEndpoint()
    region = getRegion()
    table = 'previousSongs'

    if(endpoint):
        dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
    else:
        dynamodb = boto3.resource('dynamodb', region_name=region)


    table = dynamodb.create_table(
        TableName=table,
        KeySchema=[
            {
                'AttributeName': 'userID',
                'KeyType': 'HASH'  #Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'userID',
                'AttributeType': 'S'
            },
#           {
#              'AttributeName': 'songSoFar',
#                'AttributeType': 'S'
#           },
#          {
#                'AttributeName': 'dayCount',
#                'AttributeType': 'N'
#            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table status:", table.table_status)

def createTable(table, region, endpoint = '' ):

    if(endpoint):
        dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
    else:
        dynamodb = boto3.resource('dynamodb', region_name=region)


    table = dynamodb.create_table(
        TableName=table,
        KeySchema=[
            {
                'AttributeName': 'userID',
                'KeyType': 'HASH'  #Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'userID',
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table status:", table.table_status)

def deletePreviousSongsTable():

    endpoint = getEndpoint()
    region = getRegion()
    table = 'previousSongs'

    if(endpoint):
        dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
    else:
        dynamodb = boto3.resource('dynamodb', region_name=region)

    table = dynamodb.Table(table)

    table.delete()

    print("Table deleted.")


#createTable("madonnaSongs", "eu-west-2", "http://localhost:8000")
#createTable("madonnaSongs", "eu-west-2", "http://localhost:8000")

#createTable2("madonnaSongsTable2", "eu-west-2", "http://localhost:8000")

#createPreviousSongsTable()

#deletePreviousSongsTable()

createPreviousSongsTable()


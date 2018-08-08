from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


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


def deleteTable(table, region, endpoint = '' ):

    if(endpoint):
        dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
    else:
        dynamodb = boto3.resource('dynamodb', region_name=region)

    table = dynamodb.Table(table)

    table.delete()

    print("Table deleted.")


def putItem(table, region, userID, endpoint = '' ):

    if(endpoint):
        dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
    else:
        dynamodb = boto3.resource('dynamodb', region_name=region)

    table = dynamodb.Table(table)

    response = table.put_item(
        Item={
            'userID': userID,
                    'info': {
                        'songsSoFar':"Vogue etc.",
                        'songCount': decimal.Decimal(0)
                    }
            }
        )

    print("PutItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))

def getItem(table, region, userID, endpoint = ''):

    if(endpoint):
        dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
    else:
        dynamodb = boto3.resource('dynamodb', region_name=region)

    table = dynamodb.Table(table)

    try:
        response = table.get_item(
            Key={
                'userID': userID
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem succeeded:")
        print(json.dumps(item, indent=4, cls=DecimalEncoder))


def queryItem(table, region, userID, endpoint = '' ):

    if(endpoint):
        dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
    else:
        dynamodb = boto3.resource('dynamodb', region_name=region)

    table = dynamodb.Table(table)

    response = table.query(
        KeyConditionExpression=Key('userID').eq(userID)
    )

    for i in response['Items']:
        print(i['userID'])

    print(response['Items'])

    return(response['Items'])


def deleteItem(table, region, userID, endpoint = ''):

    if(endpoint):
        dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
    else:
        dynamodb = boto3.resource('dynamodb', region_name=region)

    table = dynamodb.Table(table)

    response = table.delete_item(
        Key={
            'userID': userID,
        }
    )

    print(json.dumps(response, indent=4, cls=DecimalEncoder))

def updateItem(table, region, userID, songs, dayCount, endpoint = '' ):

    if(endpoint):
        dynamodb = boto3.resource('dynamodb', region_name=region, endpoint_url=endpoint)
    else:
        dynamodb = boto3.resource('dynamodb', region_name=region)

    table = dynamodb.Table(table)

    userID = userID

    response = table.update_item(
        Key={
            'userID': userID,
        },
        UpdateExpression="set info.songsSoFar = :s, info.songCount=:c",
        ExpressionAttributeValues={
            ':c': decimal.Decimal(dayCount),
            ':s': songs
        },
        ReturnValues="UPDATED_NEW"
    )

    print("UpdateItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))


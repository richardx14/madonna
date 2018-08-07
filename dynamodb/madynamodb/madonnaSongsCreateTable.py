from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2', endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='madonnaSongs',
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
from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('madonnaSongs')

table.delete()
import boto3
import json


print "Getting bucket list from Account"

s3 = boto3.resource('s3')
rs = boto3.client('redshift')
client = boto3.client('support')

response = client.describe_trusted_advisor_checks (language='en')
json.dumps(response)

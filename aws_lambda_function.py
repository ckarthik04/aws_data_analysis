from __future__ import print_function
import json
import boto3
import time
import urllib

print('Loading function')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
    try:
        print("Using waiter to wait for object to persist thru s3 service")
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=bucket, Key=key)
        response = s3.head_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        print("ETag: " + response['ETag'])
        print("Content-Length: ", response['ContentLength'])
        print("Keyname: " + key)
        print("Copying object" + key)
        copy_source = {'Bucket': bucket, 'Key': key}
        target_bucket = u'transformed-weather-data'
        s3.copy_object(Bucket=target_bucket, Key=key, CopySource=copy_source)
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist '
              'and your bucket is in the same region as this '
              'function.'.format(key, bucket))
        raise e
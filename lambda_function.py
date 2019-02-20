import json
import boto3


def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key =    event['Records'][0]['s3']['object']['key']

    sns = boto3.client('sns')
    sns.publish(
        TopicArn = 'arn:aws:sns:us-east-1:340297255339:File-Upload-Notification',
        Subject = 'File uploaded: ' + key,
        Message = 'File was uploaded to bucket: ' + bucket
    )
    

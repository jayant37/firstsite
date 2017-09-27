import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAILV5SCOK4BELEQHQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'www.thinkinnovative.tk'

data = open('bitmoji.png', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='bitmoji.png', Body=data)

print ("Done")

http://www.thinkinnovative.tk.s3-website.ap-south-1.amazonaws.com/
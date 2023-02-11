import json
import boto3
from botocore.exceptions import ClientError
from config import ACCESS_KEY_ID, SECRET_ACCESS_KEY, BUCKET_NAME

s3 = boto3.resource(
    service_name='s3',
    region_name='eu-central-1',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY
)


json.load_s3 = lambda f: json.load(s3.Bucket(BUCKET_NAME).Object(key=f).get()["Body"])
json.dump_s3 = lambda obj, f: s3.Bucket(BUCKET_NAME).Object(key=f).put(Body=json.dumps(obj))


def file_exists(filepath):
    try:
        json.load_s3(filepath + '.json')
        return True
    except ClientError:
        return False
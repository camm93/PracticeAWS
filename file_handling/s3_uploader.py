import boto3
import os
from dotenv import load_dotenv
from settings import log

load_dotenv()


DATA_FOLDER = "files/"
AWS_USER_NAME = os.getenv("AWS_USER_NAME")
AWS_BUCKET = os.getenv("AWS_BUCKET")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

client = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)


for file_ in os.listdir(DATA_FOLDER):

    if file_.endswith('.py'):
        folder = "python/"
    elif file_.endswith('.js'):
        folder = "javascript/"
    elif file_.endswith('.json'):
        folder = "json/"
    else:
        folder = "text/"
    
    upload_file_key = folder + file_

    try:
        client.upload_file(DATA_FOLDER + file_, AWS_BUCKET, upload_file_key)
        log.info("Successfully uploaded {0}".format(upload_file_key))
    except Exception as e:
        log.error("An exception has occurred while uploading {}. {}".format(upload_file_key, e))

from PIL import Image
import boto3
import io

AWS_ACCESS_KEY=''
AWS_SECRET_KEY=''
AWS_REGION=''
BUCKET_NAME = ''



object_key = 'test/test.jpg'

base_image = "man.jpg"

orginal = Image.open(base_image).convert("RGBA")
byte_arr = io.BytesIO()
orginal.save(byte_arr, format = "PNG")

s3 = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_KEY,
    region_name = AWS_REGION
)

res = s3.upload_fileobj(io.BytesIO(byte_arr.getvalue()), Bucket = BUCKET_NAME, Key = object_key)



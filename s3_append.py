import boto3

AWS_ACCESS_KEY=''
AWS_SECRET_KEY=''
AWS_REGION='ap-south-1'
BUCKET_NAME = 'face-checkin-2025'

OBJECT_KEY = 'test/test.jpg'

rekognition = boto3.client(
    'rekognition',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

response = rekognition.detect_faces(
    Image={
        'S3Object': {
            'Bucket': BUCKET_NAME,
            'Name': OBJECT_KEY
        }
    },
    Attributes=['ALL']
)

if response['FaceDetails']:
    print("Face detected")
else:
    print("No face detected")

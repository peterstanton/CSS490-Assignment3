import boto3
import os
from botocore.client import ClientError


# The bucket does not exist or you have no access.

# https://stackoverflow.com/questions/26871884/how-can-i-easily-determine-if-a-boto-3-s3-bucket-resource-exists

def recurse(s3, new_bucket, full_path):
    for root, dirs, files in os.walk(full_path):
        # String gets current local path
        curDir = root + '\\'

        for file in files:
            # upload file to bucket.
            s3.Object(new_bucket, "Backup/" + file).put(Body=open(curDir + file, "rb"))
            #                           should concatenate in path
        # Loop through present direectories, should move up ABOVE the for loop, loop through dirs calling recurse.
    pass


s3 = boto3.resource("s3")

buckets = s3.buckets.all()
for bucket in buckets:
    print(bucket.name)

newBucket = input("new bucket name ")
print("Creating bucket: ", newBucket)
try:
    s3.meta.client.head_bucket(Bucket=bucket.name)
except ClientError:
    s3.create_bucket(Bucket=newBucket, CreateBucketConfiguration={"LocationConstraint": "us-west-1"})

bucketName = newBucket
fullPath = input("Input directory path ")

recurse(s3, bucketName, fullPath)

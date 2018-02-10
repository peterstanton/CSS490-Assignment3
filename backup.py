import boto3
import os


def recurse(s3, newBucket, fullPath):

    for root, dirs, files in os.walk(fullPath):
        # replace below with stuff I actually need to do.
        for file in files:
            # upload file to bucket.
            s3.Object(newBucket, "Backup/" + file).put(Body=open(fullPath + file, "rb"))
        # create next folder(s).
    pass


s3 = boto3.resource("s3")

buckets = s3.buckets.all()
for bucket in buckets:
    print(bucket.name)

newBucket = input("new bucket name")
print("Creating bucket: ", newBucket)
s3.create_bucket(Bucket=newBucket, CreateBucketConfiguration={"LocationConstraint": "ap-oregon-1"})

bucketName = newBucket
fullPath = input("Input directory path")

recurse(s3, newBucket, fullPath)

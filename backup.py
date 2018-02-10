import boto3
import os


def recurse(s3, new_bucket, full_path):
    for root, dirs, files in os.walk(full_path):
        for file in files:
            # upload file to bucket.
            s3.Object(new_bucket, "Backup/" + file).put(Body=open(full_path + file, "rb"))
            # s3.Object(existingbucket, "hello/" + filename).put(Body=open(fullpath + filename, "rb"))
            #                           should concatenate in path
        # create next folder(s).
    pass


s3 = boto3.resource("s3")

buckets = s3.buckets.all()
for bucket in buckets:
    print(bucket.name)

newBucket = input("new bucket name")
print("Creating bucket: ", newBucket)
s3.create_bucket(Bucket=newBucket, CreateBucketConfiguration={"LocationConstraint": "us-west-1"})

bucketName = newBucket
fullPath = input("Input directory path")

recurse(s3, bucketName, fullPath)

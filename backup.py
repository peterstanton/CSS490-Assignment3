import boto3
import os

# The bucket does not exist or you have no access.

# https://stackoverflow.com/questions/26871884/how-can-i-easily-determine-if-a-boto-3-s3-bucket-resource-exists

# I need a way to preserve folder structure by appending stuff to backup.

def recurse(s3, new_bucket, full_path):
    for root, dirs, files in os.walk(full_path):
        curpath = root + '\\'
        curdir = os.path.basename(os.path.normpath(curpath))

        for dir in dirs:
            recurse(s3, new_bucket, curpath + dir)

        for file in files:
            s3.Object(new_bucket, "Backup/" + curdir + '/' + file).put(Body=open(curpath + file, "rb"))
            #                           should concatenate in path
        # Loop through present direectories, should move up ABOVE the for loop, loop through dirs calling recurse.
    pass


s3 = boto3.resource("s3")

buckets = s3.buckets.all()
for bucket in buckets:
    print(bucket.name)

newBucket = input("new bucket name ")
print("Creating bucket: ", newBucket)
s3.create_bucket(Bucket=newBucket, CreateBucketConfiguration={"LocationConstraint": "us-west-1"})

bucketName = newBucket
fullPath = input("Input directory path ")

recurse(s3, bucketName, fullPath)

import boto3
import os
from boto3 import Session

# https://stackoverflow.com/questions/26871884/how-can-i-easily-determine-if-a-boto-3-s3-bucket-resource-exists
# https://stackoverflow.com/questions/7872611/in-python-what-is-the-difference-between-pass-and-return
# Thanks to Roman Zhang for helping me understand Session objects in boto3.


def recurse(s3, new_bucket, full_path, old_dir):
    for root, dirs, files in os.walk(full_path):
        curpath = root + '\\'
        curdir = old_dir + os.path.basename(os.path.normpath(curpath))

        for thisdir in dirs:
            parser = old_dir + '/' + os.path.basename(curdir)
            recurse(s3, new_bucket, curpath + thisdir, parser.replace('//', '/') + '/')

        for file in files:
            print("Uploading: " + curdir + '/' + file)
            s3.Object(new_bucket, curdir + '/' + file).put(Body=open(curpath + file, "rb"))
        return
    return


def getsession():
    return Session(aws_access_key_id=input("Enter your AWS access key ID: "),
                   aws_secret_access_key=input("Enter your AWS secret key: "),
                   region_name=input("Enter the AWS region you wish to use, try us-west-1: "))


mysession = getsession()
s3 = mysession.resource("s3")
buckets = s3.buckets.all()

print("These are your account's current S3 buckets: ")
print("---------------------------------------------")
for bucket in buckets:
    print(bucket.name)

newBucket = input("Enter the name of a bucket to use for backing up: ")
print("Creating bucket: ", newBucket)
try:
    s3.create_bucket(Bucket=newBucket, CreateBucketConfiguration={"LocationConstraint": mysession.region_name})
except:
    print("This bucket already exists, continuing with existing bucket.")

bucketName = newBucket
fullPath = input("Input directory path for backup do NOT end with a /: ")
recurse(s3, bucketName, fullPath, "Backup/")
input("Press enter to exit.")

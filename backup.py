import boto3
import os


# https://stackoverflow.com/questions/26871884/how-can-i-easily-determine-if-a-boto-3-s3-bucket-resource-exists

# https://stackoverflow.com/questions/7872611/in-python-what-is-the-difference-between-pass-and-return

def recurse(s3, new_bucket, full_path, old_dir):
    for root, dirs, files in os.walk(full_path):
        curpath = root + '\\'
        curdir = old_dir + os.path.basename(os.path.normpath(curpath))

        for dir in dirs:
            parser = old_dir + '/' + os.path.basename(curdir)
            recurse(s3, new_bucket, curpath + dir, parser.replace('//', '/') + '/')

        for file in files:
            s3.Object(new_bucket, curdir + '/' + file).put(Body=open(curpath + file, "rb"))
            #                           should concatenate in path
        # Loop through present direectories, should move up ABOVE the for loop, loop through dirs calling recurse.
        return
    return


s3 = boto3.resource("s3")

buckets = s3.buckets.all()
for bucket in buckets:
    print(bucket.name)

newBucket = input("new bucket name ")
print("Creating bucket: ", newBucket)
try:
    s3.create_bucket(Bucket=newBucket, CreateBucketConfiguration={"LocationConstraint": "us-west-1"})
except:
    print("This bucket already exists.")

bucketName = newBucket
fullPath = input("Input directory path ")

recurse(s3, bucketName, fullPath, "Backup/")

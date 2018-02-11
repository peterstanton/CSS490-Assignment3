CSS-490 backup application
======
This program uses Amazon Web Services' API to backup a given directory to a S3 bucket.
 
#### Does not work on
* Non-Windows file systems due to processing directories with Window path conventions.
* Gibberish file locations.
* S3 buckets not owned by the user.
* IAM users without at least S3 full access security policy.

#### Assumptions
* Empty folders are not meaningful and can be disregarded. They will be created by AWS if a file is added at their leaf and the backup
is subsequently run.
 
## How-to use this code
* Ensure you have at least Python 3.6 installed and configured in your PATH.
* Ensure you have the Boto3 package installed.
* Ensure you have an IAM user with S3 access and the credentials accessible.
* Navigate to the directory where backup.py is located.
* Run the program from terminal with "python backup.py", or double-click executable.bat
* Enter your access key ID and secret access key in when prompted.
* Enter a valid AWS service region.
* Enter a valid, formatted URI of the form, "C:\Users\Peter\Documents". Do not end the path with a slash.
* Watch as all files in the folder are recursively uploaded.

## Known bugs
* Due to issues with pyinstaller not being compatible with Windows 10, I could not generate a working .exe.
 
## Dependencies
* Python 3.6.4, or higher.
* Boto3 1.4.8, or higher.
* Properly configured PATH variable to run Python 3.6.4 from a command prompt.
* Usable AWS account.
* Properly configured IAM credentials.

## Sources
* https://stackoverflow.com/questions/26871884/how-can-i-easily-determine-if-a-boto-3-s3-bucket-resource-exists
* https://stackoverflow.com/questions/7872611/in-python-what-is-the-difference-between-pass-and-return
* Thanks to Roman Zhang for helping me understand Session objects in boto3.

Functionality based on Boto3 documentaiton:


https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html 
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html

Description: 

This python/flask app uses AWS SDK Python methods to upload / download / list files to&from an S3 bucket. 

Prerequisites:

 Python 3,
 Pipenv,
 AWS CLI Tool,
 Git
 
 To run:
 
 aws configure
 
 pip install -r requirements.txt
 
 python3 app.py
 
 Note:
 
 In app.py change (line 10) the BUCKET = "add_bucket_name" to match your bucket name.  
 
 
 Go to: http://localhost:5000/storage

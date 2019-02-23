# aws_data_analysis

The raw weather data is brought from the amazon s3 public bucket to the target s3 bucket
using AWS CLI option. The AWS CLI can also be used to bring the data from our source
S3 bucket to the EC2 instance location. The other method that was used to ensure that if
there are any new files that come in the source bucket have to be moved to target bucket
for the validation, transformation and prediction purpose is to use lambda function along
with python (boto3). The data is then can be used directly for prediction with the help of
python/spark modules which can be run in the EC2-EMR instance. The python and
anaconda packages along with jupyter notebooks are installed in an EC2-EMR instance
(AMAZON linux AMI machine). The data which is present in the ec2 instance is then read
through the python scripts (run through jupyter notebooks) and using iris packages we
are able to model and visualize the data along with transformation techniques. The source
data can also be converted to csv files in the source s3 bucket and amazon quicksight
can be used to visualize and analyze the data. Based on the forecast time period and
data available we can predict the future data points.

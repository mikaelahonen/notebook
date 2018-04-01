Setup the server
* Tranfer files to user's home dir
* chmod 755 setup-1.sh setup-2.sh
* ./setup-1.sh
* Exit and start new SSH session
* ./setup-2.sh

The security group for EC2
* Allow all from port 22
* Allow VPC CIDR from port 80

Create an execution role for lambda
* Create a role e.g. `lambda_proxy` from `IAM`
* Set policies `AWSLambdaVPCAccessExecutionRole` and `CloudWatchEventsFullAccess`

Deploy lambda function
* `pip install requests -t ./lambda_deploy`
* Copy `lambda.py` to lambda deploy directory
* Make zip from `lambda_deploy` <b>content</b>, not the top folder

Create lambda function
* Create function `api_gateway_proxy`
* Rename the module to `app.py`
* Copy code from `lambda.py` to `app.py`
* Set the handler to `app.request_handler`
* Set `lambda_proxy` as the role
* Set same VPC, subnet and security group than the EC2 instance

Setup API Gateway
* Create new API Gateway.
* Create new resource
* Tick the proxy box
* Integration type: `Lambda function`
* The same region than lambda
* Lambda function: `api_gateway_proxy`
* Deploy as `v1`

Testing
* If not working, add or remove slash at the end

[Setup docs on AWS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html).

# AWS Elastic Beanstalk
Deploying a python Flask application to AWS Elastic Beanstalk service.

[Documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html).

## Set up
1. Create new app
2. Create new environment (usually test and production)
3. Platform > Preconfigured platform > Preconfigured > Python
  * Installs python 3.6
  * Choose the sample application

## Upload your code
Select `application.py` and `requirements.txt` and compress them to a zip file. Upload it to AWS Elastic Beanstalk. Both file names and also the variable called `application` in `application.py` are important for Beanstalk.

## Configure HTTPS
Configuring secured HTTPS connection requires your own domain name.

1. If needed, set the NS records in the web host where your domain has been purchased.
2. Create alias domain to Amazon Route 53 and point it to the Beanstalk application.
3. Apply certificate for your domain.
4. Set up a Load balancer from beanstalk console from
  * From your environment go to Configuration > Load balancer.
  * Disable the default listener.
  * Create new listener with port 443 (HTTPS) and instance port 80 (HTTP). Select the certificate.

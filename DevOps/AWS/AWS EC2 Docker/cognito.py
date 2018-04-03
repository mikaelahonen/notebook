import boto3

client = boto3.client('cognito-identity')
response = client.get_credentials_for_identity(
    IdentityId='eu-west-1_H5mb08BMU',
    Logins={
        'string': 'string'
    },
    CustomRoleArn='string'
)

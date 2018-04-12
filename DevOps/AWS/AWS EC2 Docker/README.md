# Back-end

## AWS Cognito
### General settings
* Create a new user pool
* Create an app client
* Create a user

### App integration
* Setup the `Callback URL(s)`
* From Allowed OAuth Flows allow `Authorization code grant`
* From Allowed OAuth Scopes allow all.

### Federated identities

### Javascript SDK
AWS Amplify is recommended.

### Explicit flow
Recommended way if explicit or implicit should be chosen.

Step 1: Get auth code
* Get the code from `/oauth2/authorize` endpoint from browser.
* Example uri: https://webapp.auth.eu-west-1.amazoncognito.com/oauth2/authorize?client_id=46bf3oa91k0ff16vduo7lolv82&response_type=code&redirect_uri=https://app.mikaelahonen.com/login/

Step 2: Get token
* Get the tokens from `/oauth2/token` endpoint by the application code.
* Example uri (post method): https://webapp.auth.eu-west-1.amazoncognito.com/oauth2/token?code=7080bdc3-6e6f-4092-6201-7feaa5d01902&client_id=46bf3oa91k0ff16vduo7lolv82&redirect_uri=https://app.mikaelahonen.com/login/&grant_type=authorization_code

Step 3: Refresh token


### Implicit flow
This doesn't offer a method to refresh the token.
* Example uri: `https://webapp.auth.eu-west-1.amazoncognito.com/login?response_type=token&client_id=46bf3oa91k0ff16vduo7lolv82&redirect_uri=https://app.mikaelahonen.com/authorize/`
* The token will be in query parameters in redirect page.
* Use the whole `id_token` to authorize against API gateway.


[Token explained](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html).

[Cognito Javascript examples](https://docs.aws.amazon.com/cognito/latest/developerguide/using-amazon-cognito-user-identity-pools-javascript-examples.html).

## EC2

### Launch the instance
* Choose `Amazon Linux AMI`
*

### The security group for EC2
* Allow all from port 22
* Allow VPC CIDR from port 80

### Download a key
* Download a new or an existing SSH key
* Convert to `.ppk` in `PuTTY Key Generator`
* Click `load` and select the `.pem` file
* Click `Save private key`

### Connect the EC2
Connect by PuTTY.

### Setup the server
* Tranfer files to user's home dir
* `chmod 755 setup-1.sh setup-2.sh`
* `./setup-1.sh`
* Exit and start new SSH session
* `./setup-2.sh`

## Lambda
### Create an execution role for lambda
* Create a role e.g. `lambda_proxy` from `IAM`
* Set policies `AWSLambdaVPCAccessExecutionRole` and `CloudWatchEventsFullAccess`

### Deploy lambda function
* `pip install requests -t ./lambda_deploy`
* Copy `.py` files to `lambda_deploy` directory
* Make zip from `lambda_deploy` <b>content</b>, not the top folder

### Create lambda function
* Create function `api_gateway_proxy`
* Rename the module to `app.py`
* Copy code from `lambda.py` to `app.py`
* Set the handler to `app.request_handler`
* Set `lambda_proxy` as the role
* Set same VPC, subnet and security group than the EC2 instance

## API Gateway
Create new API Gateway.
It might take a short while that changes will be applied.

### Autorizers
* Create a cognito authorizer from `Authorizers`
* Set header `Authorization`

### Setup resources
* Select Cognito to request authorizer
* Create new resource
* Tick the proxy box
* Integration type: `Lambda function`
* The same region than lambda
* Lambda function: `api_gateway_proxy`

### CORS
* Click Actions > Enable CORS
* Accept the default settings
* When using `ANY` method, response header `Access-Control-Allow-Origin`
should be set to `'*'` on server side anyway.
[Docs: CORS with Api Gateway and lambda](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors.html).

### Deploy
* Deploy as `v1`

### Mock
Set `Mock` as an integration type to imitate server response.
Set any response text you want from
`Integration response` > `200` > `Body Mapping templates`.

## Testing
* If Flask is not working, add or remove slash at the end


[Setup docs on AWS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html).

# Front-end

## Install nodejs server
Install nodejs

## Install react
Install create-react-app.

Run `npx create-react-app some-name-for-app`

Install additional libraries with `npm install -s some-library-name`.

## React router
[React router tutorial](https://medium.com/@pshrmn/a-simple-react-router-v4-tutorial-7f23ff27adf).

1. `npm install -s react-router-dom` (for websites)
2. In `index.js` module `import { BrowserRouter, Route, Switch } from 'react-router-dom'`

Sample code
```js
ReactDOM.render((
  <BrowserRouter>
    <Switch>
      <Route exact path='/' component={App}/>
      <Route path='/page-1' component={Page1}/>
    </Switch>
  </BrowserRouter>
), document.getElementById('root'));
```

## React-bootstrap
1. Include bootstrap `css` to `index.html` in `public` folder.
2. import module like `import { Button } from 'react-bootstrap';`.

## AWS Amplify
Amplify stores tokens to local storage.

1. `npm install -s aws-amplify`
2. Configure `Amplify.config()` anywhere before executing.
3. Use for example `Auth.currentAuthenticatedUser()` method to define weather user have signed in.

[AWS Amplify Auth examples](https://aws.github.io/aws-amplify/media/authentication_guide).

## API calls

## Organize directories

## S3 Hosting
Create an AWS S3 bucket.

Go to Properties
* Enable `Versioning` (for cloud front cache).
* Enable `Static website hosting`
* Set `index.html` as `Index document`

Go to Permissions
* Grant public read access to the bucket objects: [Docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html).

## Deploy react
1. Go to the directory react app.
2. `npm run build`.
3. Go to `build` folder and upload the contents to the S3 bucket.
4. Test the website by visting the S3 website url.

## CloudFront Distribution

CloudFront is used to enable `HTTPS` and efficient file distribution.

### Instructions
1. Create distribution
2. Choose `Web`
3. In `Origin domain name` choose your S3 bucket
4. Leave `Origin Path` empty to include all files
5. `Restrict Bucket Access`: `Yes`.
6. `Origin Access Identity`: `Create new identity`
7. `Grant Read Permissions on Bucket`: `Yes, Update Bucket Policy`
8. Define `Default Root Object` explicitly to `index.html`.

### Test
* Wait for distribution to be created.
* Paste the domain name to browser's address bar.

import config
import requests

def get_route_url(event):

    #Get the full request path
    path = event["requestContext"]["path"]

    #Parse stage and the first resource
    path_list = path.split("/")
    #First item of the list is empty, because of the starting slash /
    stage = path_list[1]
    resource = path_list[2]

    #Host, port and path
    host = config.route_table[stage][resource]["host"]
    port = config.route_table[stage][resource]["port"]
    path = event["requestContext"]["path"]

    #Create url for the request
    url = "{}:{}{}".format(host, port, path)

    print("Url: " + url)

    return url

def do_request(event, url):

    #Http method
    method = event["httpMethod"]

    #Query parameters
    if event["queryStringParameters"]:
        params = event["queryStringParameters"]
    else:
        params = {}

    #Body
    if event["body"]:
        data = event["body"]
    else:
        data = ""

    #Headers
    headers = event["headers"]
    headers["X-Cognito-User"] = event["requestContext"]["identity"]["user"]

    #Get response object
    print("Start request")
    response_obj = requests.request(
        method=method,
        headers=headers,
        url=url,
        data=data,
        params=params
    )
    print("End request")

    # Reponse in HTTP format
    response = {
        "statusCode": response_obj.status_code,
        "body": response_obj.text,
        "headers": {
            #"Content-Type": response_obj.headers["Content-Type"],
            #"Content-Length": response_obj.headers["Content-Length"],
            #"Date": response_obj.headers["Date"]
            "Access-Control-Allow-Origin": "*"
        }
    }


    return response

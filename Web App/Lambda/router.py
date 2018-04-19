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
    url = "http://{}:{}{}".format(host, port, path)

    print("Url: " + url)

    return url

def do_request(event, url):

    #Request variables
    method = event["httpMethod"]
    data = {
        "body": event["body"],
        "event": event
    }
    params = event["queryStringParameters"]
    data = event["body"]

    #Headers
    headers = event["headers"]
    headers["X-Cognito-User"] = event["requestContext"]["identity"]["user"]

    #Get response object
    response_obj = requests.request(
        method=method,
        headers=headers,
        url=url,
        data=data,
        params=params
    )

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

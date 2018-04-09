default_host = "http://ec2-34-243-58-167.eu-west-1.compute.amazonaws.com"

route_table = {
    "data": {
        host: default_host
        port: "80",
    },
    "static-content": {
        host: default_host,
        port: "4001",
    },
}

def route_resource(event):

    #Use the first part of path as route resource
    resources = event.path.split("/")
    resource_to_route = resources[0]
    
    return resource_to_route

def request_url(event, resource):

    #Host and path
    host = route_table[resource]["host"]
    port = route_table[resource]["port"]
    stage = event["requestContext"]["stage"]
    path = event["path"]
    url = host + ":" + port + "/" + stage + path

    return url

def do_request(event, url):

    #Request variables
    method = event["httpMethod"]
    data = {
        "body": event["body"],
        "event": event
    }
    params = event["queryStringParameters"]
    headers = event["headers"]

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
            "Content-Type": response_obj.headers["Content-Type"],
            "Content-Length": response_obj.headers["Content-Length"],
            "Date": response_obj.headers["Date"]
        }
    }

    return response

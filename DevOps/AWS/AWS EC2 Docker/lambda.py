import requests

def request_handler(event, context):

    #Host and path
    host = "http://ec2-34-243-58-167.eu-west-1.compute.amazonaws.com"
    port = "80"
    stage = event["requestContext"]["stage"]
    path = event["path"]
    url = host + ":" + port + "/" + stage + path

    #Other variables
    method = event["httpMethod"]
    headers = event["headers"]
    data = {
        "body": event["body"],
        "event": event
    }
    params = event["queryStringParameters"]

    #Request
    resp_container = requests.request(
        method=method,
        headers=headers,
        url=url,
        data=data,
        params=params
    )

    # Reponse
    resp_proxy = {
        "statusCode": resp_container.status_code,
        "body": resp_container.text,
        "headers": {
            "Content-Type": resp_container.headers["Content-Type"],
            "Content-Length": resp_container.headers["Content-Length"],
            "Date": resp_container.headers["Date"]
        }
    }

    #Return
    return resp_proxy

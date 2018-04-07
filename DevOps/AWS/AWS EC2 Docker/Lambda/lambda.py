import config

def api_router(event, context):

    #Get a resource to route
    route = config.route_resource(event)

    #Generate url from host and port according to the route table
    url = config.route_url(event, route)

    #Make a request and get the response
    response = config.do_request(event, url)

    #Return
    return response

import router
import json

def api_router(event, context):

    #Log the event
    print(json.dumps(event))

    #Generate url from host and port according to the route table
    url = router.get_route_url(event)

    #Make a request and get the response
    response = router.do_request(event, url)

    #Return
    return response

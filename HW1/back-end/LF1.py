import json
from botocore.vendored import requests
from urllib.parse import quote

API_KEY = ''

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'


def request(host, path, api_key, url_params=None):

    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    # print(u'Querying {0} ...'.format(url))
    response = requests.request('GET', url, headers=headers, params=url_params)
    shortresponse = response.json()["businesses"][0:3]
    res = []
    count = 1
    for e in shortresponse:
        temp = []
        temp.append(str(count) + ".")
        temp.append(e["name"])
        temp.append(e["location"]["address1"])
        res.append(temp)
        count += 1
    # print(json.dumps(res, indent=1))
    print(res)
    return res


def lambda_handler(event, context):
    # print ("111111", event)

    response = {"dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Message to convey to the user."
                }
    }
    }
    # print ("response", response)

    return dispatch(event)


def dispatch(event):
    # print ("event", event)
    intent = event['currentIntent']['name']
    # print ("intent", intent)

    if intent == "GreetingIntent":
        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Hi there, how can I help?"
                }
            }
        }

    elif intent == "ThankIntent":
        return {"dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "You are more than welcome"
                }
                }
                }

    elif intent == "DiningSuggestionIntent":
        slot = event['currentIntent']['slots']
        location = slot['Location']
        foodtype = slot["FoodType"]
        people = slot['People']
        date = slot['Date']
        time = slot['Time']
        url_params = {}
        url_params['location'] = location
        url_params['term'] = foodtype
        response = request(API_HOST, SEARCH_PATH, API_KEY, url_params)
        return {"dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Here are my {} restaurant suggestion for {} people, for {} at {}: {} {}, located at {}; {} {}, located at {}; {} {}, located at {}. Enjoy your meal!".format(foodtype, people, time, date, response[0][0], response[0][1], response[0][2], response[1][0], response[1][1], response[1][2], response[2][0], response[2][1], response[2][2])
                }
                }
                }
    else:
        return {"dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "I cannot give you restaurant suggestion."
                }
                }
                }

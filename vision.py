import requests
import json
def prediction(s):
    url = 'https://api-us.restb.ai/vision/v2/multipredict'
    payload = {
        # Add your client key
        'client_key': '18d2c3def97f08eee4261f6dbe69c2081a4535166e48f116d38c17303f5b3a39',
        'model_id': 're_roomtype_global_v2,re_features_v3,re_appliances_v2,re_condition',
        # Add the image URL you want to classify
        'image_url': s
    }

    # Make the classify request
    response = requests.get(url, params=payload)

    # The response is formatted in JSON
    json_response = response.json()
    house_part = json_response['response']['solutions']['re_roomtype_global_v2']['top_prediction']['label']
    mark = json_response['response']['solutions']['re_condition']['score']
    json_object = json.dumps(json_response, indent = 4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    return (house_part, mark) 


    
    #print(json_object[1])
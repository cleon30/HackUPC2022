import base64
import requests
import json
def prediction(path):
    client_key="18d2c3def97f08eee4261f6dbe69c2081a4535166e48f116d38c17303f5b3a39"
    url = f"https://api-eu.restb.ai/vision/v2/multipredict?client_key={client_key}"
    with open(path, "rb") as image_file:
        image_base64 = base64.urlsafe_b64encode(image_file.read())
    payload = {
        # Add your client key
        'image_base64': image_base64,
        'model_id': 're_roomtype_global_v2,re_features_v3,re_appliances_v2,re_condition',
    }
    files=[
    ]

    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    
    # Make the classify request

    # The response is formatted in JSON
    json_response = response.json()
    house_part = json_response['response']['solutions']['re_roomtype_global_v2']['top_prediction']['label']
    mark = json_response['response']['solutions']['re_condition']['score']
    json_object = json.dumps(json_response, indent = 4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    return (house_part, mark) 


    
    #print(json_object[1])
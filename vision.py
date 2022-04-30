import base64
import requests
import json
def prediction(path):
    client_key="256fa7c3b7da99373032e42d0d9398e216e6b10021fbe0e8af6fe2bdedd992fa"
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
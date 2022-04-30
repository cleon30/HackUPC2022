import requests
import json
def details(s, path):
    url = 'https://api-us.restb.ai/vision/v2/multipredict'
    key = '18d2c3def97f08eee4261f6dbe69c2081a4535166e48f116d38c17303f5b3a39'
    if s == 'kitchen':
        payload = {
        # Add your client key
        'client_key': key,
        'model_id': 're_kitchen_finishes',
        # Add the image URL you want to classify
        'image_base64': path
        }
    if s=='bathroom':
        payload = {
        # Add your client key
        'client_key': key,
        'model_id': 're_bathroom_features',
        # Add the image URL you want to classify
        'image_base64': path
        }

    # Make the classify request
    response = requests.get(url, params=payload)

    # The response is formatted in JSON
    json_response = response.json()
    json_object = json.dumps(json_response, indent = 4)
    with open("sample_details.json", "w") as outfile:
        outfile.write(json_object)
    return  


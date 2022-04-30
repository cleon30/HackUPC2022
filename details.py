import requests
import json
import base64
def details(s, path):
    client_key="256fa7c3b7da99373032e42d0d9398e216e6b10021fbe0e8af6fe2bdedd992fa"
    url = f"https://api-eu.restb.ai/vision/v2/multipredict?client_key={client_key}"
    with open(path, "rb") as image_file:
        image_base64 = base64.urlsafe_b64encode(image_file.read())
    if s == 'kitchen':
        payload = {
        # Add your client key
        'image_base64': image_base64,
        'model_id': 're_kitchen_finishes',
        }
    if s=='bathroom':
        payload = {
        # Add your client key
        'image_base64': image_base64,
        'model_id': 're_bathroom_features',
        }
    # Make the classify request
    files=[
    ]

    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    # The response is formatted in JSON
    json_response = response.json()
    json_object = json.dumps(json_response, indent = 4)
    with open("sample_details.json", "w") as outfile:
        outfile.write(json_object)
    return  


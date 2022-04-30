from fastapi import FastAPI
import json
app = FastAPI()


@app.get("/room")
async def room():
    with open('../sample_details.json') as json_file:
        data = json.load(json_file)
    return data["room"]
@app.get("/score")
async def score():
    with open('../sample_details.json') as json_file:
        data = json.load(json_file)
    return data["score"]
@app.get("/objects")
async def objects():
    with open('../sample_details.json') as json_file:
        data = json.load(json_file)
    return data["objects"]
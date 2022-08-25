import json
from fastapi import APIRouter

router = APIRouter()

tags = ["ml"]

@router.get(f"/ml/get/urls")
async def get_urls():
    with open("data/ml.json") as reader:
        data = json.load(reader)
    return data

@router.get("/ml/get/url/{name}")
async def get_url(name):
    with open("data/ml.json") as reader:
        data = json.load(reader)
        return data.get(name, None)
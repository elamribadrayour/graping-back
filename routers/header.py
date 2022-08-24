import json

from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi.responses import FileResponse

router = APIRouter()

tags = ["header"]


@router.get(f"/header/get/tabs")
async def get_tabs():
    with open("data/tabs.json") as reader:
        data = json.load(reader)
    return data

@router.get(f"/header/get/logo")
async def get_logo():
    return FileResponse("data/images/logo.png")
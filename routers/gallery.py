import os
import base64
from unittest import result

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

tags = ["gallery"]

@router.get("/gallery/get/image/{filename}")
async def get_image(filename):
    print(filename)
    if os.path.exists(f"data/gallery/images/{filename}"):
        return FileResponse(f"data/gallery/images/{filename}")
    else:
        return None

@router.get("/gallery/get/images/")
async def get_image():
    result = {}
    result["images"] = {}
    filenames = os.listdir("data/gallery/images")
    for filename in filenames:
        filepath = f'data/gallery/images/{filename}'
        encoded = base64.b64encode(open(filepath, "rb").read())
        result["images"][filename] = encoded
    return result
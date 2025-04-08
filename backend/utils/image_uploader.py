import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()
IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")

def upload_image_to_imgbb(image_path):
    with open(image_path, "rb") as file:
        encoded_image = base64.b64encode(file.read())
    response = requests.post(
        "https://api.imgbb.com/1/upload",
        data={
            "key": IMGBB_API_KEY,
            "image": encoded_image
        }
    )
    response.raise_for_status()
    return response.json()["data"]["url"]

# app/api.py
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import os
import uuid
from openai import OpenAI
import base64
from io import BytesIO
import requests
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()

UPLOAD_DIR = "static/images/sketches"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-sketch/")
async def upload_sketch(file: UploadFile = File(...)):
    # Save the uploaded sketch
    file_ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Optional: Open and process the image
    try:
        image = Image.open(file_path).convert("RGB")
       # Convert image to base64
        guess = ask_local_model(image)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

    return {"filename": filename, "ai_guess": guess}


def ask_local_model(image: Image.Image, prompt: str = "What is this sketch?") -> str:
    # Convert image to base64
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # Send to local Ollama server
    payload = {
        "model": "llava",  # or "bakllava"
        "prompt": prompt,
        "images": [image_data],
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        image.close()  # Close the image to free resources
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Error from model: {str(e)}"
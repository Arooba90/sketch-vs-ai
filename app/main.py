# app/main.py
from fastapi import FastAPI
from app.api import router as api_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Sketch vs AI")
app.include_router(api_router)
app.mount("/ui", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def root():
    return {"message": "Welcome to Sketch vs AI!"}

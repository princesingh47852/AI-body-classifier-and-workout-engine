
import os

# Code of main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from workout_engine import router as workout_router

# Initialize the FastAPI app
app = FastAPI(title="SOMA Core Engine API")

# Read allowed frontend URL from environment variable (set this on Render)
# Fallback to localhost for local development
ALLOWED_ORIGIN = os.getenv("ALLOWED_ORIGIN", "https://ai-body-classifier-and-workout-engi.vercel.app")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOWED_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach the workout and nutrition routing logic
app.include_router(workout_router)

@app.get("/")
def health_check():
    return {"status": "SOMA Engine is running normally"}

if __name__ == "__main__":
    import uvicorn
    # Starts the server on port 8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

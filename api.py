from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import cognitive
from db.mongo import db_connection 

app = FastAPI()

# Allow requests from your React app
origins = [
    "http://localhost:5173",  # Adjust this to match your Vite app's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the existing cognitive route
app.include_router(cognitive.router, prefix="/api/cognitive", tags=["Cognitive"])

# Add a /test endpoint to verify the server is running
@app.get("/test")
async def test_server():
    return {"message": "Server is running!"}
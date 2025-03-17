from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Add CORS middleware to allow cross-origin requests

app = FastAPI()
# Allow all origins (not recommended for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI on AWS Amplify!"}


@app.get("/api/data")
async def get_data():
    return {"data": [1, 2, 3, 4, 5]}

from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from openai import OpenAI
from fastapi import Request
from pydantic import BaseModel

load_dotenv()


app = FastAPI()

# Define the origins that are allowed to make requests
origins = [
    "http://localhost:3000",  # React frontend
    "http://127.0.0.1:3000",  # Alternate localhost
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define the request body model
class QueryRequest(BaseModel):
    issue: str
    query: str

# Define a new request model for image description
class ImageDescriptionRequest(BaseModel):
    image_filename: str
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Technical Support Assistant!"}

@app.post("/get_query_response")
def get_query_response(request: QueryRequest):
    client = OpenAI(
        base_url = os.getenv("GENAI_PLATFORM_API_URL"),
        api_key = os.getenv("GENAI_PLATFORM_API_KEY"),
    )
    
    issue = request.issue
    query = request.query

    prompt = "User is facing the below issue: " + issue + ". Here is the query: " + query
    response = client.chat.completions.create(
        model = "n/a",
        messages = [{"role": "user", "content": prompt}],
        extra_body = {"include_retrieval_info": True}
    )

    return {"response": response.choices[0].message.content}

@app.post("/get_image_description")
def get_image_description(request: ImageDescriptionRequest):
    image_url = os.getenv("SPACES_ENDPOINT") + request.image_filename

    openai_api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": image_url}
                },
                {
                    "type": "text",
                    "text": request.query
                }
            ]
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=100,
        stream=False
    )

    content = response.choices[0].message.content
    return {"description": content}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
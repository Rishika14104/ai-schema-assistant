from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SchemaRequest(BaseModel):
    description: str

@app.post("/analyze")
def analyze_schema(request: SchemaRequest):
    
    description = request.description.lower()

    # Simple rule-based logic
    if "user" in description and "order" in description:
        response = {
            "collections": {
                "users": {
                    "_id": "ObjectId",
                    "name": "String",
                    "email": "String"
                },
                "orders": {
                    "_id": "ObjectId",
                    "user_id": "ObjectId (Reference to users)",
                    "product": "String",
                    "amount": "Number"
                }
            },
            "indexes": [
                "Create index on orders.user_id"
            ],
            "justification": "Referencing is used because one user can have many orders."
        }
    else:
        response = {
            "message": "Provide entities like User and Order to generate schema."
        }

    return response
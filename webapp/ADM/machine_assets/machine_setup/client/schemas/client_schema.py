# schemas.py or within the endpoints module
from pydantic import BaseModel, EmailStr

class ClientUpdate(BaseModel):
    user_id: int
    company_code: str
    name: str
    description: str
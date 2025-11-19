"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogpost" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ContactMessage(BaseModel):
    """
    Contact messages from portfolio site
    Collection name: "contactmessage" (lowercase of class name)
    """
    name: str = Field(..., min_length=2, max_length=100, description="Sender full name")
    email: EmailStr = Field(..., description="Sender email")
    subject: Optional[str] = Field(None, max_length=150, description="Message subject")
    message: str = Field(..., min_length=5, max_length=2000, description="Message content")

# Example additional schemas for potential future use
class Project(BaseModel):
    title: str
    description: str
    live_url: Optional[str] = None
    repo_url: Optional[str] = None
    tags: list[str] = []

class Skill(BaseModel):
    name: str
    level: Optional[str] = None

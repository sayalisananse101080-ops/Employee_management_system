from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):

    email: EmailStr = Field(..., example="sayali@gmail.com")

    password: str = Field(..., min_length=8, example="Admin@123")


class TokenResponse(BaseModel):

    access_token: str

    token_type: str = "bearer"
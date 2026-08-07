from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    age: int = Field(ge=18)

class UserDB(UserSchema):
    password: str
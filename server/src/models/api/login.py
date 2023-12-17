from pydantic import BaseModel


class LoginData(BaseModel):
    user_name: str
    password: str


class SignupData(BaseModel):
    user_name: str
    password: str
    region_id: int


class LoginResponse(BaseModel):
    auth_token: str

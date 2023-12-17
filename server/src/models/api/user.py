from pydantic import BaseModel

class PictureData(BaseModel):
    encoding: str
    data: bytes

class AccountType(BaseModel):
    identifier: str
    price: int

class UserData(BaseModel):
    name:str
    
    account_type: AccountType
    picture_file: PictureData
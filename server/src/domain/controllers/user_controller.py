from fastapi.responses import Response

from ...models.api.user import UserData, AccountType, PictureData
from ...models.database.regional_models import RegionalUser, AccountType as AccountTypeModel, PictureFile
from ...database.sql.regional_connection import  get_user as get_user_model, create_user as post_user_model, delete_user as delete_user_model
from ..authentication import validate_header



async def get_user(user_name: str, token:str) -> UserData:
    user_login = validate_header(token)

    user_model = get_user_model(user_login.region.name, user_name)

    user_data = UserData(
        name= user_model.name,
        account_type= AccountType(
            identifier=user_model.account_type.identifier,
            price=user_model.account_type.price
        ),
        picture_file=PictureData(
            encoding=user_model.picture_file.encoding,
            data=user_model.picture_file.data
        )
    )

    return user_data


async def post_user(user_data:UserData, token:str) -> Response:
    user_login = validate_header(token)
    
    user_model = RegionalUser(
        name=user_data.name,
        account_type=AccountTypeModel(
            identifier=user_data.account_type.identifier,
            price= user_data.account_type.price,
        ),
        picture_file=PictureFile(
            encodeing= user_data.picture_file.encoding,
            data=user_data.picture_file.data,
        ),
    )

    post_user_model(user_login.region.name, user_model)
    return Response()

async def delete_user(user_name:UserData, token:str) -> Response:
    user_login = validate_header(user_name)

    userData = get_user_model(user_login.region.name, user_login.name)
    delete_user_model(user_login.region.name, userData)
    return Response()

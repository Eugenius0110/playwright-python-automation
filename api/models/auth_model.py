
from pydantic import BaseModel, field_validator, Field
from typing import List, Optional
from api.base_api.base_api import BaseApi


class SignUpModel200(BaseModel):
    message: str = Field(min_length=1)

    # @field_validator('message')
    # @classmethod
    # def field_data(cls, value: str, data):
    #     data = f"На указанную почту выслан код верификации!"
    #     return BaseApi.field_data(value, data)


# class SignUpModelError(BaseModel):
#     phone: Optional[List[str]] = None
#     email: Optional[List[str]] = None
#
#
# class SignUpModelErrorPhone(BaseModel):
#     phone: List[str] = Field(min_length=1)
#     @field_validator('phone')
#     @classmethod
#     def field_data(cls, value: str, data):
#         data = ["Пользователь с таким номером телефона уже зарегистрирован."]
#         return BaseApi.field_data(value, data)
#
#
# class SignUpModelErrorEmail(BaseModel):
#     email: List[str] = Field(min_length=1)
#     @field_validator('email')
#     @classmethod
#     def field_data(cls, value: str, data):
#         data = ["Пользователь с таким email уже зарегистрирован."]
#         return BaseApi.field_data(value, data)
#
#
# class ConfirmCodeModel200(BaseModel):
#     message: str = Field(min_length=1)
#     @field_validator('message')
#     @classmethod
#     def field_data(cls, value: str, data):
#         data = "Код подтвержден."
#         return BaseApi.field_data(value, data)
#
#
# class ConfirmCodeModel400(BaseModel):
#     non_field_errors: List[str] = Field(min_length=1)
#     # @field_validator('non_field_errors')
#     # @classmethod
#     # def field_data(cls, value: str, data):
#     #     data = [["Неверный код подтверждения."], ["Код подтверждения истёк или не найден."]]
#     #     return BaseApi.field_data(value, data)
#
#
# class SetPasswordModel200(BaseModel):
#     message: str = Field(min_length=1)
#     access_token: str = Field(min_length=1)
#     refresh_token: str = Field(min_length=1)
#     @field_validator('message')
#     @classmethod
#     def field_data(cls, value: str, data):
#         data = "Пароль успешно установлен."
#         return BaseApi.field_data(value, data)
#
#
# class SetPasswordModelUserNotExist400(BaseModel):
#     non_field_errors: List[str] = Field(min_length=1)
#     @field_validator('non_field_errors')
#     @classmethod
#     def field_data(cls, value: str, data):
#         data = ["Пользователь не найден или не активирован."]
#         return BaseApi.field_data(value, data)
#
#
# class SetPasswordModelPasswordNotMatch400(BaseModel):
#     non_field_errors: List[str] = Field(min_length=1)
#     @field_validator('non_field_errors')
#     @classmethod
#     def field_data(cls, value: str, data):
#         data = ["Пароли не совпадают."]
#         return BaseApi.field_data(value, data)
#
#
# class SetPasswordModelPasswordLength400(BaseModel):
#     password: List[str] = Field(min_length=1)
#     @field_validator('password')
#     @classmethod
#     def field_data(cls, value: str, data):
#         data = ["Пароль должен быть от 8 до 256 символов."]
#         return BaseApi.field_data(value, data)
#
#
# class SetPasswordModelPasswordWithSpace400(BaseModel):
#     password: List[str] = Field(min_length=1)
#     @field_validator('password')
#     @classmethod
#     def field_data(cls, value: str, data):
#         data = ["Пароль не должен содержать пробелы."]
#         return BaseApi.field_data(value, data)
#
#
# class SetPasswordModelPasswordInvalidChar415(BaseModel):
#     detail: str = Field(min_length=1)
#     @field_validator('detail')
#     @classmethod
#     def field_data(cls, value: str, data):
#         data = 'Неподдерживаемый тип данных "" в запросе.'
#         return BaseApi.field_data(value, data)


class LoginSuccess200(BaseModel):
    accessToken: str = Field(min_length=1)
    refreshToken: str = Field(min_length=1)


class LoginEmailNotExist400(BaseModel):
    non_field_errors: List[str] = Field(min_length=1)
    @field_validator('non_field_errors')
    @classmethod
    def field_data(cls, value: str, data):
        data = ["Неверный email или пароль."]
        return BaseApi.field_data(value, data)


class LoginPasswordIncorrect400(BaseModel):
    non_field_errors: List[str] = Field(min_length=1)
    @field_validator('non_field_errors')
    @classmethod
    def field_data(cls, value: str, data):
        data = ["Неверный email или пароль."]
        return BaseApi.field_data(value, data)


class LoginEmailEmpty400(BaseModel):
    email: List[str] = Field(min_length=1)
    @field_validator('email')
    @classmethod
    def field_data(cls, value: str, data):
        data = ["Это поле не может быть пустым."]
        return BaseApi.field_data(value, data)


class LogoutSuccess200(BaseModel):
    detail: str = Field(min_length=1)
    @field_validator('detail')
    @classmethod
    def field_data(cls, value: str, data):
        data = "Вы успешно вышли из аккаунта."
        return BaseApi.field_data(value, data)


class LogoutError400(BaseModel):
    detail: str = Field(min_length=1)
    @field_validator('detail')
    @classmethod
    def field_data(cls, value: str, data):
        data = "Необходим refresh-токен."
        return BaseApi.field_data(value, data)


class RefreshTokenSuccess200(BaseModel):
    access_token: str = Field(min_length=1)

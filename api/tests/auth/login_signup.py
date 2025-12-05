
import pytest
import json
from api.endpoints.auth import Auth
#from api.endpoints.confirm_code import ConfirmCode
#from api.endpoints.set_password import SetPassword
from api.payloads.auth_payload import SignUpPayload, LoginPayload
from api.payloads.auth_payload import ConfirmCodePayload
from api.payloads.auth_payload import SetPasswordPayload
import api.models.auth_model as models
from http import HTTPStatus


@pytest.mark.parametrize('payload, status_code, model', [(
        SignUpPayload.payload_signup_ok,
        HTTPStatus.OK,
        models.SignUpModel200)])
def test_signup_user_200(api_request_context, payload, status_code, model):
    signup_endpoint = Auth(api_request_context)
    signup_endpoint.signup_user(payload)
    signup_endpoint.check_response_status_code(status_code)
    signup_endpoint.check_model(model)
    signup_endpoint.delete_user()

@pytest.mark.parametrize('payload, status_code, model', [(
        LoginPayload.payload_user_admin_login_success,
        HTTPStatus.OK,
        models.LoginSuccess200)])
@pytest.mark.api
@pytest.mark.smoke
def test_login_200(api_request_context, payload, status_code, model): # test_passed
    login_endpoint = Auth(api_request_context)
    login_endpoint.login_user_admin(payload)
    login_endpoint.print_response()
    login_endpoint.check_response_status_code(status_code)
    login_endpoint.check_model(model)



# @pytest.mark.parametrize('payload, status_code, model', [(
#         ConfirmCodePayload.payload_confirm_code_invalid,
#         HTTPStatus.BAD_REQUEST,
#         models.ConfirmCodeModel400)])
# def test_confirm_code_invalid_400(payload, status_code, model): # skip
#     confirm_code_endpoint = ConfirmCode()
#     confirm_code_endpoint.confirm_code(payload)
#     confirm_code_endpoint.check_response_status_code(status_code)
#     confirm_code_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         ConfirmCodePayload.get_confirm_code(),
#         HTTPStatus.OK,
#         models.ConfirmCodeModel200)])
# def test_confirm_code_200(payload, status_code, model):
#     confirm_code_endpoint = ConfirmCode()
#     confirm_code_endpoint.confirm_code(payload)
#     confirm_code_endpoint.check_response_status_code(status_code)
#     confirm_code_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         SignUpPayload.payload_signup_already_email_reg,
#         HTTPStatus.BAD_REQUEST,
#         models.SignUpModelErrorEmail)])
# def test_signup_email_already_ref_400(payload, status_code, model):
#     signup_endpoint = SignupUser()
#     signup_endpoint.new_signup_user(payload)
#     signup_endpoint.check_response_status_code(status_code)
#     signup_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         SignUpPayload.payload_signup_already_phone_reg,
#         HTTPStatus.BAD_REQUEST,
#         models.SignUpModelErrorPhone)])
# def test_signup_phone_already_reg_400(payload, status_code, model):
#     signup_endpoint = SignupUser()
#     signup_endpoint.new_signup_user(payload)
#     signup_endpoint.check_response_status_code(status_code)
#     signup_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         SetPasswordPayload.payload_user_not_exist_400,
#         HTTPStatus.BAD_REQUEST,
#         models.SetPasswordModelUserNotExist400)])
# def test_setpassword_user_not_exist_400(payload, status_code, model):
#     setpassword_endpoint = SetPassword()
#     setpassword_endpoint.set_password(payload)
#     setpassword_endpoint.check_response_status_code(status_code)
#     setpassword_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         SetPasswordPayload.payload_password_not_match,
#         HTTPStatus.BAD_REQUEST,
#         models.SetPasswordModelPasswordNotMatch400)])
# def test_setpassword_password_not_match_400(payload, status_code, model):
#     setpassword_endpoint = SetPassword()
#     setpassword_endpoint.set_password(payload)
#     setpassword_endpoint.check_response_status_code(status_code)
#     setpassword_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         SetPasswordPayload.payload_password_short,
#         HTTPStatus.BAD_REQUEST,
#         models.SetPasswordModelPasswordLength400)])
# def test_setpassword_password_short_400(payload, status_code, model):
#     setpassword_endpoint = SetPassword()
#     setpassword_endpoint.set_password(payload)
#     setpassword_endpoint.check_response_status_code(status_code)
#     setpassword_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         SetPasswordPayload.payload_password_long,
#         HTTPStatus.BAD_REQUEST,
#         models.SetPasswordModelPasswordLength400)])
# def test_setpassword_password_long_400(payload, status_code, model):
#     setpassword_endpoint = SetPassword()
#     setpassword_endpoint.set_password(payload)
#     setpassword_endpoint.check_response_status_code(status_code)
#     setpassword_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         SetPasswordPayload.payload_password_with_space,
#         HTTPStatus.BAD_REQUEST,
#         models.SetPasswordModelPasswordWithSpace400)])
# def test_setpassword_password_with_space_400(payload, status_code, model):
#     setpassword_endpoint = SetPassword()
#     setpassword_endpoint.set_password(payload)
#     setpassword_endpoint.check_response_status_code(status_code)
#     setpassword_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         SetPasswordPayload.password_invalid_characters,
#         HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
#         models.SetPasswordModelPasswordInvalidChar415)])
# def test_setpassword_password_invalid_characters_415(payload, status_code, model): #passed
#     setpassword_endpoint = SetPassword()
#     setpassword_endpoint.set_password(payload)
#     setpassword_endpoint.check_response_status_code(status_code)
#     setpassword_endpoint.check_model(model)
#
# @pytest.mark.parametrize('payload, status_code, model', [(
#         SetPasswordPayload.payload_password_match,
#         HTTPStatus.OK,
#         models.SetPasswordModel200)])
# def test_setpassword_200(payload, status_code, model):
#     setpassword_endpoint = SetPassword()
#     setpassword_endpoint.set_password(payload)
#     setpassword_endpoint.check_response_status_code(status_code)
#     setpassword_endpoint.check_model(model)
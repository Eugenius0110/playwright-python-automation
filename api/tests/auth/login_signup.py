
import pytest
import allure
from http import HTTPStatus
from api.endpoints.auth import Auth
#from api.endpoints.confirm_code import ConfirmCode
#from api.endpoints.set_password import SetPassword
from api.payloads.auth_payload import SignUpPayload, LoginPayload, ConfirmCodePayload
from api.payloads.auth_payload import ConfirmCodePayload
from api.payloads.auth_payload import SetPasswordPayload
import api.models.auth_model as models


@pytest.mark.api
@pytest.mark.smoke
@allure.feature("Authentication")
@allure.suite("API tests")
class TestAuthentication:

    @allure.title("Login")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("login", "positive")
    @allure.description("""
        step 1: login user admin
        step 2: verify status code
        step 3: verify model
        step 4: verify access token
        """)
    @pytest.mark.parametrize('payload, status_code, model', [(
        LoginPayload.payload_user_admin_login_success,
        HTTPStatus.OK,
        models.LoginSuccess200)])
    def test_login_200(self, api_request_context, payload, status_code, model): # test_passed
        auth = Auth(api_request_context)
        auth.login_user_admin(payload)
        auth.check_response_status_code(status_code)
        auth.check_model(model)


    @allure.title('Logout')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("logout", "positive")
    @allure.description("""
        step 1: login user admin
        step 2: verify status code
        step 3: verify model
        step 4: verify access token
        step 5: logout user
        step 6: verify status code
        step 7: verify model
        """)
    @pytest.mark.parametrize('payload, status_code, model', [(
        LoginPayload.payload_user_admin_login_success,
        HTTPStatus.OK,
        models.LogoutSuccess200)])
    def test_logout_200(self, api_request_context, payload, status_code, model): # test_passed
        auth = Auth(api_request_context)
        auth.login_user_admin(payload)
        auth.logout_user()
        auth.check_response_status_code(status_code)
        auth.check_model(model)

@pytest.mark.skip
@pytest.mark.api
@pytest.mark.smoke
@allure.story("Sign up")
@pytest.mark.parametrize('payload, status_code, model', [(
        SignUpPayload.payload_signup_ok,
        HTTPStatus.OK,
        models.SignUpModel200)])
def test_signup_user_200(api_request_context, payload, status_code, model):
    auth = Auth(api_request_context)
    auth.signup_user(payload)
    auth.check_response_status_code(status_code)
    auth.check_model(model)
    auth.confirm_code(ConfirmCodePayload.get_confirm_code())
    #auth.check_model(model)
    #signup_endpoint.delete_user()
    #auth.print_response()

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
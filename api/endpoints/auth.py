
import os
import allure
from playwright.sync_api import APIRequestContext, expect
from api.base_api.base_api import BaseApi
from api.payloads.auth_payload import ConfirmCodePayload
from dotenv import load_dotenv
load_dotenv()

class Auth(BaseApi):

    BASE_URL = f"{os.getenv('HOST_TEAM_2')}"
    URL_REG = f"{os.getenv('URL_REG')}"
    URL_LOG = f"{os.getenv('URL_LOGIN')}"
    URL_LOGOUT = f"{os.getenv('URL_LOGOUT')}"

    TEST_EMAIL_USER = f"{os.getenv('TEST_EMAIL_USER')}."


    def __init__(self, request_context: APIRequestContext):
        super().__init__(request_context)
        self.header = {
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        }
        self.access_token = None
        self.refresh_token = None

    def signup_user(self, payload): # payload
        self.logger.info(f"Signup user: {self.URL_REG}")
        with allure.step(f"Request API POST {self.URL_REG}"):
            self.response = self.request.post(
                url=f"{self.BASE_URL}{self.URL_REG}",
                headers=self.header,
                data=payload
            )
        #self.logger.info(f"Response body: {self.response.json()}")
        return self.response.json()

    @allure.step(f"POST request to {URL_LOG}")
    def login_user(self, payload):
        self.logger.info(f"Login user: {self.URL_LOG}")
        self.response = self.request.post(
            url=f"{self.BASE_URL}{self.URL_LOG}",
            data=payload
            )
        if self.response.ok:
            if 'accessToken' in self.response.json():
                self.logger.info(f"Login success. Tokens received.")
                self.access_token = self.response.json()['accessToken']
                self.refresh_token = self.response.json()['refreshToken']
            else:
                self.logger.warning(f"Login success, but no tokens received.")
            return self.response.json()

        else:
            self.logger.error(f"Login failed with status code {self.response.status}")

    @allure.step(f"POST request to {URL_LOGOUT}")
    def logout_user(self):
        self.logger.info(f"Logout user: {self.URL_LOGOUT}")

        self.response = self.request.post(
            url=f"{self.BASE_URL}{self.URL_LOGOUT}",
            headers={
                "Authorization": f"Bearer {self.access_token}"
                }
            )

    def confirm_code(self, payload): # payload
        self.logger.info(f"Get confirm_code: /api/auth/registration/confirm-mail")
        self.response = self.request.post(
            url=f"{self.BASE_URL}/api/auth/registration/confirm-mail",
            headers={
                "Authorization": f"Bearer {self.access_token}"
                },
            data=payload
        )
        self.logger.info(f"Confirm_code: {payload}")
        return self.response.json()

    # def delete_user(self):
    #     self.response = self.request.post(
    #         url=f"{self.BASE_URL}/api/user/delete",
    #         headers={
    #             "Authorization": f"Bearer {self.access_token}"
    #         }
    #     )



    def login_user_admin(self, payload):
        self.logger.info(f"Login user: {self.BASE_URL}{self.URL_LOG}")
        self.response = self.request.post(
            url=f"{self.BASE_URL}{self.URL_LOG}",
            data=payload
        )
        if 'accessToken' in self.response.json():
           self.logger.info(f"Login success.")
           self.logger.info(f"Access token has been received.")
           self.access_token = self.response.json()['accessToken']
           self.refresh_token = self.response.json()['refreshToken']
        return self.response.json()

    # def refresh(self):
    #     payload_refresh_token = {
    #         "refresh_token": f"{self.refresh_token}"
    #         }
    #     self.response = requests.post(
    #         url=f"{self.BASE_URL}/api/token/refresh/",
    #         json=payload_refresh_token,
    #         headers={
    #            "Authorization": f"Bearer {self.access_token}"
    #             }
    #         )

    # def assign_admin_self(self):
    #     payload_refresh_token = {
    #         "refresh_token": f"{self.refresh_token}"
    #     }
    #     self.response = request.post(
    #         url=f"{self.BASE_URL}/api/user/assign-admin-self",
    #         json=payload_refresh_token,
    #         headers={
    #             "Authorization": f"Bearer {self.access_token}"
    #         }
    #     )

    # class ConfirmCode(BaseApi):
    #
    #     def confirm_code(self, payload):
    #         self.response = requests.post(f"{self.BASE_URL}/api/auth/confirm-code/", payload)
    #

#
# class ResetAndSetNewPassword(BaseApi):
#
#
#     def reset_password(self, payload):
#         self.response = requests.post(f"{self.BASE_URL}/api/auth/reset-password/", payload)
#
#     def verify_reset_code(self, payload):
#         self.response = requests.post(f"{self.BASE_URL}/api/auth/verify-reset-code/", payload)
#
#     def set_new_password(self, payload):
#         self.response = requests.post(f"{self.BASE_URL}/api/auth/set-new-password/", payload)

#
# class SetPassword(BaseApi):
#
#     def set_password(self, payload):
#         self.response = requests.post(f"{self.BASE_URL}/api/auth/set-password/", payload)
#
#

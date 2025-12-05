
#import requests
import json
from playwright.sync_api import APIRequestContext, expect
from api.base_api.base_api import BaseApi


class Auth(BaseApi):
    def __init__(self, request_context: APIRequestContext):
        super().__init__(request_context)
        self.header = {
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        }
        self.access_token = None
        self.refresh_token = None

    def signup_user(self, payload): # payload
        self.response = self.request.post(
            url=f"{self.BASE_URL}/api/auth/registration",
            headers=self.header,
            data=payload
        )
        return self.response.json()

    def login_user_admin(self, payload):
        self.response = self.request.post(
            url=f"{self.BASE_URL}/api/auth/login",
            data=payload
        )
        if 'accessToken' in self.response.json():
           self.access_token = self.response.json()['accessToken']
           self.refresh_token = self.response.json()['refreshToken']
        return self.response.json()

    # def logout(self):
    #     payload_refresh_token = {
    #         "refresh_token": f"{self.refresh_token}"
    #         }
    #     self.response = requests.post(
    #        url=f"{self.BASE_URL}/api/auth/logout",
    #        json=payload_refresh_token,
    #        headers={
    #             "Authorization": f"Bearer {self.access_token}"
    #             }
    #         )

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


    def delete_user(self):
        self.response = self.request.post(
            url=f"{self.BASE_URL}/api/user/delete",
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )

    #
    # import requests
    # from api.endpoints.base_api import BaseApi
    #
    #
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

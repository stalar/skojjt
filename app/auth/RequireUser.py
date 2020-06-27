import jwt
import werkzeug
from flask import request, Response
from werkzeug.exceptions import HTTPException

from auth.Auth import Auth
from auth.XOrigin import XOrigin
from init import api


class RequireUser(XOrigin):
    auth = None

    def require_user(self):
        if "Authorization" not in request.headers:
            raise werkzeug.exceptions.Forbidden("Authorization header is missing")

        auth_header = request.headers["Authorization"]

        if auth_header[0:7] != "Bearer ":
            raise werkzeug.exceptions.Forbidden("Authorization header is not Bearer type")

        self.auth = Auth(auth_header[7:])

    def dispatch_request(self, *args, **kwargs):
        try:
            self.require_user()
        except Exception as e:
            return self.exception(e)

        return super().dispatch_request(*args, **kwargs)

    def require_kar_admin(self, kar_id):
        if not self.auth.has_kar_admin_access(kar_id):
            raise werkzeug.exceptions.Forbidden("You are not admin for this group(kår)")

    def require_kar_access(self, kar_id):
        if not self.auth.has_kar_access(kar_id):
            raise werkzeug.exceptions.Forbidden("You don't have access for this group(kår)")
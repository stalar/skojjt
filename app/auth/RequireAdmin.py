from auth.RequireUser import RequireUser


class RequireAdmin(RequireUser):
    def dispatch_request(self, *args, **kwargs):
        try:
            self.require_user()
        except Exception as e:
            return self.exception(e)

        if not self.auth.is_admin():
            return self.error("Admin access required", 403)

        return super().dispatch_request(*args, **kwargs)
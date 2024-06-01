from api.base_api import BaseAPI


class ReqresGET(BaseAPI):

    def get_list_users(self, return_raw=False):
        return self.get("/api/users", return_raw=return_raw)

    def get_user(self, user_id, return_raw=False):
        return self.get(f"/api/users/{user_id}", return_raw=return_raw)

    def get_list_unknown(self, return_raw=False):
        return self.get(f"/api/unknown", return_raw=return_raw)

    def get_unknown(self, unknown_id, return_raw=False):
        return self.get(f"/api/unknown/{unknown_id}", return_raw=return_raw)

from api.base_api import BaseAPI


class ReqresGET(BaseAPI):

    def get_list_users(self, return_raw=False):
        return self.get("/api/users", return_raw=return_raw)

    def get_list_users_schema(self):
        return {
            "type": "object",
            "properties": {
                "page": {"type": "integer"},
                "per_page": {"type": "integer"},
                "total": {"type": "integer"},
                "total_pages": {"type": "integer"},
                "data": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "email": {"type": "string", "format": "email"},
                            "first_name": {"type": "string"},
                            "last_name": {"type": "string"},
                            "avatar": {"type": "string", "format": "uri"}
                        },
                        "required": ["id", "email", "first_name", "last_name", "avatar"]
                    }
                },
                "support": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string", "format": "uri"},
                        "text": {"type": "string"}
                    },
                    "required": ["url", "text"]
                }
            },
            "required": ["page", "per_page", "total", "total_pages", "data", "support"]
        }

    def get_user(self, user_id, return_raw=False):
        return self.get(f"/api/users/{user_id}", return_raw=return_raw)

    def get_list_unknown(self, return_raw=False):
        return self.get(f"/api/unknown", return_raw=return_raw)

    def get_unknown(self, unknown_id, return_raw=False):
        return self.get(f"/api/unknown/{unknown_id}", return_raw=return_raw)

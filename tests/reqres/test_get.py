from api.reqres.reqres_api import reqres_api


class TestReqresGet:

    def test_get_users_list(self, reqres_api):
        response = reqres_api.reqres_get.get_list_users(return_raw=True)
        assert response.status_code == 200

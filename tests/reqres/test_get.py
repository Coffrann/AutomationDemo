import allure
from api.reqres.reqres_api import reqres_api
from api.reqres.get_schemas import *
from constants.api.reqres_get.reqres_get_constants import *


class TestReqresGet:

    def test_get_users_list(self, reqres_api):
        response = reqres_api.reqres_get.get_list_users(return_raw=True)
        reqres_api.attach_allure_info(response)
        assert response.status_code == 200, f"Expecting SC 200, obtained {response.status_code}"
        assert reqres_api.validate_schema(get_list_users_schema, response.json()), "Schema for API is not correct"
        assert response.json()["support"]["text"] == support_text, "Wrong support text obtained"

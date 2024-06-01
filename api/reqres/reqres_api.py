import pytest
from api.base_api import BaseAPI
from api.reqres.get_api import ReqresGET


class ReqresAPI(BaseAPI):

    def __init__(self, base_api):
        super().__init__(base_api)
        self.reqres_get = ReqresGET(base_api)


@pytest.fixture(scope="session")
def reqres_api():
    return ReqresAPI("https://reqres.in")

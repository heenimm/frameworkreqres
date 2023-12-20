import pytest

from framework.reqres_api import ReqresAPI

@pytest.fixture(scope="session")
def reqres_api():
   HOST = 'https://reqres.in'
   return ReqresAPI(HOST)
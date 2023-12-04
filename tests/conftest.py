import pytest

from config import HOST
from framework.reqres_api import ReqresAPI

@pytest.fixture(scope="session")
def reqres_api():
   return ReqresAPI(HOST)
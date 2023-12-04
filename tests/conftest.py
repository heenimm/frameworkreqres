import pytest

from config import HOST
from framework.reqres_api import ReqresAPI

@pytest.fixture(scope="session")
def reqres_api():
   return ReqresAPI(HOST)

if __name__ == "__main__":
    import config
    import framework
else:
    from config import HOST
    from framework.reqres_api import ReqresAPI
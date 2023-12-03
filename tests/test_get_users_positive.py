from data.data import PAGE_POS, PER_PAGE
from hamcrest import assert_that,equal_to

def test_get_users_valid(reqres_api):
    status_code, response = reqres_api.get_users(PAGE_POS[0])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(PAGE_POS[0]))
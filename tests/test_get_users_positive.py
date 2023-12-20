from tests.data.data import PAGE_POS, PER_PAGE
from hamcrest import assert_that,equal_to

class TestGetUsersPositive():
    def test_get_users_valid_with_page(self, reqres_api):
        status_code, response = reqres_api.get_users(PAGE_POS)
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(PAGE_POS))

    def test_get_users_valid_with_per_page(self, reqres_api):
        status_code, response = reqres_api.get_users_with_per_page(PAGE_POS, PER_PAGE)
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(PAGE_POS))
        assert_that(response.get('per_page'), equal_to(PER_PAGE))
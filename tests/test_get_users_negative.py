from tests.data.data import PAGE_NEG
from hamcrest import assert_that, equal_to

class TestGetUsersNegative():

    def test_create_with_empty_string(self, reqres_api):
        status_code, response = reqres_api.get_users(PAGE_NEG[0])
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(1))
    def test_get_users_with_symbol(self, reqres_api):
        status_code, response = reqres_api.get_users(PAGE_NEG[1])
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(1))

    def test_get_users_with_whitespace(self, reqres_api):
        status_code, response = reqres_api.get_users(PAGE_NEG[2])
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(1))

    def test_get_users_with_fractional(self, reqres_api):
        status_code, response = reqres_api.get_users(PAGE_NEG[3])
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(1))

    def test_get_users_with_negative_integer(self, reqres_api):
        status_code, response = reqres_api.get_users(PAGE_NEG[4])
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(1))

    def test_get_users_with_latin(self, reqres_api):
        status_code, response = reqres_api.get_users(PAGE_NEG[5])
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(1))

    def test_get_users_with_сyrillic(self, reqres_api):
        status_code, response = reqres_api.get_users(PAGE_NEG[6])
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(1))

    def test_get_users_with_per_page_max_int(self, reqres_api):
        status_code, response = reqres_api.get_users_with_per_page(PAGE_NEG[7], PAGE_NEG[7])
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(1))

    def test_get_users_with_XSS(self, reqres_api):
        status_code, response = reqres_api.get_users(PAGE_NEG[8])
        assert_that(status_code, equal_to(200))
        assert_that(response.get('page'), equal_to(1))

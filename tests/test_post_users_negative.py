from hamcrest import assert_that, equal_to, is_not
from tests.data.data import NAME_AND_JOB_NEG

class TestPostUsersNegative():
    def test_create_with_empty_string(self, reqres_api):
        status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[0], NAME_AND_JOB_NEG[0])
        assert_that(status_code, is_not(201))

    def test_create_with_symbol(self, reqres_api):
        status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[1], NAME_AND_JOB_NEG[1])
        assert_that(status_code, is_not(201))

    def test_create_with_whitespace(self, reqres_api):
        status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[2], NAME_AND_JOB_NEG[2])
        assert_that(status_code, is_not(201))

    def test_create_with_fractional(self, reqres_api):
        status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[3], NAME_AND_JOB_NEG[3])
        assert_that(status_code, is_not(201))

    def test_create_with_integer(self, reqres_api):
        status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[4], NAME_AND_JOB_NEG[4])
        assert_that(status_code, is_not(201))


    def test_create_string__with_characters_and_spaces(self, reqres_api):
        status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[5], NAME_AND_JOB_NEG[5])
        assert_that(status_code, equal_to(201))
        assert_that(response['name'], equal_to(NAME_AND_JOB_NEG[5]))
        assert_that(response.get('job'), equal_to(NAME_AND_JOB_NEG[5]))

    def test_create_with_XSS(self, reqres_api):
        status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[6], NAME_AND_JOB_NEG[6])
        assert_that(status_code, is_not(201))

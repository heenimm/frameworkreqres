from hamcrest import assert_that,equal_to
from data.data import NAME_POS, JOB_POS

def test_create_post_valid(reqres_api):
    status_code, response = reqres_api.create_user(NAME_POS[0], JOB_POS[0])
    print(NAME_POS[0], JOB_POS[0], response)
    assert_that(status_code, equal_to(201))
    assert_that(response.get('name'), equal_to(NAME_POS[0]))
    assert_that(response.get('job'), equal_to(JOB_POS[0]))

def test_create_post_invalid(reqres_api):
    status_code, response = reqres_api.create_user(NAME_POS[1], JOB_POS[1])
    assert_that(status_code, equal_to(201))
    assert_that(response['name'], equal_to(NAME_POS[1]))
    assert_that(response.get('job'), equal_to(JOB_POS[1]))



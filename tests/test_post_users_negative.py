from hamcrest import assert_that,equal_to
from data.data import NAME_AND_JOB_NEG


def test_create_with_empty_string(reqres_api):
    status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[0], NAME_AND_JOB_NEG[0])
    assert_that(status_code, equal_to(201))
    assert_that(response['name'], equal_to(NAME_AND_JOB_NEG[0]))
    assert_that(response.get('job'), equal_to(NAME_AND_JOB_NEG[0]))

def test_create_with_symbol(reqres_api):
    status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[1], NAME_AND_JOB_NEG[1])
    assert_that(status_code, equal_to(201))
    assert_that(response['name'], equal_to(NAME_AND_JOB_NEG[1]))
    assert_that(response.get('job'), equal_to(NAME_AND_JOB_NEG[1]))


def test_create_with_whitespace(reqres_api):
    status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[2], NAME_AND_JOB_NEG[2])
    assert_that(status_code, equal_to(201))
    assert_that(response['name'], equal_to(NAME_AND_JOB_NEG[2]))
    assert_that(response.get('job'), equal_to(NAME_AND_JOB_NEG[2]))

def test_create_with_fractional(reqres_api):
    status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[3], NAME_AND_JOB_NEG[3])
    assert_that(status_code, equal_to(201))
    assert_that(float(response['name']), equal_to(NAME_AND_JOB_NEG[3]))
    assert_that(float(response.get('job')), equal_to(NAME_AND_JOB_NEG[3]))

def test_create_with_integer(reqres_api):
    status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[4], NAME_AND_JOB_NEG[4])
    assert_that(status_code, equal_to(201))
    assert_that(int(response['name']), equal_to(NAME_AND_JOB_NEG[4]))
    assert_that(int(response.get('job')), equal_to(NAME_AND_JOB_NEG[4]))

def test_create_string__with_characters_and_spaces(reqres_api):
    status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[5], NAME_AND_JOB_NEG[5])
    assert_that(status_code, equal_to(201))
    assert_that(response['name'], equal_to(NAME_AND_JOB_NEG[5]))
    assert_that(response.get('job'), equal_to(NAME_AND_JOB_NEG[5]))

def test_create_with_XSS(reqres_api):
    status_code, response = reqres_api.create_user(NAME_AND_JOB_NEG[6], NAME_AND_JOB_NEG[6])
    assert_that(status_code, equal_to(201))
    assert_that(response['name'], equal_to(NAME_AND_JOB_NEG[6]))
    assert_that(response.get('job'), equal_to(NAME_AND_JOB_NEG[6]))
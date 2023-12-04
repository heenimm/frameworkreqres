from data.data import PAGE_NEG
from hamcrest import assert_that, equal_to

def test_create_with_empty_string(reqres_api):
    status_code, response = reqres_api.get_users(PAGE_NEG[0])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(1))

def test_get_users_with_symbol(reqres_api):
    status_code, response = reqres_api.get_users(PAGE_NEG[1])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(1))

def test_get_users_with_whitespace(reqres_api):
    status_code, response = reqres_api.get_users(PAGE_NEG[2])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(1))

def test_get_users_with_fractional(reqres_api):
    status_code, response = reqres_api.get_users(PAGE_NEG[3])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(1))

def test_get_users_with_negative_integer(reqres_api):
    status_code, response = reqres_api.get_users(PAGE_NEG[4])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(1))

def test_get_users_with_latin(reqres_api):
    status_code, response = reqres_api.get_users(PAGE_NEG[5])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(1))

def test_get_users_with_сyrillic(reqres_api):
    status_code, response = reqres_api.get_users(PAGE_NEG[6])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(1))

def test_get_users_with_per_page_max_int(reqres_api):
    status_code, response = reqres_api.get_users_with_per_page(PAGE_NEG[7], PAGE_NEG[7])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(1))

def test_get_users_with_XSS(reqres_api):
    status_code, response = reqres_api.get_users(PAGE_NEG[8])
    assert_that(status_code, equal_to(200))
    assert_that(response.get('page'), equal_to(1))

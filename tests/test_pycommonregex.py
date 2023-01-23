from pycommonregex.pycommonregex import *

def test_is_positive_int():
    assert is_positive_int("123")
    assert not is_positive_int("1.23")
    assert not is_positive_int("abc")

def test_is_int():
    assert is_int(123)
    assert not is_int(1.23)
    assert not is_int("abc")

def test_is_decimal_num():
    assert is_decimal_num("123")
    assert is_decimal_num("1.23")
    assert not is_decimal_num("abc")


def test_is_num():
    assert is_num("123")
    assert is_num("1.23")
    assert not is_num("abc")


def test_is_alpha_numeric():
    assert is_alpha_numeric("abc123")
    assert not is_alpha_numeric("abc 123")
    assert not is_alpha_numeric("abc@123")

def test_is_alpha_numeric_with_space():
    assert is_alpha_numeric_with_space("abc123")
    assert is_alpha_numeric_with_space("abc 123")
    assert not is_alpha_numeric_with_space("abc@123")

def test_is_email():
    assert is_email("x@p.com")
    assert not is_email("x@p")


def test_is_good_password():
    assert is_good_password("12345678Aa@#")
    assert not is_good_password("123456")


def test_is_username():
    assert is_username("user1")
    assert not is_username("u")
    assert not is_username("user@1")

def test_is_url():
    assert is_url("http://www.google.com")
    assert not is_url("www.google")

def test_is_ip():
    assert is_ipv4("0.0.0.0")
    assert not is_ipv4("0.0.0")

def test_is_ipv6():
    assert is_ipv6("2001:db8:3333:4444:5555:6666:7777:8888")
    assert not is_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370")

def test_is_date_yyyy_mm_dd():
    assert is_date_yyyy_mm_dd("2019-01-01")
    assert not is_date_yyyy_mm_dd("2019-01-1")
    assert not is_date_yyyy_mm_dd("2019-1-01")
    assert not is_date_yyyy_mm_dd("2019-1-1")
    assert not is_date_yyyy_mm_dd("2019-01-01 12:00:00")

    
def test_is_date_dd_mm_yyyy():
    assert is_date_dd_mm_yyyy("01-01-2019")
    assert not is_date_dd_mm_yyyy("1-01-2019")
    assert not is_date_dd_mm_yyyy("01-1-2019")
    assert not is_date_dd_mm_yyyy("1-1-2019")
    assert not is_date_dd_mm_yyyy("01-01-2019 12:00:00")

def test_is_time_hh_mm_12h():
    assert is_time_hh_mm_12h("12:00 AM")
    assert not is_time_hh_mm_12h("12:00")
    assert is_time_hh_mm_12h("12:00 am")

def test_is_time_hh_mm_24h():
    assert is_time_hh_mm_24h("12:00")
    assert not is_time_hh_mm_24h("12:00 AM")
    assert not is_time_hh_mm_24h("12:00 am")

def test_is_time_hh_mm():
    assert is_time_hh_mm("12:00")
    assert is_time_hh_mm("12:00 AM")
    assert is_time_hh_mm("12:00 am")

def test_is_html_tag():
    assert is_html_tag("<html>")
    assert not is_html_tag("html")

def test_is_slug():
    assert is_slug("this-is-a-slug")
    assert not is_slug("this is a slug")

def test_is_tel():
    assert is_tel("+1 (555) 555-5555")
    assert is_tel("555-555-5555")
    assert is_tel("555-555-5555")
    assert is_tel("555 555 5555")
    assert is_tel("555 555-5555 x1234")
    assert is_tel("555 555-5555 ext1234")
    assert is_tel("555")

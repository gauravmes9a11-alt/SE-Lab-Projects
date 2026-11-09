
import pytest
from hypothesis import given, strategies as st

from elevator_dispatch import (
    parse_request,
    total_travel,
    load_percent
)


# ==========================================
# FUZZ TEST 1: parse_request()
# ==========================================

@given(st.one_of(st.text(), st.none()))
def test_parse_request_no_crash(s):
    try:
        result = parse_request(s)
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert all(isinstance(x, int) for x in result)
    except ValueError:
        pass


def test_parse_request_valid():
    assert parse_request("5->9") == (5, 9)


def test_parse_request_invalid():
    with pytest.raises(ValueError):
        parse_request("invalid")


# ==========================================
# FUZZ TEST 2: total_travel()
# ==========================================

@given(st.one_of(st.text(), st.none()))
def test_total_travel_no_crash(s):
    try:
        result = total_travel(s)
        assert isinstance(result, int)
        assert result >= 0
    except ValueError:
        pass


def test_total_travel_valid():
    assert total_travel("1,5,3,9") == 12


def test_total_travel_invalid():
    with pytest.raises(ValueError):
        total_travel("1,abc,3")


# ==========================================
# FUZZ TEST 3: load_percent()
# ==========================================

@given(st.one_of(st.text(), st.none()))
def test_load_percent_no_crash(s):
    try:
        result = load_percent(s)
        assert isinstance(result, int)
        assert result >= 0
    except ValueError:
        pass


def test_load_percent_valid():
    assert load_percent("450 of 630") == 71


def test_load_percent_zero_capacity():
    with pytest.raises(ValueError):
        load_percent("450 of 0")


def test_load_percent_invalid():
    with pytest.raises(ValueError):
        load_percent("invalid")


import pytest

from elevator_dispatch import (
    next_direction,
    door_action,
    pick_elevator
)


# --------------------------------------------------
# CODE COVERAGE TESTS: next_direction()
# --------------------------------------------------

def test_next_direction_up_with_request_above():
    assert next_direction(3, "up", [5, 7]) == "up"


def test_next_direction_up_with_request_below():
    assert next_direction(5, "up", [2]) == "down"


def test_next_direction_up_without_requests():
    assert next_direction(5, "up", []) == "idle"


def test_next_direction_down_with_request_below():
    assert next_direction(5, "down", [2]) == "down"


def test_next_direction_down_with_request_above():
    assert next_direction(5, "down", [8]) == "up"


def test_next_direction_down_without_requests():
    assert next_direction(5, "down", []) == "idle"


def test_next_direction_other_direction_with_request_above():
    assert next_direction(3, "idle", [8]) == "up"


def test_next_direction_other_direction_with_request_below():
    assert next_direction(5, "idle", [2]) == "down"


def test_next_direction_other_direction_without_requests():
    assert next_direction(5, "idle", []) == "idle"


# --------------------------------------------------
# CODE COVERAGE TESTS: door_action()
# --------------------------------------------------

def test_door_action_emergency():
    assert door_action(100, False, True) == "hold_open"


def test_door_action_overload():
    assert door_action(700, False, False) == "overload"


def test_door_action_blocked():
    assert door_action(100, True, False) == "reopen"


def test_door_action_normal():
    assert door_action(100, False, False) == "close"


# --------------------------------------------------
# CODE COVERAGE TESTS: pick_elevator()
# --------------------------------------------------

def test_pick_elevator_empty_list():
    assert pick_elevator([], 5) is None


def test_pick_elevator_selects_nearest_idle_car():
    cars = [
        ("A", 2, True),
        ("B", 6, True)
    ]
    assert pick_elevator(cars, 5) == "B"


def test_pick_elevator_selects_nearest_car_with_penalty():
    cars = [
        ("A", 5, False),
        ("B", 8, True)
    ]
    assert pick_elevator(cars, 5) == "B"


def test_pick_elevator_penalty_changes_selection():
    cars = [
        ("A", 4, False),
        ("B", 8, True)
    ]
    assert pick_elevator(cars, 5) == "B"


def test_pick_elevator_first_car_wins_tie():
    cars = [
        ("A", 4, True),
        ("B", 6, True)
    ]
    assert pick_elevator(cars, 5) == "A"

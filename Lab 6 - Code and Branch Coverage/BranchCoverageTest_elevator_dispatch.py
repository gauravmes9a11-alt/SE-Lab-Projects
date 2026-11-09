
from elevator_dispatch import (
    next_direction,
    door_action,
    pick_elevator
)


# ==========================================
# BRANCH TESTS: next_direction()
# ==========================================

def test_up_direction_request_above():
    assert next_direction(3, "up", [5]) == "up"


def test_up_direction_no_request_above():
    assert next_direction(5, "up", [2]) == "down"


def test_up_direction_no_requests():
    assert next_direction(5, "up", []) == "idle"


def test_down_direction_request_below():
    assert next_direction(5, "down", [2]) == "down"


def test_down_direction_no_request_below():
    assert next_direction(5, "down", [8]) == "up"


def test_down_direction_no_requests():
    assert next_direction(5, "down", []) == "idle"


def test_other_direction_request_above():
    assert next_direction(3, "idle", [8]) == "up"


def test_other_direction_request_below():
    assert next_direction(5, "idle", [2]) == "down"


def test_other_direction_no_requests():
    assert next_direction(5, "idle", []) == "idle"


def test_requests_at_current_floor():
    assert next_direction(5, "idle", [5]) == "idle"


# ==========================================
# BRANCH TESTS: door_action()
# ==========================================

def test_emergency_branch():
    assert door_action(100, False, True) == "hold_open"


def test_no_emergency_overload_branch():
    assert door_action(700, False, False) == "overload"


def test_no_emergency_no_overload_blocked_branch():
    assert door_action(100, True, False) == "reopen"


def test_normal_door_branch():
    assert door_action(100, False, False) == "close"


def test_exact_overload_threshold():
    assert door_action(630, False, False) == "close"


# ==========================================
# BRANCH TESTS: pick_elevator()
# ==========================================

def test_no_elevators():
    assert pick_elevator([], 5) is None


def test_first_elevator_selected():
    cars = [("A", 4, True)]
    assert pick_elevator(cars, 5) == "A"


def test_idle_and_non_idle_branches():
    cars = [("A", 5, False), ("B", 8, True)]
    assert pick_elevator(cars, 5) == "B"


def test_non_idle_elevator_selected_when_best():
    cars = [("A", 5, False), ("B", 11, True)]
    assert pick_elevator(cars, 5) == "A"


def test_equal_scores_keep_first_elevator():
    cars = [("A", 4, True), ("B", 6, True)]
    assert pick_elevator(cars, 5) == "A"

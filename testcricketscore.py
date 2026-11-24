
from cricket_score import (
    run_rate,
    strike_rate,
    required_run_rate,
    match_status
)


# Test run rate
def test_run_rate_standard():
    assert run_rate(120, 15) == 8.0


def test_run_rate_zero_overs():
    assert run_rate(50, 0) == 0


def test_run_rate_partial_over():
    assert run_rate(160, 17.5) == 8.97


# Test strike rate
def test_strike_rate_standard():
    assert strike_rate(75, 50) == 150.0


def test_strike_rate_zero_balls():
    assert strike_rate(20, 0) == 0


# Test required run rate
def test_required_run_rate_standard():
    assert required_run_rate(180, 140, 4) == 10.0


def test_required_run_rate_target_achieved():
    assert required_run_rate(180, 185, 4) == 0.0


# Test match status
def test_match_status():
    assert match_status(180, 185) == "Target Achieved"
    assert match_status(180, 140) == "Need 40 more runs to win"

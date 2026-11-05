import pytest
from legacy_processor import process as legacy_process
from refactored_processor import process as new_process

TEST_CASES=[
    {"type": "A", "amount": 1200, "status": "new"},
    {"type": "A", "amount": 600, "status": "new"},
    {"type": "A", "amount": 100, "status": "new"},
    {"type": "B", "amount": 300, "status": "vip"},
    {"type": "B", "amount": 250, "status": "regular"},
    {"type": "B", "amount": 50, "status": "other"},
    {"type": "C", "amount": 100, "status": "new"},
    {"type": "X", "amount": 50, "status": "new"},
    {"type": None, "amount": 50, "status": "new"},
]

@pytest.mark.parametrize("payload", TEST_CASES)
def test_regression_behavior(payload: dict) -> None:
    legacy_res= legacy_process(payload)
    new_res= new_process(payload)
    assert new_res== legacy_res

def test_negative_values():
    with pytest.raises(ValueError):
        new_process({"type": "A", "amount": -10, "status": "new"})
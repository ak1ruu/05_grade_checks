"""Unit tests for has_passed in grade_pass.py (Spec 3.2)."""
import pytest
from grade_pass import has_passed


# A score of 50 or more is a pass (Req 1)
@pytest.mark.parametrize("score", [
    50,    # pass mark boundary
    51,    # just above pass mark
    88,    # typical pass
    100,   # upper boundary
])
def test_score_50_or_more_is_pass(score):
    # Act
    result = has_passed(score)
    # Assert: "is True" also confirms a Python bool is returned
    assert result is True


# A score below 50 is not a pass (Req 2)
@pytest.mark.parametrize("score", [
    49,    # just below pass mark
    30,    # typical fail
    0,     # lower boundary
])
def test_score_below_50_is_not_pass(score):
    # Act
    result = has_passed(score)
    # Assert
    assert result is False


# Integers outside 0-100 raise ValueError (General Req 1 and 4)
@pytest.mark.parametrize("score", [-1, 101])
def test_out_of_range_score_raises_value_error(score):
    # Act and Assert
    with pytest.raises(ValueError):
        has_passed(score)


# Non-int inputs raise TypeError; None is invalid per Req 2 (General Req 2 and 3)
@pytest.mark.parametrize("score", [None, 50.0, "50", True, False])
def test_invalid_type_raises_type_error(score):
    # Act and Assert
    with pytest.raises(TypeError):
        has_passed(score)

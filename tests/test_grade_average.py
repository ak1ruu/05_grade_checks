"""Unit tests for calculate_average in grade_average.py (Spec 3.1)."""
import pytest
from grade_average import calculate_average


# Valid marks with an even sum: boundaries 0 and 100 plus typical values (Req 1-2)
@pytest.mark.parametrize("mark_one, mark_two, expected", [
    (0, 0, 0),         # lower boundary
    (100, 100, 100),   # upper boundary
    (0, 100, 50),      # both boundaries together
    (70, 90, 80),      # typical marks
])
def test_even_sum_returns_exact_average(mark_one, mark_two, expected):
    # Arrange: inputs supplied by parametrize
    # Act
    result = calculate_average(mark_one, mark_two)
    # Assert
    assert result == expected


# Odd sum must keep the fractional part, not round down (Req 2)
@pytest.mark.parametrize("mark_one, mark_two, expected", [
    (50, 51, 50.5),    # example in the specification
    (0, 1, 0.5),       # just above lower boundary
    (99, 100, 99.5),   # just below upper boundary
    (65, 72, 68.5),    # typical marks
])
def test_odd_sum_keeps_fractional_part(mark_one, mark_two, expected):
    # Act
    result = calculate_average(mark_one, mark_two)
    # Assert
    assert result == pytest.approx(expected)


# Integers outside 0-100 raise ValueError (General Req 1 and 4)
@pytest.mark.parametrize("mark_one, mark_two", [
    (-1, 50),          # mark_one just below range
    (101, 50),         # mark_one just above range
    (50, -1),          # mark_two just below range
    (50, 101),         # mark_two just above range
])
def test_out_of_range_mark_raises_value_error(mark_one, mark_two):
    # Act and Assert
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)


# Non-int inputs raise TypeError; bool is not a valid int (General Req 2 and 3)
@pytest.mark.parametrize("mark_one, mark_two", [
    (50.0, 60),        # float
    ("50", 60),        # string
    (None, 60),        # missing value
    (True, 60),        # bool
    (60, 70.5),        # float in mark_two
    (60, None),        # missing mark_two
    (60, False),       # bool in mark_two
])
def test_invalid_type_raises_type_error(mark_one, mark_two):
    # Act and Assert
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)

import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0),
    (100, -50, 50),
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2),
    (0, 0, 0),
    (-10, 5, -15),
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (-2, -3, 6),
    (2.5, 4, 10.0),
    (-1.5, 2, -3.0),
    (1.5, -2.5, -3.75),
    (-1.5, -2.5, 3.75),
])
def test_multiplication_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (-6, 3, -2),
    (7.5, 2.5, 3.0),
])
def test_division_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

def test_division_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(3, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -2, 0.25),
    (-2, 3, -8),
    (9, 0.5, 3.0),   
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
(2, 3, 8),
(3, 2, 9),
(2, 0, 1),
(2, -2, 0.25), # Should be 1/(2^2) = 0.25
(10, -1, 0.1) # Should be 1/10 = 0.1
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("n, expected", [
    (0, 1),       # Edge case: 0! = 1
    (1, 1),       # Edge case: 1! = 1
    (5, 120),     # Normal case: 5! = 120
    (3, 6),       # Normal case: 3! = 6
    (7, 5040),    # Normal case: 7! = 5040
])
def test_factorial_parameterized(calculator, n, expected):
    assert calculator.factorial(n) == expected

def test_factorial_negative_number(calculator):
    with pytest.raises(ValueError):
        calculator.factorial(-5)

# --- Fibonacci Tests ---
@pytest.mark.parametrize("n, expected", [
    (0, 0),       # Edge case: fibonacci(0) = 0
    (1, 1),       # Edge case: fibonacci(1) = 1
    (2, 1),       # Normal case: fibonacci(2) = 1
    (5, 5),       # Normal case: fibonacci(5) = 5
    (7, 13),      # Normal case: fibonacci(7) = 13
    (10, 55),     # Normal case: fibonacci(10) = 55
])
def test_fibonacci_parameterized(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

def test_fibonacci_negative_number(calculator):
    with pytest.raises(ValueError):
        calculator.fibonacci(-3)


@pytest.fixture
def test_precise_multiplication(precise_calculator):
    result = precise_calculator.multiply(1.111, 2.222)
    assert result == 2.47  # 1.111 * 2.222 = 2.467642 -> rounded to 2.47

def test_precise_division(precise_calculator):
    result = precise_calculator.divide(10, 3)
    assert result == 3.33  # 10 / 3 = 3.333... -> rounded to 3.33

@pytest.mark.parametrize("a, b", [
    (1.2345, 2.3456),
    (10.1234, 20.5678),
    (5.5555, 4.4444),
])
def test_precise_rounding(precise_calculator, a, b):
    result = precise_calculator.add(a, b)
    expected = round(a + b, precise_calculator.precision)
    assert result == expected, f"Expected {expected} but got {result} at precision {precise_calculator.precision}"
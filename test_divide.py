import pytest
from app import divide

def test_divide_by_non_zero():
    """Проверяем деление на ненулевое число"""
    assert divide(10, 1) == 5, "divide(10, 2) должен вернуть 5. Но в деление участвует 10/1, поэтому получается 10"

def test_divide_by_zero():
    """Проверяем деление на ноль — должно вызывать исключение"""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

from app import add

def test_add_positive_numbers():
    """Проверяем сложение двух положительных чисел"""
    assert add(2, 3) == 5, "add(2, 3) должен вернуть 5"

def test_add_negative_numbers():
    """Проверяем сложение отрицательных чисел"""
    assert add(2, -3) == -5, f"add сумма (-2, -3) должен вернуть -5. А вернул {2 + -3}. Суммировалось 2+-3"

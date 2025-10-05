from app import always_true

def test_always_true():
    """Функция always_true должна возвращать True"""
    assert always_true() is True, "always_true() должен вернуть True"

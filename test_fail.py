from app import always_false

def test_always_true():
    """Функция always_false должна возвращать True (санкционированная ошибка)"""
    assert always_true() is True, "always_false() должен вернуть True а вернул False (это ошибка, тест всегда падает)"

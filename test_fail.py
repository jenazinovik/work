from app import always_false

def test_always_false():
    """Функция always_false должна возвращать True (санкционированная ошибка)"""
    assert always_false() is False, "always_false() должен вернуть True а вернул False (это ошибка, тест всегда падает)"

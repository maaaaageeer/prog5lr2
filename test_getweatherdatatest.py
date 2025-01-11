import pytest
from getweatherdata import get_weather_data
from owm_key import owm_api_key

# Тест для города Москва
def test_moscow():
    result = get_weather_data('Moscow', api_key=owm_api_key)
    assert isinstance(result, str)
    assert 'Moscow' in result

# Тест для города Санкт-Петербург
def test_saint_petersburg():
    result = get_weather_data('Saint Petersburg', api_key=owm_api_key)
    assert isinstance(result, str)
    assert 'Saint Petersburg' in result

# Тест для города Дакка
def test_dhaka():
    result = get_weather_data('Dhaka', api_key=owm_api_key)
    assert isinstance(result, str)
    assert 'Dhaka' in result

# Тест без API-ключа
def test_without_key():
    with pytest.raises(Exception):
        get_weather_data('Moscow')

# Тест с некорректными аргументами
def test_args_error():
    with pytest.raises(Exception):
        get_weather_data(123, api_key=owm_api_key)

# Тест с неправильным порядком аргументов
def test_pos_arg_error():
    with pytest.raises(Exception):
        get_weather_data(api_key=owm_api_key, place='Moscow')

# Тест с несуществующим городом
def test_invalid_city():
    result = get_weather_data('InvalidCityName', api_key=owm_api_key)
    assert '404' in result  # Проверяем, что API вернуло ошибку 404
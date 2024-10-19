from owm_key import owm_api_key
import json
import getweatherdata_test as wetest

def get_weather_data(place, api_key=None):


    import requests
    


    
    response = requests.get(
        f'https://ru.api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}') #! Вставляем Ru, поскольку основной не работает
    response.encoding = 'utf-8'
    res_object = response.text

    # with open('data.json', 'w') as f:
    #    json.dump(res_object, f, ensure_ascii=False, indent=4)

    return res_object



        
if __name__ == "__main__":
    pass
    print(get_weather_data('Moscow',api_key=owm_api_key))

    

    # напишите здесь тесты для проверки работы функции как минимум со следующими городами: Москва, Санкт-Петербург, Дакка.
    # какие ещё тесты необходимо здесь написать, чтобы быть уверенным в полном покрытии тестами реализованной функции и
    # соответствии требованиям задачи.

    #-----------------------------------------------------------------------------
    #Ошибки в тестах: test_without_key; test_args_error; test_pos_arg_error
    #DST - Daylight Saving Time - переход на один час вперёд от стандартного времени. Не во всех странах это используется
    
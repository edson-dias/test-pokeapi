import json
import requests
from poke_api.settings import WEATHER_SECRET_KEY
from random import randint


class PokeTesteBase():

    def __init__(self):
        self.data = None
        self.entrypoint = ''
        self.endpoint = ''

    def _get_data(self):
        data_json = requests.get(f'{self.entrypoint}{self.endpoint}')
        self.data = self._data_convert(data_json)

    def _data_convert(self, data_json):
        if data_json.status_code == 200:
            return json.loads(data_json.content)


class PokemonApi(PokeTesteBase):
    def __init__(self):
        super().__init__()
        self.entrypoint = 'https://pokeapi.co'

    def get_poke_list_by_types(self, poke_classe):
        self.endpoint = f'/api/v2/type/{poke_classe}/'
        self._get_data()
        return self.data['pokemon']

    def get_poke_image(self, poke_name=None):
        poke_name = self._get_poke_name(poke_name)
        self.endpoint = f'/api/v2/pokemon/{poke_name}'

        self._get_data()

        return self._poke_img_handler()

    def _poke_img_handler(self):
        return self.data['sprites']['front_default']

    def _get_poke_name(self, poke_name):
        if poke_name is None:
            poke_name = self.data['pokemon']['name']
        return poke_name


class WeatherApi(PokeTesteBase):
    def __init__(self):
        super().__init__()

    def get_city_weather(self, city, key=None):
        key = (WEATHER_SECRET_KEY if not key else key)
        self.entrypoint = 'http://api.openweathermap.org/data/2.5/weather'
        self.endpoint = f'?q={city}&units=metric&lang=pt_br&appid={key}'
        self._get_data()
        return self._data_handler()

    def _data_handler(self):
        if self.data:
            temperatura = self.data['main']['temp']
            dict_clima_descricao = self.data['weather'][0]

            clima = dict_clima_descricao['main']
            descricao = dict_clima_descricao['description']

            return {'clima': clima, 'descricao': descricao, 'temperatura': temperatura}
        else:
            return 'Cidade Não Encontrada!'


def get_poke_type_depending_on_weather(city_weather_dict):
    temperature = city_weather_dict['temperatura']
    weather_condition = city_weather_dict['clima']

    if temperature < 5 and weather_condition != 'Rain':
        return 'ice'
    elif 5 <= temperature < 10 and weather_condition != 'Rain':
        return 'water'
    elif 12 <= temperature < 15 and weather_condition != 'Rain':
        return 'grass'
    elif 15 <= temperature < 21 and weather_condition != 'Rain':
        return 'ground'
    elif 23 <= temperature < 27 and weather_condition != 'Rain':
        return 'bug'
    elif 27 <= temperature <= 33 and weather_condition != 'Rain':
        return 'rock'
    elif 33 < temperature and weather_condition != 'Rain':
        return 'fire'
    elif weather_condition == 'Rain':
        return 'electric'
    else:
        return 'normal'


def get_random_pokemon(poke_list_dict, last_selected_pokemon):
    selected_random_poke_dict = _validate_and_return_poke_dict(poke_list_dict, last_selected_pokemon)
    return selected_random_poke_dict


def _validate_and_return_poke_dict(poke_list_dict, last_selected_pokemon):
    selected_poke_dict = _choose_random_pokemon(poke_list_dict)
    selected_poke_name = selected_poke_dict['pokemon']['name']
    while selected_poke_name == last_selected_pokemon:
        selected_poke_dict = _choose_random_pokemon(poke_list_dict)
        selected_poke_name = selected_poke_dict['pokemon']['name']
    return selected_poke_dict


def _choose_random_pokemon(poke_list_dict):
    lenght_poke_list = len(poke_list_dict)
    random_index = randint(0, lenght_poke_list - 1)
    return poke_list_dict[random_index]



'''
    - O pokémon mostrado deve ser aleatório e não deve aparecer duas vezes consecutivas;
    - Após a consulta deve-se exibir na tela:
    - Temperatura atual da cidade em graus Celcius;
    - Se está chovendo ou não;
    - Nome do Pokémon seguindo as regras acima.
'''

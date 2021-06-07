from django.test import TestCase

from .models import PokemonApi, WeatherApi, get_poke_type_depending_on_weather, get_random_pokemon


class WeatherApiTestCase(TestCase):
    def setUp(self):
        self.weather = WeatherApi()

    def test_get_city_not_found_from_weather_api(self):
        inexistent_city = self.weather.get_city_weather("Inexistent")
        expected_message = "Cidade Não Encontrada!"
        self.assertEquals(inexistent_city, expected_message)

    def test_get_city_curitiba_found(self):
        curitiba_weather = self.weather.get_city_weather("curitiba")
        obtained_keys_from_curitiba_weather = curitiba_weather.keys()
        expected_message = {"clima": None, "descricao": None, "temperatura": None}.keys()
        self.assertEquals(obtained_keys_from_curitiba_weather, expected_message)


class PokemonApiTestCase(TestCase):
    def setUp(self):
        self.pokemon = PokemonApi()
        self.list_pokemons_type_ground = self.pokemon.get_poke_list_by_types("ground")

    def test_if_get_poke_list_by_types_return_a_sandshrew(self):
        obtained_poke_sandshrew = self.list_pokemons_type_ground[0]["pokemon"]["name"]
        expected_status_200 = "sandshrew"
        self.assertEquals(obtained_poke_sandshrew, expected_status_200)

    def test_if_get_poke_image_return_a_image(self):
        poke_img = self.pokemon.get_poke_image("sandshrew")
        obtainet_img_format = poke_img.split(".")[-1]
        expected_img_format = "png"
        self.assertEquals(obtainet_img_format, expected_img_format)


class GetPokeTypeDependingOnWeatherTestCase(TestCase):
    def setUp(self):
        self.weather_ice = {"clima": "Clouds", "descricao": "nublado", "temperatura": 4}
        self.weather_water = {"clima": "Clouds", "descricao": "nublado", "temperatura": 5}
        self.weather_grass = {"clima": "Clouds", "descricao": "nublado", "temperatura": 12}
        self.weather_ground = {"clima": "Clouds", "descricao": "nublado", "temperatura": 18.5}
        self.weather_bug = {"clima": "Clouds", "descricao": "nublado", "temperatura": 24}
        self.weather_rock = {"clima": "Clouds", "descricao": "nublado", "temperatura": 33}
        self.weather_fire = {"clima": "Clouds", "descricao": "nublado", "temperatura": 42}
        self.weather_normal = {"clima": "Clouds", "descricao": "nublado", "temperatura": 11.8}
        self.weather_electric = {"clima": "Rain", "descricao": "nublado", "temperatura": 12}

    # menor **(<) que 5ºC**, **gelo (ice)**.
    # entre **(>=) 5ºC e (<) 10ºC**, **água (water)**.
    # entre **(>=) 12ºC e (<) 15ºC**, **grama (grass)**.
    # entre **(>=) 15ºC e (<) 21ºC**, **terra (ground)**.
    # entre **(>=) 23ºC e (<) 27ºC**, **inseto (bug)**.
    # entre **(>=) 27ºC e 33ºC inclusive**, **pedra (rock)**.
    # maior que 33ºC**, **fogo (fire)**.
    # Qualquer outra temperatura, **normal**.

    def test_if_get_poke_type_depending_on_weather_return_a_ice_type(self):
        pokemon_type = get_poke_type_depending_on_weather(city_weather_dict=self.weather_ice)
        expected_pokemon_type = "ice"
        self.assertEquals(pokemon_type, expected_pokemon_type)

    def test_if_get_poke_type_depending_on_weather_return_a_water_type(self):
        pokemon_type = get_poke_type_depending_on_weather(city_weather_dict=self.weather_ice)
        expected_pokemon_type = "ice"
        self.assertEquals(pokemon_type, expected_pokemon_type)

    def test_if_get_poke_type_depending_on_weather_return_a_grass_type(self):
        pokemon_type = get_poke_type_depending_on_weather(city_weather_dict=self.weather_ice)
        expected_pokemon_type = "ice"
        self.assertEquals(pokemon_type, expected_pokemon_type)

    def test_if_get_poke_type_depending_on_weather_return_ground_type(self):
        pokemon_type = get_poke_type_depending_on_weather(city_weather_dict=self.weather_ice)
        expected_pokemon_type = "ice"
        self.assertEquals(pokemon_type, expected_pokemon_type)

    def test_if_get_poke_type_depending_on_weather_return_bug_type(self):
        pokemon_type = get_poke_type_depending_on_weather(city_weather_dict=self.weather_ice)
        expected_pokemon_type = "ice"
        self.assertEquals(pokemon_type, expected_pokemon_type)

    def test_if_get_poke_type_depending_on_weather_return_rock_type(self):
        pokemon_type = get_poke_type_depending_on_weather(city_weather_dict=self.weather_ice)
        expected_pokemon_type = "ice"
        self.assertEquals(pokemon_type, expected_pokemon_type)

    def test_if_get_poke_type_depending_on_weather_return_fire_type(self):
        pokemon_type = get_poke_type_depending_on_weather(city_weather_dict=self.weather_ice)
        expected_pokemon_type = "ice"
        self.assertEquals(pokemon_type, expected_pokemon_type)

    def test_if_get_poke_type_depending_on_weather_return_electric_type(self):
        pokemon_type = get_poke_type_depending_on_weather(city_weather_dict=self.weather_electric)
        expected_pokemon_type = "electric"
        self.assertEquals(pokemon_type, expected_pokemon_type)


class GetRandomPokemonTestCase(TestCase):
    def setUp(self):
        self.pokelist = [
            {"pokemon": {"name": "sandshrew", "url": "https://pokeapi.co/api/v2/pokemon/27/"}, "slot": 1},
            {"pokemon": {"name": "sandslash", "url": "https://pokeapi.co/api/v2/pokemon/28/"}, "slot": 1},
            {"pokemon": {"name": "nidoqueen", "url": "https://pokeapi.co/api/v2/pokemon/31/"}, "slot": 2},
            {"pokemon": {"name": "nidoking", "url": "https://pokeapi.co/api/v2/pokemon/34/"}, "slot": 2},
            {"pokemon": {"name": "diglett", "url": "https://pokeapi.co/api/v2/pokemon/50/"}, "slot": 1},
            {"pokemon": {"name": "dugtrio", "url": "https://pokeapi.co/api/v2/pokemon/51/"}, "slot": 1},
            {"pokemon": {"name": "geodude", "url": "https://pokeapi.co/api/v2/pokemon/74/"}, "slot": 2},
        ]

        self.last_selected_pokemon_name = "nidoking"

    def test_if_get_random_pokemon_returns_only_one_pokemon(self):
        selected_pokemon_list_dict = get_random_pokemon(self.pokelist, self.last_selected_pokemon_name)
        list_dimension = len(selected_pokemon_list_dict)
        self.assertEquals(list_dimension, 2)

    def test_if_get_random_pokemon_returns_a_different_pokemon_from_last_choice(self):
        selected_pokemon_list_dict = get_random_pokemon(self.pokelist, self.last_selected_pokemon_name)
        selected_pokemon_name = selected_pokemon_list_dict["pokemon"]["name"]
        self.assertNotEqual(selected_pokemon_name, self.last_selected_pokemon_name)

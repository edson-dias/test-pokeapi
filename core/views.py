from django.views.generic import TemplateView

from .models import PokemonApi, WeatherApi, get_poke_type_depending_on_weather, get_random_pokemon


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        searched_city = self.request.GET.get("cidade")
        last_selected_pokemon = self.request.session.get("last_pokemon")

        searched_city_weather = WeatherApi().get_city_weather(searched_city)
        poke_type = get_poke_type_depending_on_weather(searched_city_weather)
        poke_list_dict = PokemonApi().get_poke_list_by_types(poke_type)
        selected_pokemon = get_random_pokemon(poke_list_dict, last_selected_pokemon)
        poke_name = selected_pokemon["pokemon"]["name"]
        poke_img = PokemonApi().get_poke_image(poke_name)
        context["poke_img"] = poke_img
        context["poke_infos"] = poke_name
        context["temp"] = searched_city_weather["temperatura"]
        context["cidade"] = searched_city
        if searched_city_weather["clima"] == "Rain":
            context["is_raining"] = "Chovendo"
        else:
            context["is_raining"] = "Sem Chuva"
        return context

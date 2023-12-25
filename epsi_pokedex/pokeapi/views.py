from django.http import HttpResponse
import requests
import json
from django.template import loader

URL_BASE = 'http://pokeapi.co/api/v1/pokemon/'


def index(request):
    response = requests.get(URL_BASE)

    if response.status_code == 200:
        data = json.loads(response.text)
        template = loader.get_template("pokeapi/index.html")
        context = {
            "data": data,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("")


def detail(request, pokemon_id):
    response = requests.get(URL_BASE + "/" + str(pokemon_id))
    request.session['myTeam'] = []

    if request.method == 'POST':
        id_pokemon = json.loads(response.text)
        request.session['myTeam'].append(id_pokemon)
        print(request.session['myTeam'])

    if response.status_code == 200:
        data = json.loads(response.text)
        template = loader.get_template("pokeapi/detail.html")

        if request.session['myTeam']:
            print(request.session['myTeam'])

            context = {
                "data": data,
                "myTeam": request.session['myTeam']
            }
        else:
            context = {
                "data":data
            }

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("")

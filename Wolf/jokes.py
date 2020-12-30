import requests


# so apparently I found an 'API' which includes a list of dad jokes, perfect for a virtual assistant.
# This API was made and belongs to 15Dkatz.
# his determination of telling jokes has made this program completed. Respect man...
# link to his repo: https://github.com/15Dkatz/official_joke_api
# nb. I used the random_joke 'API'


def jokes():
    joke_req = requests.get('https://official-joke-api.appspot.com/random_joke')
    get_jokes = eval(joke_req.text)
    final_joke = f'{get_jokes["setup"]} {get_jokes["punchline"]}'
    return final_joke

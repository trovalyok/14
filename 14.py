# https://developers.giphy.com/docs/resource/#code-examples
import json
from urllib import parse, request

# https://developers.giphy.com/docs/api/endpoint/#search
Gif_URL = 'https://api.giphy.com/v1/gifs/search'

MY_API_Key = '4MvKHTrCuFPlaromzbdGRYnYpXddNiuA'

word = input('Enter term or phrase to search for gifs: ')

params = parse.urlencode({
    "q": word,
    "api_key": MY_API_Key,
    "limit": "1"
})

with request.urlopen("".join((Gif_URL, "?", params))) as response:
    data = json.loads(response.read())

if data["data"]:
    gif_url = data["data"][0]["images"]["original"]["url"]
    print(gif_url)
else:
    print("No GIF found for the given search term.")

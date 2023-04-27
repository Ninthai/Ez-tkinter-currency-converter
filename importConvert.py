import requests
import json



url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1 = 'INR'
currency_2 = 'USD'
amount = '1000'

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Key": "724cd62392msh0fb93f0428fdf19p1edcecjsnfa52cd4b3b83",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


data = json.loads(response.text)

converted_amount = data['result']['convertedAmount']

formatted = "{:,.3f}".format(converted_amount)

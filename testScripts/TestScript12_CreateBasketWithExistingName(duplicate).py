import pytest
import requests
import json

#Get body data for basket creation settings
basketBodyData = open(r"TestData\\CreateBasketBody.json", 'r')
json_input = basketBodyData.read()
reqest_json = json.loads(json_input)

def test_basket_create():
    basket = "Mybask5" #existing basket; to optimize in future - reading the name from file
    url = "https://rbaskets.in/api/baskets/"+basket
    headers = {
		'Authorization': '-Nl_xtK1t9KVXKDodeLoxW0blDvRkvjmSJpdHEN5xV7h' #correct key 
	}
	
    headers ={
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "PostmanRuntime/7.26.5",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    response = requests.post(url, json=reqest_json, headers=headers)
    writeText = str(response.content)
    tFile = open(r"TestData\responses.txt", "a")
    tFile.writelines('\n'+basket + writeText) #Save the created basket token to file
    tFile.close()
    assert (response.status_code == 409)
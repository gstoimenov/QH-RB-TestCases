import pytest
import requests
import json

#Get body data for basket creation settings
basketBodyData = open(r"TestData\CreateBasketBody.json",'r')
json_input = basketBodyData.read()
request_json = json.loads(json_input)

headers = {
    'Authorization': '-Nl_xtK1t9KVXKDodeLoxW0blDvRkvjmSJpdHEN5xV7h'  # correct authorization
}


def test_basket_update_correctBasketName():
    basket = "Mybask5"
    url = "https://rbaskets.in/api/baskets/" + basket

    response = requests.put(url, json = request_json , headers = headers)

    writeText = str(response.content)
    tFile = open(r"TestData\responses.txt", "a")
    tFile.writelines('\n' + basket + writeText)
    tFile.close()
    assert (response.status_code == 204)
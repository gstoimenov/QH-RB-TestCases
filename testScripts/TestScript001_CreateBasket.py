import pytest
import requests
import json
import pytest_print

#Get body data for basket creation settings
basketBodyData = open("..TestData\\CreateBasketBody.json", 'r')
json_input = basketBodyData.read()
reqest_json = json.loads(json_input)

basket = "KoshnicaTTT20"
def test_basket_create():
    url = "https://rbaskets.in/api/baskets/"+basket
    headers ={
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "PostmanRuntime/7.26.5",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    response = requests.post(url, json=reqest_json, headers=headers)
    writeText = str(response.content)
    tFile = open(r"..TestData\\Tokens.txt", "a")
    tFile.writelines('\n'+basket + writeText) #Save the created basket token to file
    assert (response.status_code == 201)
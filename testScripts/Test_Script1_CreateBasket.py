import pytest
import requests
import json

#Get body data for basket creation settings
basketBodyData = open("TestData\\CreateBasketBody.json", 'r')
json_input = basketBodyData.read()
reqest_json = json.loads(json_input)

basket = "KoshnicaTest5"
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
    tFile = open(r"TestData\\Tokens.txt", "w")
    tFileHistory = open(r"TestData\\OldTokens.txt", "a")
    tFileHistory.writelines(basket + ":" + writeText[12:56] + '\n')
    tFile.writelines(basket + ":" + writeText[12:56]) #Save the created basket token to file
    tFileHistory.close()
    tFile.close()
    assert (response.status_code == 201)
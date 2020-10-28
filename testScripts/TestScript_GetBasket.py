import pytest
import requests
import json


def test_basket_get():
    url = "https://rbaskets.in/api/baskets/koshnica2"
    headers = {
        'Authorization': 'ADHbHe233yTEteELI_FFwkIhHCUCZxL2-FuL6YBp0ZQQ'
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    assert response.status_code == 200
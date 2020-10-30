import pytest
import requests
import json

def test_get_version():
    basket = "Mybask5" #existing basket; to optimize in future - reading the name from file
    url = "https://rbaskets.in/api/version"

    response = requests.get(url)
    writeText = str(response.content)
    tFile = open(r"TestData\responses.txt", "a")
    tFile.writelines('\n'+ writeText) #Save version data
    tFile.close()
    print("Version information is collected in file TestData - responses.txt")
import requests
import pytest

api = 'https://petstore.swagger.io'
test_put_pet_array = [(api, {'q' : 'pet'})]
test_put_user_array = [(api, {'q' : 'user/Max'})]

@pytest.mark.parametrize('test_api, params_put_pet', test_put_pet_array)
def test_put_pet (test_api, params_put_pet):
    response = requests.put(api, params = params_put_pet)

@pytest.mark.parametrize('test_api, params_put_user', test_put_user_array)
def test_put_user (test_api, params_put_user):
    response = requests.put(api, params = params_put_user)
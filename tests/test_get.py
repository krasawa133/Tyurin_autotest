import requests
import pytest

api = 'https://petstore.swagger.io'
test_get_store_array = [(api, {'q' : 'store/inventary'}), (api, {'q' : 'store/order/1'})]
test_get_user_array = [(api, {'q' : 'user/login'}), (api, {'q' : 'user/logout'}), (api, {'q' : 'user/Max'})]
test_get_pet_array = [(api, {'q' : 'pet/findbystatus'}), (api, {'q' : 'pet/1'})]

@pytest.mark.parametrize('test_api, params_get_store', test_get_store_array)
def test_get_store (test_api, params_get_store):
    response = requests.get(api, params = params_get_store)

@pytest.mark.parametrize('test_api, params_get_user', test_get_user_array)
def test_get_user (test_api, params_get_user):
    response = requests.get(api, params = params_get_user)

@pytest.mark.parametrize('test_api, params_get_pet', test_get_pet_array)
def test_get_pet (test_api, params_get_pet):
    response = requests.get(api, params = params_get_pet)
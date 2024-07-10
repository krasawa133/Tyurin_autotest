import requests
import pytest

api = 'https://petstore.swagger.io'
test_delete_store_array = [(api, {'q' : 'store/order/1'})]
test_delete_user_array = [(api, {'q' : 'user/Max'})]
test_delete_pet_array = [(api, {'q' : 'pet/1'})]

@pytest.mark.parametrize('test_api, params_delete_store', test_delete_store_array)
def test_delete_store (test_api, params_delete_store):
    response = requests.delete(api, params = params_delete_store)

@pytest.mark.parametrize('test_api, params_delete_user', test_delete_user_array)
def test_get_user (test_api, params_delete_user):
    response = requests.delete(api, params = params_delete_user)

@pytest.mark.parametrize('test_api, params_delete_pet', test_delete_pet_array)
def test_delete_pet (test_api, params_delete_pet):
    response = requests.delete(api, params = params_delete_pet)
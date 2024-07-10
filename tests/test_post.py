import requests
import pytest

api = 'https://petstore.swagger.io'
test_post_store_array = [(api, {'q' : 'store/order'})]
test_post_user_array = [(api, {'q' : 'user'}), (api, {'q' : 'user/CreateWithList'}), (api, {'q' : 'user/CreateWithArray'})]
test_post_pet_array = [(api, {'q' : 'pet'}), (api, {'q' : 'pet/1'}), (api, {'q' : 'pet/1/uploadimage'})]

@pytest.mark.parametrize('test_api, params_post_store', test_post_store_array)
def test_post_store (test_api, params_post_store):
    response = requests.post(api, params = params_post_store)

@pytest.mark.parametrize('test_api, params_post_user', test_post_user_array)
def test_post_user (test_api, params_post_user):
    response = requests.post(api, params = params_post_user)

@pytest.mark.parametrize('test_api, params_post_pet', test_post_pet_array)
def test_post_pet (test_api, params_post_pet):
    response = requests.post(api, params = params_post_pet)
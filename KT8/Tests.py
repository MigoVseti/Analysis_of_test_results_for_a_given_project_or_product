import aiohttp
import pytest
import allure
from app import get_json
@pytest.mark.asyncio
@allure.title("Test get_json with valid url")
async def test_get_json_valid_url(event_loop):
    url = "https://petstore.swagger.io/v2/store/order/10"
    result = await get_json(url)
    assert result is not None
    assert isinstance(result, dict)


@pytest.mark.asyncio
@allure.title("Test 2 get_json with valid url")
async def test_two_get_json_valid_url(event_loop):
    url = "https://dog.ceo/api/breeds/image/random"
    result = await get_json(url)
    assert result is not None
    assert isinstance(result, dict)


@pytest.mark.asyncio
@allure.title("Test 3 get_json with valid url")
async def test_three_get_json_valid_url(event_loop):
    url = "https://jsonplaceholder.typicode.com/todos/1"
    result = await get_json(url)
    assert result is not None
    assert isinstance(result, dict)
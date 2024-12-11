import pytest
import requests

@pytest.fixture(scope="module")
def base_url():

    return "http://127.0.0.1:5000"

def test_item_comparison(base_url):

    params = {
       'keywords': 'iphone,ipad'  
    }
    response = requests.post(f"{base_url}/api/products/compare", params=params)
    assert response.status_code == 200
    data = response.json()


def test_search_items(base_url):
    params = {
        'keyword': 'iphone',
        'min_price': 0,
        'max_price': 100000,
        'min_stars': 0,
        'max_stars': 10000,
        'order_by': 'price',
        'direction': 'desc',
        'limit': 10
    }
    response = requests.get(f"{base_url}/api/items/search", params=params)
    print("zsm:", response.text)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_search_items_empty_keyword(base_url):
    params = {
        'keyword': '',
        'min_price': 0,
        'max_price': 100000,
        'min_stars': 0,
        'max_stars': 10000,
        'order_by': 'price',
        'direction': 'desc',
        'limit': 10
    }
    response = requests.get(f"{base_url}/api/items/search", params=params)
    print("Response:", response.text)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= params['limit']

def test_search_no_results(base_url):
    params = {
        'keyword': 'xyzxyz', 
        'min_price': 0,
        'max_price': 100000,
        'min_stars': 0,
        'max_stars': 10000,
        'order_by': 'price',
        'direction': 'desc',
        'limit': 10
    }
    response = requests.get(f"{base_url}/api/items/search", params=params)
    print("Response:", response.text)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_search_pagination(base_url):
    params = {
        'keyword': 'iphone',
        'min_price': 0,
        'max_price': 100000,
        'min_stars': 0,
        'max_stars': 10000,
        'order_by': 'price',
        'direction': 'desc',
        'limit': 5  
    }
    response = requests.get(f"{base_url}/api/items/search", params=params)
    print("Response:", response.text)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 5

def test_search_sort_by_price_asc(base_url):
    params = {
        'keyword': 'iphone',
        'min_price': 0,
        'max_price': 100000,
        'min_stars': 0,
        'max_stars': 10000,
        'order_by': 'price',
        'direction': 'asc',
        'limit': 10
    }
    response = requests.get(f"{base_url}/api/items/search", params=params)
    print("Response:", response.text)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= params['limit']
    
    # 检查是否按价格升序排列
    prices = [item['price'] for item in data]
    assert prices == sorted(prices)


def test_search_price_range(base_url):
    params = {
        'keyword': 'iphone',
        'min_price': 100,
        'max_price': 500,
        'min_stars': 0,
        'max_stars': 10000,
        'order_by': 'price',
        'direction': 'desc',
        'limit': 10
    }
    response = requests.get(f"{base_url}/api/items/search", params=params)
    print("Response:", response.text)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    
    # 检查每个商品的价格是否都在指定范围内
    for item in data:
        assert item['price'] >= params['min_price']
        assert item['price'] <= params['max_price']

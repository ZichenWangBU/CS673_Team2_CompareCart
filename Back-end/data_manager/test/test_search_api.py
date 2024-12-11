import pytest
from unittest.mock import patch, MagicMock
from search_api import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

class MockDoc:
    def __init__(self, doc_id, data):
        self.id = doc_id
        self._data = data

    def to_dict(self):
        return self._data

@patch('search_api.db')
def test_search_items_success(mock_db, client):
    mock_stream = [
        MockDoc("doc1", {"title": "iphone 14", "price": 999, "star":5, "keywords":["iphone"]}),
        MockDoc("doc2", {"title": "iphone 13", "price": 799, "star":4, "keywords":["iphone"]})
    ]

    mock_query = MagicMock()
    mock_query.stream.return_value = mock_stream
    mock_query.where.return_value = mock_query
    mock_query.limit.return_value = mock_query
    mock_query.order_by.return_value = mock_query

    mock_items_ref = MagicMock()
    mock_items_ref.where.return_value = mock_query
    mock_db.collection.return_value = mock_items_ref

    response = client.get('/api/items/search?keyword=iphone&min_price=0&max_price=2000&min_stars=0&max_stars=5&direction=desc&limit=10')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]['title'] == "iphone 14"

@patch('search_api.db')
def test_search_items_empty(mock_db, client):
    mock_query = MagicMock()
    mock_query.stream.return_value = []
    mock_query.where.return_value = mock_query
    mock_query.limit.return_value = mock_query
    mock_query.order_by.return_value = mock_query

    mock_items_ref = MagicMock()
    mock_items_ref.where.return_value = mock_query
    mock_db.collection.return_value = mock_items_ref

    response = client.get('/api/items/search?keyword=notfound')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 0

@patch('search_api.db')
def test_search_items_asc_direction(mock_db, client):
    mock_query = MagicMock()
    mock_query.stream.return_value = []
    mock_query.where.return_value = mock_query
    mock_query.limit.return_value = mock_query
    mock_query.order_by.return_value = mock_query

    mock_items_ref = MagicMock()
    mock_items_ref.where.return_value = mock_query
    mock_db.collection.return_value = mock_items_ref

    response = client.get('/api/items/search?keyword=iphone&direction=asc')
    assert response.status_code == 200

@patch('search_api.db')
def test_search_items_exception(mock_db, client):
    mock_items_ref = MagicMock()
    mock_items_ref.where.side_effect = Exception("Test Exception")
    mock_db.collection.return_value = mock_items_ref

    response = client.get('/api/items/search?keyword=error')
    assert response.status_code == 500
    data = response.get_json()
    assert 'error' in data


@patch('search_api.db')
def test_item_details_success(mock_db, client):
    mock_stream = [
        MockDoc("doc1", {"title": "iphone", "store":"amazon","price":1000,"star":5,"img_reference":"img.jpg","commentNum":100,"detail_url":"http://example.com"})
    ]

    mock_query = MagicMock()
    mock_query.stream.return_value = mock_stream
    mock_query.where.return_value = mock_query
    mock_query.select.return_value = mock_query

    mock_items_ref = MagicMock()
    mock_items_ref.where.return_value = mock_query
    mock_db.collection.return_value = mock_items_ref

    response = client.get('/api/products/123?keyword=iphone')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['title'] == "iphone"

@patch('search_api.db')
def test_item_details_no_results(mock_db, client):
    mock_query = MagicMock()
    mock_query.stream.return_value = []
    mock_query.where.return_value = mock_query
    mock_query.select.return_value = mock_query

    mock_items_ref = MagicMock()
    mock_items_ref.where.return_value = mock_query
    mock_db.collection.return_value = mock_items_ref

    response = client.get('/api/products/123?keyword=nonexist')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 0

@patch('search_api.db')
def test_item_details_exception(mock_db, client):
    mock_items_ref = MagicMock()
    mock_items_ref.where.side_effect = Exception("Detail Error")
    mock_db.collection.return_value = mock_items_ref

    response = client.get('/api/products/123?keyword=error')
    assert response.status_code == 200
    data = response.get_json()
    assert "error" in data


@patch('search_api.db')
def test_item_comparison_success(mock_db, client):
    # 假设keywords=iphone, ipad
    mock_stream_iphone = [
        MockDoc("doc1", {"title":"i","store":"amazon","price":900,"star":4,"img_reference":"img.jpg","commentNum":50})
    ]
    mock_stream_ipad = [
        MockDoc("doc2", {"title":"i","store":"target","price":500,"star":4,"img_reference":"img2.jpg","commentNum":20})
    ]

    def side_effect(*args, **kwargs):
        if kwargs and "title" in args:
            keyword_val = args[2]
            mock_query = MagicMock()
            mock_query.select.return_value = mock_query
            if keyword_val == 'i': 
                mock_query.stream.side_effect = [mock_stream_iphone, mock_stream_ipad]
            return mock_query
        return MagicMock()

    mock_items_ref = MagicMock()
    mock_items_ref.where.side_effect = lambda field, op, val: side_effect(field, op, val)
    mock_db.collection.return_value = mock_items_ref

    response = client.post('/api/products/compare?keywords=ii') # 'ii'表示关键词: 'i','i'
    assert response.status_code == 200
    data = response.get_json()

@patch('search_api.db')
def test_item_comparison_no_results(mock_db, client):
    mock_query = MagicMock()
    mock_query.select.return_value = mock_query
    mock_query.stream.return_value = []

    mock_items_ref = MagicMock()
    mock_items_ref.where.return_value = mock_query
    mock_db.collection.return_value = mock_items_ref

    response = client.post('/api/products/compare?keywords=')
    assert response.status_code == 200
    data = response.get_json()
    assert data == []

@patch('search_api.db')
def test_item_comparison_exception(mock_db, client):
    mock_items_ref = MagicMock()
    mock_items_ref.where.side_effect = Exception("Compare Error")
    mock_db.collection.return_value = mock_items_ref

    response = client.post('/api/products/compare?keywords=iphone')
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data




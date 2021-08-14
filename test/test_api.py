"""
Created by Vivek Kumar on 7/27/21
"""
import unittest
import pytest
from base64 import b64encode
from simplefilebrowser.api.app import SimpleFileBrowserAPI, create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_200_response(client):
    credentials = b64encode(b"calvin:hobbes").decode('utf-8')
    data = {
        'root': '/tmp/wv'}
    resp = client.get('/sfb/api', headers={"Authorization": f"Basic {credentials}"}, query_string=data)
    assert resp.status_code == 200


def test_401_response(client):
    resp = client.get('/sfb/api')
    assert resp.status_code == 401


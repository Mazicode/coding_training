from app.api import transform, display, app
from app.config import create_app
import pytest
import asyncio
import time

test_inputs = ['afsdgfsdg', 'H. C. Andersens Blvd. 27,'
                            ' 1553 København V, Denmark', 'random street 5']


@pytest.fixture
def test_transform():
    process = asyncio.run(transform(test_inputs))
    assert process == {'H. C. Andersens Blvd. 27, 1553 København V, Denmark': (55.674136, 12.571782)}


@pytest.fixture
def test_display():
    with app.test_client() as client:
        resp_false = client.get('/results')
        resp_true = client.get('/')
        assert resp_false.status_code == 404, resp_false
        time.sleep(8)
        assert resp_true.status_code == 200, resp_true
        parsed_resp = resp_true.get_json()
        assert parsed_resp != ''

from app.api import transform
from app.config import create_app
import pytest
import asyncio

test_app = create_app()
test_inputs = ['afsdgfsdg', '23472983765', 'random street 5']


@pytest.mark.asyncio
def test_transform():
    process = asyncio.run(transform(test_inputs))
    assert not process


def test_display():
    with test_app.test_client() as client:
        test_inputs = ['afsdgfsdg', '23472983765', 'H. C. Andersens Blvd. 27, 1553 København V, Denmark']

        run_task = asyncio.run(transform(test_inputs))
        # test_transform(run_task)
        result = ("{run_task}".format(**vars()))
        if result:
            resp = client.get('/')
            assert resp.status == 200

            parsed_resp = resp.get_json()
            assert resp.status == 200
            assert parsed_resp == 'Alberti'
            assert test_task and parsed_resp == test_task


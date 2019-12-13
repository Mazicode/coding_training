from app.config import create_app
from app.utils import is_location, is_coordinates
import pytest


# @pytest.fixture
def test_app():
    app = create_app()
    test_is_location()
    test_is_coordinates()
    return app


# @pytest.fixture
def test_is_location():
    test_input = 'some address 16'
    test_output = utils.is_location(test_input)
    assert test_output is None


# @pytest.fixture
def test_is_coordinates():
    test_input = '12143214325'
    test_output = utils.is_coordinates(test_input)
    assert test_output is None

# def test_is_address():

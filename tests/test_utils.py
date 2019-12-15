from app.config import create_app
from app.utils import is_location, is_coordinates
import pytest


@pytest.fixture
def test_app():
    app = create_app()
    return app


@pytest.fixture
def test_is_location():
    test_input_1 = 'some address 16'
    test_input_2 = 'H. C. Andersens Blvd. 27, 1553 København V, Denmark"'
    test_output_1 = is_location(test_input_1)
    test_output_2 = is_location(test_input_2)
    assert test_output_1 is False
    assert test_output_2 is True


@pytest.fixture
def test_is_coordinates():
    test_input_1 = '12143214325'
    test_input_2 = '37.423021, -122.083739'
    test_output_1 = is_coordinates(test_input_1)
    test_output_2 = is_coordinates(test_input_2)
    assert test_output_1 is False
    assert test_output_2 is True

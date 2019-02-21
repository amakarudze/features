""" Pytest conftest.py. Contains fixtures for tests. """

import pytest

from features import create_app


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True
    })

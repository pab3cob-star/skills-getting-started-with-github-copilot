import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def reset_activities():
    original_activities = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_activities)


@pytest.fixture
def client(reset_activities):
    return TestClient(app)

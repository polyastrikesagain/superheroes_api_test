import pytest, requests
from typing import Any

@pytest.fixture
def call_superheroes_api() -> list[dict[str, Any]]:
    """Fixture to call the API"""
    superheroes_json = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
    return superheroes_json
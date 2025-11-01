import pytest
from function import tallest_of_filtered
from typing import Any

@pytest.mark.parametrize("gender, is_employed, expected_gender, expected_name, expected_occupation, expected_height", [
    ('female', False, 'Female', 'Ardina', '-', '193 cm'),
    ('fEMALE', False, 'Female', 'Ardina', '-', '193 cm'),
    ('male', False, 'Male', 'Fin Fang Foom', '-', '975 cm'),
    ('Male', False, 'Male', 'Fin Fang Foom', '-', '975 cm'),
    ('-', False, '-', 'Shadow King', '-', '185 cm'),
    ('female', True, 'Female', 'Wolfsbane', 'Teacher', '366 cm'),
    ('male', True, 'Male', 'Galactus', "Planet Devourer, Third Force of the Universe - balance between Eternity and Death, Nullifying Abraxas' Influence on the Multiverse, Third Face of the Living Tribunal - representing Equity", '876 cm'),
    ('-', True, '-', 'Living Brain', 'Robot', '198 cm'),
])
def test_tallest_of_filtered_returns_correct_hero(call_superheroes_api: list[dict[str, Any]], gender: str,
                                                  is_employed: bool, expected_gender: str, expected_name: str,
                                                  expected_occupation: str, expected_height: str):
    superheroes_json = call_superheroes_api
    hero = tallest_of_filtered(gender, is_employed, superheroes_json)
    assert hero['appearance']['gender'] == expected_gender
    assert hero['name'] == expected_name
    assert hero['work']['occupation'] == expected_occupation
    assert hero['appearance']['height'][1] == expected_height # внутри словаря две записи роста - в футах-дюймах и в см
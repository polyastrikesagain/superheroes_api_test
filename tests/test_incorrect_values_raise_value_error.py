import pytest
from function import tallest_of_filtered
from typing import Any

# тут я постаралась покрыть все проблемы, которые могут вернуть ValueError, и попарно тестируем +/-, -/+, -/-

@pytest.mark.parametrize("gender, is_employed", [
    ("m@l3", 4),
    ("femail", True),
    (True, "-"),
    ('-', 'False'),
    ('male', 'bazinga'),
    ('-', None),
    (None, True),
    (None, None)
])
def test_incorrect_values_raise_value_error(call_superheroes_api: list[dict[str, Any]], gender: str, is_employed: bool):
    superheroes_json = call_superheroes_api
    with pytest.raises(ValueError):         # если возвращается ошибка ValueError, то все отлично, негативный тест!
        tallest_of_filtered(gender, is_employed, superheroes_json)
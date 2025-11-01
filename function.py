from typing import Any


def tallest_of_filtered(gender: str, is_employed: bool, superheroes_json: list[dict[str, Any]]) -> dict[str, Any] | None:
    """
    Function to find the tallest superhero while filtering them by gender and employment
    :param gender: Gender of the superhero
    :param is_employed: Boolean value detecting whether the superhero works or not
    :param superheroes_json: JSON data from the API parsed into a list of dicts
    :return: list[dict[str, Any]]
    """
    if not(isinstance(gender, str)) or gender.lower() not in ('female', 'male', '-'):
        raise ValueError("Only acceptable values for gender are 'Female', 'Male' and '-'")
    if not isinstance(is_employed, bool):
        raise ValueError("Only acceptable values for is_employed are boolean (True or False)")
    try:
        # setting up vars for finding the tallest superhero fitting the criteria
        max_height = 0
        hero_of_max_height = dict()
        gender = gender.title()

        # looking through the superheroes_json to see if gender and employment status match the parameters
        for hero in superheroes_json:
            if hero['appearance']['gender'] == gender and ((hero['work']['occupation'] != '-' and is_employed)
                    or (hero['work']['occupation'] == '-' and (not is_employed))):
                if hero_height:=float(hero['appearance']['height'][1].split()[0]) > max_height:
                    max_height = hero_height
                    hero_of_max_height = hero

        return hero_of_max_height # found him!

    except KeyError as key_error:
        raise ValueError('An error occurred with the provided data structure for superheroes_json parameter:', str(key_error)) from key_error



"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional

from models.basemodel import Base


class Characters_(Base):
    """Pydantic models class meant to validate the data for `Characters` object from
        single resource endpoint (https://swapi.dev/api/people/) from starwars API.
    """

    # attribute fields
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: Optional[List[str]]
    species: Optional[List[str]]
    starships: Optional[List[str]]
    vehicles: Optional[List[str]]



if __name__ == "__main__":

    char_data = {
            "name": "Luke Skywalker",
            "height": "172",
            "mass": "77",
            "hair_color": "blond",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "19BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/14/",
                "https://swapi.dev/api/vehicles/30/"
            ],
            "starships": [
                "https://swapi.dev/api/starships/12/",
                "https://swapi.dev/api/starships/22/"
            ],
            "created": "2014-12-09T13:50:51.644000Z",
            "edited": "2014-12-20T21:17:56.891000Z",
            "url": "https://swapi.dev/api/people/1/"
        }

    obj = Characters_(**char_data)    # validation & de-serialization
    print(obj)
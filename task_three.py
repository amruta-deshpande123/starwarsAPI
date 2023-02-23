import argparse
from pprint import pprint

from utils.randgen import ProduceChars
from utils.fetch_data import hit_url
from utils.timing import timeit

# resource classes.
from resources.characters import Characters
from resources.films import Films
from resources.planets import Planets
from resources.species import Species
from resources.starships import Starships
from resources.vehicles import Vehicle


# pydantic models
from models.datamodels.characters import Characters_
from models.datamodels.films import Film_
from models.datamodels.planets import Planets_
from models.datamodels.vehicles import Vehicles_
from models.datamodels.species import Species_
from models.datamodels.starships import Starships_


def characters_data():
    """
        Getting count of Characters; Validating Characters data; Generates list of all Characters
        URLs
    """


    character_obj = Characters()
    total_characters = character_obj.get_count()
    print(f"\nGetting Characters Count :: ", end="")
    pprint(total_characters)

    character_data = character_obj.get_sample_data()
    character_data = Characters_(**character_data)
    print(f"\nValidating Character Data :: \n")
    pprint(character_data)

    global character_urls
    character_urls = character_obj.get_resource_urls()
    print(f"\nGetting list of all Character URLs::")
    pprint(character_urls)


def films_data():
    """
        Getting count of Films; Validating Films data; Generates list of all Films
        URLs
    """
    film_obj = Films()
    total_films = film_obj.get_count()
    print(f"\nGetting Films Count :: ", end="")
    pprint(total_films)

    film_data = film_obj.get_sample_data()
    film_data = Film_(**film_data)
    print(f"\nValidating Film Data :: \n")
    pprint(film_data)

    global film_urls
    film_urls = film_obj.get_resource_urls()
    print(f"\nGetting list of all Film URLs::")
    pprint(film_urls)


def planets_data():
    """
        Getting count of Planets; Validating Planets data; Generates list of all Planets
        URLs
    """
    planet_obj = Planets()
    total_planets = planet_obj.get_count()
    print(f"\nGetting Planets Count :: ", end="")
    pprint(total_planets)

    planet_data = planet_obj.get_sample_data()
    planet_data = Planets_(**planet_data)
    print(f"\nValidating Planet Data :: \n")
    pprint(planet_data)

    global planet_urls
    planet_urls = planet_obj.get_resource_urls()
    print(f"\nGetting list of all Planet URLs::")
    pprint(planet_urls)


def species_data():
    """
        Getting count of Species; Validating Species data; Generates list of all Species
        URLs
    """
    specie_obj = Species()
    total_species = specie_obj.get_count()
    print(f"\nGetting Species Count :: ", end="")
    pprint(total_species)

    specie_data = specie_obj.get_sample_data()
    specie_data = Species_(**specie_data)
    print(f"\nValidating Species Data :: \n")
    pprint(specie_data)

    global specie_urls
    specie_urls = specie_obj.get_resource_urls()
    print(f"\nGetting list of all Species URLs::")
    pprint(specie_urls)


def starships_data():
    """
        Getting count of Starships; Validating Starships data; Generates list of all Starships
        URLs
    """
    starship_obj = Starships()
    total_starships = starship_obj.get_count()
    print(f"\nGetting Starships Count :: ", end="")
    pprint(total_starships)

    starship_data = starship_obj.get_sample_data(2)
    starship_data = Starships_(**starship_data)
    print(f"\nValidating Starship Data :: \n")
    pprint(starship_data)

    global starship_urls
    starship_urls = starship_obj.get_resource_urls()
    print(f"\nGetting list of all Starship URLs::")
    pprint(starship_urls)


def vehicles_data():
    """
        Getting count of Vehicles; Validating Vehicles data; Generates list of all Vehicles
        URLs
    """
    vehicle_obj = Vehicle()
    total_vehicles = vehicle_obj.get_count()
    print(f"\nGetting Vehicles Count :: ", end="")
    pprint(total_vehicles)

    vehicle_data = vehicle_obj.get_sample_data(4)
    vehicle_data = Vehicles_(**vehicle_data)
    print(f"\nValidating Vehicle Data :: \n")
    pprint(vehicle_data)

    global vehicle_urls
    vehicle_urls = vehicle_obj.get_resource_urls()
    print(f"\nGetting list of all Vehicle URLs::")
    pprint(vehicle_urls)

@timeit
def main_task():
    characters_data()
    films_data()
    planets_data()
    species_data()
    starships_data()
    vehicles_data()

@timeit
def random_data():
    """
    Generates Three random numbers and fetch data for each resource's given by user, default:people
    Returns: List
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit",
                        default=3, type=int)
    parser.add_argument("-s", "--start",
                        default=1, type=int)
    parser.add_argument("-e", "--end",
                        default=8, type=int)
    parser.add_argument("-r", "--resource",
                        default="people",
                        choices=["films",
                                 "planets",
                                 "people",
                                 "starships",
                                 "species",
                                 "vehicles"])
    argument = parser.parse_args()
    print(f"\nPassed arguments are -> {argument}")

    obj = ProduceChars(argument.start, argument.end, argument.limit)

    resources = [element for element in obj]

    for item in resources:
        if argument.resource == 'films':
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            #get_url(character_urls[item])
            data = hit_url(film_urls[item])
            data = data.json()
            pprint(data)

        if argument.resource == 'planets':
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            #get_url(character_urls[item])
            data = hit_url(planet_urls[item])
            data_ = data.json()
            pprint(data_)

        if argument.resource == 'species':
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            #get_url(character_urls[item])
            data = hit_url(specie_urls[item])
            data_ = data.json()
            pprint(data_)

        if argument.resource == 'starships':
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            #get_url(character_urls[item])
            data = hit_url(starship_urls[item])
            data_ = data.json()
            pprint(data_)

        if argument.resource == 'vehicles':
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            #get_url(character_urls[item])
            data = hit_url(vehicle_urls[item])
            data_ = data.json()
            pprint(data_)

        else:
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            #get_url(character_urls[item])
            data = hit_url(character_urls[item])
            data_ = data.json()
            pprint(data_)


if __name__ == "__main__":
    main_task()
    random_data()

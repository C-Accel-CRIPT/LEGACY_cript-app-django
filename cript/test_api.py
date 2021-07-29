"""
This file is used for testing the CRIPT Django public API.

"""

import requests


def get_material_list():
    """Return a list of all materials in the CRIPT database"""
    r = requests.get("http://127.0.0.1:8000/api/materials/?format=json")
    return r.json()


def add_new_material(material_object):
    """Add a new material to the CRIPT database"""
    url = "http://127.0.0.1:8000/api/materials/"
    return requests.post(url, data=material_object)


new_material = {
    "name": "polystyrene",
    "material_type": "polymer",
    "keywords": ["styrene", "comb", "elastomer"],
    "notes": "new_notes",
}


if __name__ == "__main__":

    print(get_material_list())

    print(add_new_material(new_material))

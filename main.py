import json


def load_data (file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


animals_info = []
for info in animals_data:
    name = info.get("name")
    diet = info.get("characteristics", {}).get("diet")
    location = info.get("locations")[0]
    fox_type = info.get("characteristics", {}).get("type")

    animals_info.append({
        "name": name,
        "diet": diet,
        "location": location,
        "type": fox_type
    })

for animal in animals_info:
    print(f"Name: {animal['name']}")
    print(f"Diet: {animal['diet']}")
    print(f"Location: {animal['location']}")

    if animal['type'] is not None:
        print(f"Type: {animal['type']}")

    print()






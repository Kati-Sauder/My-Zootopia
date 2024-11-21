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

output = ""
for animal in animals_info:
    output += f"Name: {animal['name']}\n"
    output += f"Diet: {animal['diet']}\n"
    output += f"Location: {animal['location']}\n"

    if animal['type'] is not None:
        output += f"Type: {animal['type']}\n"

    output += "\n"

print(output)


with open ("animals_template.html", "r") as file:
    html_content = file.read()
print(html_content)


new_text = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
print(new_text)


with open("updated_animals_template.html", "w") as file:
    file.write(new_text)




import json


def load_data (file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
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
    output += '<li class="cards__item">'
    output += f"Name: {animal['name']}<br/>\n"
    output += f"Diet: {animal['diet']}<br/>\n"
    output += f"Location: {animal['location']}<br/>\n"

    if animal['type'] is not None:
        output += f"Type: {animal['type']}<br/>\n"

    output += "</li>"
print(output)


with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()
print(html_content)


new_text = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
print(new_text)


with open("updated_animals_template.html", "w", encoding="utf-8") as file:
    file.write(new_text)




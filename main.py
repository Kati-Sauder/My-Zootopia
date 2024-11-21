import json


def load_data(file_path):
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
    name = animal['name']
    if name == "Darwin’s fox":
        name = name.replace("Darwin’s fox", "Darwins fox")
    output += '<li class="cards__item">'
    output += '<div class="card__title">'f"Name: {animal['name']}"'</div>'
    output += '<p class ="card__text" >'
    output += '<strong>'"Diet: "'</strong>'f"{animal['diet']}"'<br/>'
    output += '<strong>'"Location: "'</strong>'f"{animal['location']}"'<br/>'

    if animal['type'] is not None:
        output += '<strong>'"Type: "'</strong>'f" {animal['type']}"'<br/>'

    output += "</li>"
print(output)


with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()
print(html_content)


new_text = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
print(new_text)


with open("updated_animals_template.html", "w", encoding="utf-8") as file:
    file.write(new_text)




import json


def load_data(file_path):
    """ Loads a JSON file with data of foxes"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def animal_info(animals_data):
    """
    Extracts and processes data from a JSON file with data of foxes.
    """
    animals_info = []
    for info in animals_data:
        name = info.get("name")
        diet = info.get("characteristics", {}).get("diet")
        location = info.get("locations")[0]
        fox_type = info.get("characteristics", {}).get("type")
        science_name = info.get("taxonomy", {}).get("scientific_name")
        color = info.get("characteristics", {}).get("color")
        skin_type = info.get("characteristics", {}).get("skin_type")

        animals_info.append({
            "name": name,
            "diet": diet,
            "location": location,
            "type": fox_type,
            "scientific_name": science_name,
            "color": color,
            "skin_type": skin_type
        })
    return animals_info


def serialize_animals_info(animal):
    output = ""
    output += '<li class="cards__item">'
    output += '<div class="card__title">'f"Name: {animal['name']}"'</div>'
    output += '<p class ="card__text" >'
    output += '<ul >'
    output += f'<li><strong>'"Diet: "'</strong>'f"{animal['diet']}"'</li>'
    output += f'<li><strong>'"Location: "'</strong>'f"{animal['location']}"'</li>'
    output += f'<li><strong>'"Scientific Name: "'</strong>'f"{animal['scientific_name']}"'</li>'
    output += f'<li><strong>'"Color: "'</strong>'f"{animal['color']}"'</li>'
    if animal.get('skin_type'):
        output += f'<li><strong>'"Skintype: "'</strong>'f"{animal['skin_type']}"'</li>'
    if animal.get('type'):
        output += f'<li><strong>'"Type: "'</strong>'f" {animal['type']}"'</li>'
    output += "</ul>"
    output += "</p>"
    output += "</li>"
    return output


def generate_animals_html(data, template_path, output_path):
    animals_html = ''.join(serialize_animals_info(animal) for animal in data)
    try:
        with open(template_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        new_text = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(new_text)
    except FileNotFoundError:
        print("Error: Template file {template_path} not found.")


def main():
    animals_data = load_data('animals_data.json')
    if not animals_data:
        return

    processed_data = animal_info(animals_data)

    generate_animals_html(
        processed_data,
        template_path="animals_template.html",
        output_path="updated_animals_template.html"
    )


if __name__ == "__main__":
    main()

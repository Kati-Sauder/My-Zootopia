def serialize_animals_info(animal):
    output = ""
    output += '<li class="cards__item">'
    output += '<div class="card__title">'f"Name: {animal['name']}"'</div>'
    output += '<p class ="card__text" >'
    output += '<strong>'"Diet: "'</strong>'f"{animal['diet']}"'<br/>'
    output += '<strong>'"Location: "'</strong>'f"{animal['location']}"'<br/>'
    output += '<strong>'"Scientific Name: "'</strong>'f"{animal['scientific_name']}"'<br/>'
    output += '<strong>'"Color: "'</strong>'f"{animal['color']}"'<br/>'
    if animal['type'] is not None:
        output += '<strong>'"Type: "'</strong>'f" {animal['type']}"'<br/>'
    output += "</li>"
    return output
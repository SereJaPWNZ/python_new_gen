def get_formatted_city(city, country, population=None):
    """Строит отформатированное название города и страны"""
    if population is None:
        formatted_city = f"{city}, {country}"
    else:
        formatted_city = f"{city}, {country}, {population}"
    return formatted_city.title()

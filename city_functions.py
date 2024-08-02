def get_info(city,country,population=0):
    """描述城市"""
    if population:
        city_info = f"{city},{country} - population {population}"
    else:
        city_info = f"{city},{country}"
    return city_info.title()
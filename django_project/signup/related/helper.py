def format_cities(cities):
    """Returns: a list of strings, each in the format of "City, State".
    Requires: a QuerySet of City instances"""
    f = lambda city : str(city.city) + ", " + str(city.state)
    return list(map(f, cities))

def deformat_city(string):
    """Returns: a dictionary containing the 'city' and 'state'
    Requires: a string in the format of "City, State"""
    comma_index = string.find(", ")
    return {'city': string[0:comma_index], 'state': string[2+comma_index:]}

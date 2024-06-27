import sys

def get_key_from_value(capital_cities, value):
    for key, capital in capital_cities.items():
        if capital == value:
            return key
    return None

def state():
    if len(sys.argv) != 2:
        sys.exit(0)
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    if sys.argv[1] in capital_cities.values():
        print(get_key_from_value(states,get_key_from_value(capital_cities,sys.argv[1])))
    else:
        print("Unknown capital")
if __name__ == '__main__':
    state()
import sys

def get_key_from_value(capital_cities, value):
    for key, capital in capital_cities.items():
        if capital == value:
            return key
    return None

def is_state(states, capital_cities, content):
    for state in states:
        if state.lower() == content.lower():
            print(f"{capital_cities[states[state]]} is the capital of {state}")
            return True
    return False

def is_capital(states, capital_cities, content):
    for capital in capital_cities.values():
        if capital.lower() == content.lower():
            print(f"{capital} is the capital of {get_key_from_value(states,get_key_from_value(capital_cities,capital))}")
            return True
    return False

def all_in():
    if len(sys.argv) != 2:
        sys.exit(1)
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
    contents = sys.argv[1].split(',')
    for content in contents:
        content = content.strip()
        if len(content) == 0:
            pass
        elif is_capital(states, capital_cities, content):
            pass
        elif is_state(states, capital_cities, content):
            pass
        else:
            print(f"{content} is neither a capital city nor a state")

if __name__ == '__main__':
    all_in()
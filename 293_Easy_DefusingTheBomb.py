WIRE_RULES = {
    "white":  ["red", "orange", "green", "purple"],
    "red":    ["green"],
    "black":  ["red", "black", "purple"],
    "orange": ["red", "black"],
    "green":  ["orange", "white"],
    "purple": ["red", "black"]
    }
def is_valid_sequence(wire_sequence):
    is_valid = True
    wire_sequence = wire_sequence.split('\n')
    prev_wire = wire_sequence[0]
    for wire in wire_sequence[1:]:
        if wire not in WIRE_RULES[prev_wire]:
            is_valid = False
            break
        prev_wire = wire
    return is_valid
INPUT1 = """white\nred\ngreen\nwhite"""
INPUT2 = """white\norange\ngreen\nwhite"""
GET_FLAVOR_TEXT = lambda input_text: "Bomb defused" if is_valid_sequence(input_text) else "Boom"
print(GET_FLAVOR_TEXT(INPUT1))
print(GET_FLAVOR_TEXT(INPUT2))

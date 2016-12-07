# Reddit DailyProgrammer #294_Easy, Rack Management

# Description
# Today's challenge is inspired by the board game Scrabble.
# Given a set of 7 letter tiles and a word, determine whether you can make
# the given word using the given tiles.Feel free to format your input
# and output however you like. You don't need to read from your
# program's input if you don't want to - you can just write a function
# that does the logic. I'm representing a set of tiles as a single string,
# but you can represent it using whatever data structure you want.

# Examples

# scrabble("ladilmy", "daily") -> true
# scrabble("eerriin", "eerie") -> false
# scrabble("orrpgma", "program") -> true
# scrabble("orppgma", "program") -> false

def scrabble(pieces, to_find):
    found_word = True
    if len(pieces) >= len(to_find):
        pool = list(pieces)
        for char in to_find:
            if char in pool:
                pool.remove(char)
            else:
                found_word = False
    else:
        found_word = False
    return found_word

print(scrabble("ladilmy", "daily"))
print(scrabble("eerriin", "eerie"))
print(scrabble("orrpgma", "program"))
print(scrabble("orppgma", "program"))

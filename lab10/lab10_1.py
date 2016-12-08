from actions import *
from save import *

result = {}
sequence = input('Input a sequence:')
user_azos = list(filter(letter_is_azot_osn, list(sequence)))
print('start sequence:   ', user_azos)

action = input('Input a action:')

while action != 'stop':
    if action == 'show all':
        print(result)
    elif action[:5] == "show ":
        key = action[5:]
        print(key, ':', result[key])
    elif action == 'save':
        save(result)
    elif action == 'load':
        result = load()
    elif action == 'add':
        result[action] = add_random(user_azos)
    elif action == 'delete':
        result[action] = delete_first(user_azos)
    elif action == 'mutation':
        result[action] = mutation(user_azos)
    elif action == 'rnd_mutation':
        result[action] = rnd_mutation(user_azos)
    else:
        result[action] = 'no data'
    # get next
    action = input('Input a action:')

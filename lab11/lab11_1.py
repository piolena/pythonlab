from Sequence import *
from save import *

seq = Sequence()
print('start sequense is: ', seq.as_str())

result = {}

action = input('Input a action:')

while action != 'stop':
    if action == 'show all':
        print(result)
    elif action[:5] == "show ":
        try:
            key = action[5:]
            print(key, ':', result[key])
            break
        except KeyError:
            print('No such key in result dictionary!, try another please')
    elif action == 'save.py':
        save(result)
    elif action == 'load':
        result = load()
    elif action == 'add':
        seq.add_random()
        result[action] = seq.as_str()
    elif action == 'delete':
        seq.delete_first()
        result[action] = seq.as_str()
    elif action == 'mutation':
        seq.mutation()
        result[action] = seq.as_str()
    elif action == 'rnd_mutation':
        seq.rnd_mutation()
        result[action] = seq.as_str()
    else:
        result[action] = 'no data'
    # get next
    action = input('Input a action:')

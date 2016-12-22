from MyExceptions import *
from Sequence import *
from save import *

seq = Sequence()
print('start sequense is: ', seq.as_str())

result = {}
action = input('Input a action:')

while action != 'stop':
    try:
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
            raise NotImplementedError
    except KeyError:
        print('Can`t show it, no such key in result dictionary!, try another please')
    except FileNotFoundError as fileError:
        print(fileError)
    except IOError as error:
        print(error)
    except NotImplementedError:
        print('Unknown action, try another please')
    except MutationException as ex:
        print(ex)
        # get next
    action = input('Input a action:')

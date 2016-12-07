from actions import *

result = {}
sequence = input('Input a sequence:')
user_azos = list(filter(letter_is_azot_osn, list(sequence)))
print('start sequence:   ', user_azos)

action = input('Input a action:')
while action != 'stop':
    if action == 'show all':
        print(result)
    else:
        if action.find("show ") >= 0 :
            act = action[action.find(" ")+1:]
            print(act, ':', result[act])
        else:
            if action == 'add':
                result[action] = add_random(user_azos)
            else:
                if action == 'delete':
                    result[action] = delete_first(user_azos)
                else:
                    if action == 'mutation':
                        result[action] = mutation(user_azos)
                    else:
                        if action == 'rnd_mutation':
                            result[action] = rnd_mutation(user_azos)
                        else:
                            result[action] = 'no data'
    # get next
    action = input('Input a action:')

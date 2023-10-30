import json

ask = True
with open('dictionary\data', 'r') as file:
    temp = json.load(file)


while ask:
    foo = {}
    try:
        get_input = input(f' > ')
        get_input_2 = input(f'{get_input} = ')
    except KeyboardInterrupt:
        print('fakk')
        ask = False
    if ask == True:
        temp.update({get_input:get_input_2})   
        temp.update({get_input_2:get_input})   
    
with open('dictionary\data', 'w') as file:
    json.dump(temp, file, indent=4)
    print('File writted...')
import json

with open('sample_data.json', 'r') as my_json:
    a = json.load(my_json)

names = ['DN', 'Description', 'Speed', 'MTU']
form = '{:<47} {:<15} {:<10} {:<6}'

print(format('=' * 75))
print(form.format(*names))
print(format('-' * 47 + ' ' + '-' * 15 + '  ' + '-' * 10 + '  ' + '-' * 6))

for i in a['imdata']:
    print(form.format(i['l1PhysIf']['attributes']['dn'], i['l1PhysIf']['attributes']['descr'], i['l1PhysIf']['attributes']['speed'], i['l1PhysIf']['attributes']['mtu']))



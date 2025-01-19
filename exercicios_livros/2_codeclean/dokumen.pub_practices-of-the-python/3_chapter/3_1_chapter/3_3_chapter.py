NAMES = ['Abby', 'Dave', 'Keira']

def print_greetings():
    greeting_pattern = 'Say hi to {name}!'
    nice_person_pattern = '{name} is a nice person!'
    for name in NAMES:
        print(greeting_pattern.format(name=name))
        print(nice_person_pattern.format(name=name))

print_greetings()
import randfacts

'''
randwand = randfacts.__doc__
print(randwand)
'''

randwanda = randfacts.get_fact(only_unsafe=True)
print(randwanda)


randwand = randfacts.unsafe_facts()
print(randwand)
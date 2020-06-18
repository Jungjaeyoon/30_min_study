from random import randint 


random_bits = 0

for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i

flavor_list = [ 'vanilla', 'choloate', 'pecan', 'strawberry']

for flavor in flavor_list:
    print('%s is delicious' % flavor)


for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))
# iterator 
print('iterator')
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))

print('iterator with position number')
print('position number doesn\'t means starting position')

# iterator with start position number
# position number doesn't means starting position
for i, flavor in enumerate(flavor_list,2):
    print('%d: %s' % (i + 1, flavor))


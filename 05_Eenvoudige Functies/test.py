#uitvoer = '{} + {} = {}'

#print(uitvoer.format(3, 4, 5))
#print(uitvoer.format(-1, 3, 9))

#uitvoer = '{0} + {1} = {1}'
#print(uitvoer.format(1, 6))

#uitvoer = '{0:d} + {0:.2f} = {1:d}'

#print(uitvoer.format(1, 2))

#uitvoer = '{0} + {1:9.2f} = {2:d}'

#print(uitvoer.format('een', pow(2, 0.5), 2))
#^><

#from math import sqrt, floor, pi

#print(pi)

from random import uniform, random, randint, seed
seed(1233)
#random is nooit random
print(random())
print(uniform(1, 5))
print(randint(3, 100))

import randomm
random.seed(1233)
#random is nooit random
print(random.random())
print(random.uniform(1, 5))
print(random.randint(3, 100))

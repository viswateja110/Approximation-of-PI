import random
from decimal import Decimal
import math
#assuming radius of the circle
radius=200

#total number of darts thrown
totaldots=0

#number of darts thrown inside the circle
circledots=0
while True:
    #throwing 10000 darts at a time
    for i in range(10000):
        x=random.randint(-radius,radius)**2
        y=random.randint(-radius,radius)**2
        totaldots+=1
        dist=Decimal(math.sqrt(x+y))
        if dist<Decimal(radius):
            circledots+=1
    print (4*(Decimal(circledots)/Decimal(totaldots)))

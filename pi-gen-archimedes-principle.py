import math
from decimal import *
getcontext().prec=70
pi=0
polysides=6
sidelen=1
r_a=0
r_b=0
polycircum=0
i=50
num="1"
while i>=0:
    num=str(int(num)*10)
    i-=1

while polysides<int(num):
    sidelen2=Decimal(sidelen)/Decimal(2)
    r_a=(Decimal(1**2)-Decimal(sidelen2**2)).sqrt()
    r_b=Decimal(1)-Decimal(r_a)
    sidelenNew=(Decimal(r_b**2)+Decimal(sidelen2**2)).sqrt()
    polycircum=Decimal(polysides*sidelen)
    pi=Decimal(polycircum)/Decimal(2)
    print("pi:",pi)
    sidelen=sidelenNew
    polysides*=2

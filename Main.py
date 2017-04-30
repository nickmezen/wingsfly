__author__ = 'Galaxcity'
from math import exp
from math import sqrt

y=5126
x=3020
y1=5178
x1=2945
y2=5094
x2=3087
a = 2
aa = 1
q = 6
P = 10000
l = 134
bb = 1
S = 100


d = sqrt((y1 - y2) * (y1 - y2)+(x1 - x2) * (x1 - x2))
dr = sqrt((((y1 - y2) * x + (x2 - x1) * y + x1 * y2 - x2 * y1)/d)*(((y1 - y2) * x + (x2 - x1) * y + x1 * y2 - x2 * y1)/d))
d1 = sqrt((y1 - y) * (y1 - y) + (x1 - x) * (x1 - x))
d2 = sqrt((y - y2) * (y - y2) + (x - x2) * (x - x2))
dd = sqrt(sqrt((d1 * d1 - dr * dr)*(d1 * d1 - dr * dr))) + sqrt(sqrt((d2 * d2 - dr * dr)*(d2 * d2 - dr * dr)))
if dd >(d + 0.00000001):
    d = min(d1,d2)
else: d = dr

f = P/l/a*bb/sqrt(6.28)*exp(-(d)*(d-a)/2/q/q)
ff = 0
ff += aa*S*f
print(ff)
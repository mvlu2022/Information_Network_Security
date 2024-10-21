import random
p=18
g=3
print("the value of p is: %d"%(p))
print("the of value of g is: %d"%(g))
a=4
print("Secrete Number for alice is : %d"%(a))
x=int(pow(g,a,p))
b=7
print("Secrete Number for BOB is : %d"%(b))

y=int(pow(g,b,p))
ka=int(pow(b,g,p))
kb=int(pow(x,b,p))
print("secret key for the alice is: %d"%(ka))
print("Secrete key for the bob is :%d"%(kb))
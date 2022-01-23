# Write a Python Program to compute the area of circle, square, rectangle and triangle by using functions 
def cir(r):
  return(3.14*r*r)
def rec(l,b):
  return(l*b)
def tri(b,h):
  return(b*h)
def sqr(a):
  return(a*a)

rad=int(input())
print(cir(rad))
lend=int(input())
bre=int(input())

print(rec(lend,bre))
base=int(input())
hei=int(input())
print(tri(base,hei))
sid=int(input())
print(sqr(sid))
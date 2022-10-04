import numpy as np
import matplotlib.pyplot as mp
import sympy as sp
from sympy import simplify,Eq,cos,sin,diff

def comparate(x):
  if not x.is_real:
    if sp.re(x)<=0:
      x=None
    else:
      if abs(sp.im(x)/sp.re(x))<1e-10:
        x=sp.sqrt(sp.re(x)**2+sp.im(x)**2)
      else:
        x=None
  else:
    if x<=0:
      x=None
  return x

def subs(f,*args):
  for i in args:
    f=f.subs(i[0],i[1])
  return f

def solve(f):
  solutions=sp.solve(f)
  realSolutions=[comparate(i) for i in solutions]
  return realSolutions

def count(array):
  count=0
  for i in array:
    if i!=None:
        count+=1
  return count

def findSolutions(f,maxNumOfSols,domAndArray,imgAndArray):
  solutions=[[[],[]] for i in range(maxNumOfSols+1)]
  for i in domAndArray[1]:
    for j in imgAndArray[1]:
        index=int(count(solve(subs(f,(domAndArray[0],i),(imgAndArray[0],j)))))
        solutions[index][0].append(i)
        solutions[index][1].append(j)
  return solutions

def graf(f,alphaVal,betaVal,radios,mVal=1,cVal=1,m_gVal=1):
  return radios,[subs(f,(m,mVal),(c,cVal),(m_g,m_gVal),(alpha,alphaVal),(beta,betaVal),(r,rad)) for rad in radios]
  

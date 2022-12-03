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

def graf(f,alphaVal,betaVal,radios,coords,params,mVal=1,cVal=1,m_gVal=1):
    return radios,[subs(f,(params[1],mVal),(params[2],cVal),(params[0],m_gVal),(params[3],alphaVal),(params[4],betaVal),(coords[1],rad)) for rad in radios]
  
def plot(sols, alphaVal, MVal):
    mp.figure(figsize=(4.8, 4.8))
    color = "kbgmr"
    labels = ["0 soluciones","1 solución","2 soluciones","3 soluciones","4 soluciones"]
    for i in range(len(sols)):
        mp.scatter(sols[i][0],sols[i][1],s=2,c=color[i], label=labels[i])

    mp.xlabel(r"$\alpha$")
    mp.ylabel(r"$\beta$")

    mp.title(f"Espacio ($\\alpha,\\beta$) de soluciónes del agujero\nnegro rotante ($m_g=1$, $\\epsilon=1$, $a={alphaVal}$ y $M={MVal}$).")

    mp.legend(bbox_to_anchor=(1,1))
    mp.show()
    
def Ergosphere(Ergo,FHorizonte0,thetas,alphaVal,betaVal,aVal,coords,params,Kerr = False):
    ergosphere = []
    m_gVal = 1
    if Kerr:
        m_gVal = 0
    for angle in thetas:
        ergoSols=[i if i!=None else 0 for i in solve(subs(Ergo,(params[0],m_gVal),(params[2],1),(params[3],alphaVal),(params[4],betaVal),(coords[2],angle),(params[1],1),(params[5],aVal)))]
        ergoSols.sort()
        ergosphere.append(ergoSols[-1])
    rHorizon = [i if i!=None else 0 for i in solve(subs(FHorizonte0,(params[0],m_gVal),(params[2],1),(params[3],alphaVal),(params[4],betaVal),(params[1],1),(params[5],aVal)))]
    rHorizon.sort()
    return np.array(ergosphere)*np.cos(thetas), np.array(ergosphere)*np.sin(thetas), rHorizon[-1]

def temp(params, rads, alps, bets, aes):
    Temp = []
    for rs in rads:
        Temp.append(((1/(4*np.pi))*(params[3]*(3*rs**4-4*rs**3+rs*2)+params[4]*(3*rs**4-6*rs**3+3*rs*2)+(3*rs**4-2*rs**3+rs**2-params[5]**2))/((rs**2+params[5]**2)*rs)).subs(params[3], alps).subs(params[4], bets).subs(params[5], aes))
    return np.array(Temp)
   
print("Module FuncionesUtiles was charged")
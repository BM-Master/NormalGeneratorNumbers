import math
import numpy as np

def uniformGenerator(m:int, a:int, c:int, numbers:int):
  xStart = 5
  nums = []
  nums.append(xStart)
  for i in range(0, numbers):
    xNew = (a*xStart + c) % m
    nums.append(xNew)
    xStart = xNew

  ret = [x/m for x in nums]
  return ret

def standarizeValues(data, mean:int, desvStd:int):
  return [(x-mean)/desvStd for x in data]

def desStandarizeValues(data, mean:int, desvStd:int):
  return [ (x*desvStd + mean) for x in data]

def A(x, aList):
  ret = 0
  for i in range(0, 4):
    ret += (aList[i] * x**i)

  return ret

def B(x, bList):
  ret = 0
  for i in range(0, 4):
    ret += (bList[i] * x**i)

  return ret

def g(v, aList, bList):
  parm = math.sqrt(-2*np.log(v))
  aVal = A(parm, aList)
  bVal = B(parm, bList)
  
  return parm * (aVal/bVal)
  
def odehEvansAlgorithm(numbers: int):
  uniforms = uniformGenerator(8, 5, 5, numbers)
  normals = []
  a0 =  -0.322232431088
  a1 = -1
  a2 = -0.342242088547
  a3 = -0.0204231210245
  a4 = -0.0000453642210148

  b0 = 0.09934846260
  b1 = 0.588581570495
  b2 = 0.531103462366
  b3 = 0.103537752850
  b4 = 0.0038560700634

  aList = [a0, a1, a2, a3, a4]
  bList = [b0, b1, b2, b3, b4]

  for u in uniforms:
    if u != 0:
      if u < 0.5:
        normals.append(g(1-u, aList, bList))
      else:
        normals.append(-g(u, aList, bList))

  return normals

mean = 0 # change this value for non standar normal dist
desvStd = 1 # change this value for non standar normal dist

n = odehEvansAlgorithm(20)
nNew = desStandarizeValues(n, mean, desvStd)

print(f'normal values \n: {n}')
print(f'new normal values \n: {nNew}')

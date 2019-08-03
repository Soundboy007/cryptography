#Disclaimer: ECMult(P,a) takes around 10-15 seconds to process. 
#Reading the input file. 
example = open('ECCaddinput.txt', 'r')
text = example.read().split('\n')
#if the last input value has a ',' it means it is a point. Initializing values accordingly.
if ',' in text[-1]:
  A, B, p, P, Q = text[:]
  A, p = int(A), int(p)
else:
  A, B, p, P, a = text[:]
  A, B, p, a = int(A), int(B), int(p), int(a)

#Fast power algorithm source: https://www.rookieslab.com/posts/fast-power-algorithm-exponentiation-by-squaring-cpp-python-implementation
def fast_power(base, power, MOD):
  result = 1
  while power > 0:
      # If power is odd
      if power % 2 == 1:
          result = (result * base) % MOD

      # Divide the power by 2
      power = power // 2
      # Multiply base to itself
      base = (base * base) % MOD
  return result

#creating a P + P function
def ECDouble(P):
  Px, Py = P.split(',')
  Px, Py = int(Px), int(Py)

  #lam = m1/m2
  m1 = (3*(fast_power(Px,2,p)) + (A)%p)%p
  m2 = 2*Py
  #finding inverse of m2 and then multiplying it with m1
  lam = (m1 * fast_power(m2, p-2, p))%p

  # Py = lam*Px + b
  b = Py - lam*Px

  Xr = ((lam**2) - 2*(Px))%p
  Yr = -(lam*Xr + b)%p

  return str(str(Xr) + ', ' + str(Yr))

#creating a P + Q function
def ECAdd(P,Q):
  Px, Py = P.split(',')
  Qx, Qy = Q.split(',')
  Px, Py, Qx, Qy = int(Px), int(Py), int(Qx), int(Qy)
  #handling inverse points
  if Px==Qx and Py == -1*Qy:
    return("The points are additive identities of each other. Sum: 0,0")

  elif Px>0 and Py>0 and Qx>0 and Qy>0:
    #lam = m1/m2
    m1 = (Qy - Py)%p
    m2 = Qx - Px
    #finding inverse of m2 and multiplying with m1
    lam = (m1 * fast_power(m2, p-2, p))%p

    # Py = lam*Px + b
    b = Py - lam * Px

    Xr = ((lam**2) - Px - Qx)%p
    Yr = p - (lam*Xr + b)%p

    return str(str(Xr) + ', ' + str(Yr))

  #if one of the points is 0,0 , then returning the other
  elif Px>0 or Py>0:
      return str(str(Px) + ', ' + str(Py))

  elif Qx>0 or Qy>0:
    return str(str(Qx) + ', ' + str(Qy))

#creating a P - Q function
def ECSub(P,Q):
  Qx, Qy = Q.split(',')
  Qx, Qy = int(Qx), int(Qy)
  #turning (Px, Py) into (Px, -Py)
  Qy = (-1*Qy)%p
  Q = str(str(Qx) + ', ' + str(Qy))
  return ECAdd(P,Q)

#creating a a**P function
def ECMult(P,a):
  M = '0,0'
  #finding the binary of 'a' helps us simplify it for calculation
  #example: a = 9 = 2^3 + 1 = ECAdd((ECDouble(P))^3,P)
  bi = bin(a)[2:]
  for i in range(len(bi)):
    if bi[i] == '1':
      k = len(bi) - i
      Q = P
      while k > 1:
        #doubling P as many times as the value of the index of bi
        Q = ECDouble(Q)
        k -= 1
      M = ECAdd(Q, M)
  return (M)

#printing out added and subtracted values of P and Q
try:
  print("Adding point P with Q (P + Q) yeilds:\n {}\n".format(ECAdd(P,Q)))
  print("Subtracting point P with Q (P - Q) yeilds:\n {}\n".format(ECSub(P,Q)))
except:
  None

#printing out multiplied value of a and P
try:  
  print("a multiplied with point P (P*a) yeilds:\n {}\n".format(ECMult(P,a)))
except:
  None

example = open('input.txt', 'r')
text = example.read().split('\n')
#if the last input value has a ',' it means it is a point. Initializing values accordingly.
A, B, p, G, Q_A, b, ciphertext = text[:]
A, B, p, b = int(A), int(B), int(p), int(b)
example.close()

#print(A, B, p, G, Q_A, b, ciphertext)

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

#creating a a*p function
def ECMult(P,a):
  #finding binary of 'a' helps simplify the calculation
  #example: a = 9 = 2^3 + 1 = ECAdd((ECDouble(P))^3,P)
  bi = bin(a)[2:]
  k, Q = len(bi), P
  bi_mul = [P]
  #finding ECDouble(P) for all possible powers of 2 (refer example)
  while k>1:
    Q = ECDouble(Q)
    bi_mul.append(Q)
    k -= 1
  #adding all the possible values in referance to the binary of 'a'
  Q = '0,0'
  for i in range(len(bi)):
    if bi[::-1][i] == '1':
      Q = ECAdd(Q,bi_mul[i])
  return Q

#finding Q_A * b for shared key K
K = ECMult(Q_A,b)
Kx , Ky = K.split(',')

def int2bin(Kx):
  Kxbin = str(bin(int(Kx))[2:])
  while len(Kxbin)%8!=0:
    Kxbin = '0'+Kxbin
  return Kxbin

Kxbin = int2bin(Kx)

#the X cordinate of K
#print('\nKxbin: ' + Kxbin)

#XORing the K with ciphertext to get key
key = []
for i in range(len(ciphertext)):
  if ciphertext[i] == Kxbin[i]:
    key.append('0')
  else:
    key.append('1')
key = (''.join(key))

#print('\nkey: ' + key)

part = [key[i:i+8] for i in range(0, len(key), 8)]
string = ''
for i in range(len(part)):
  k = chr(int(part[i],2))
  string += k
print("\nThe message is: "+ string)
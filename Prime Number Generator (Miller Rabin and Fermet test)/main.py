import random

example = open('input.txt', 'r')
text = example.read().split('\n')
number = int(text[0])
example.close()

#FAST POWER FUNCTION
def modpow(four,three,one):
  #CONVERT THE NUMBER three TO BINARY AND FIND IT'S SUBPARTS
  binary = list(bin(int(three)))[2:]
  power = []
  for i in range(len(binary)):
    if binary[i] == '1':
      power.append(2**(len(binary)-i-1))

  table = []
  tablekey = []
  x=1
  j = (int(four))%int(one)
  tablekey.append(x)
  table.append(j)
  while x<power[0]:
    j=(j*j)%int(one)
    table.append(j)
    x *= 2
    tablekey.append(x)
  
  m = 1
  for i in range(len(power)):
    m = (m * table[tablekey.index(power[i
    ])])%int(one)
  return m

#GENERATE RANDOM NUMBERS AND PICK ONE THAT SATISFIES FERMET'S LITTLE THOREM
x=y=2
while x!=1 and y!=1:
  n=2*(random.getrandbits(number))+1
  x = modpow(49, n-1, n)
  y = modpow(27, n-1, n)
  #print(x, n)

#USE THE PICKED NUMBER AGAINST MILLER'S THEOREM WITH SEVERAL TRIAL NUMBERS AND PRINT RESULTS FOR EACH
trial = [20,58,71,11]
i = len(trial)-1
while i>-1:
  p, k = n-1, 0
  while p%2==0:
    if p%2==0:
      k+=1
    p = p//2
  q = p
  p, a = n-1, trial[i]
  print('\n number: {},  k: {}, q: {}, a: {}\n '.format(n, k, q, a))


  m = modpow(a,q,n)
  #print(m, k)
  if m==1 or m==p:
    print('{} thinks {} is prime BY MILLER THEOREM'.format(a,n))
  elif (k==1 and (m!=p or m==1)):
    print('{} thinks {} is Composite BY MILLER THEOREM'.format(a,n))


  while (m!=1 and m!=p and k>0):
    m = (m**2)%n
    k -= 1
    #print(m, k)
    if (k==1 and m!=p) or (m==1):
      print('{} thinks {} is Composite BY MILLER THEOREM'.
      format(a,n))
    elif (k==1 and (m==p or m==1)):
      print('{} thinks {} is Prime BY MILLER THEOREM'.format(a,n))


  if k==0 and m!=1:
    print('{} thinks {} is Composite BY FERMET THEOREM'.format(a,n))
  elif k-1==0 and (m**2)%n==1:
    #print((m**2)%n, k-1)
    print('{} thinks {} is Prime BY FERMET THEOREM'.format(a,n))
  i -= 1

print('\n The prime number generated is: {}'.format(n))
#READ THE INPUT FILE TO GET all the variables
example = open('input.txt', 'r')
text = example.read().split('\n')
p, g, A, a = text[:]

#DEFINE MESSAGE AND RANDOM NUMBER
#CONVERT MESSAGE INTO BINARY AND THEN DECIMAL
m = 'my name is Anand123'
binary = []
for i in range(len(m)):
  binary.append(bin(ord(m[i]))[2:])
for i in range(len(binary)):
  while len(binary[i]) % 7 != 0:
    binary[i] = '0' + binary[i]
m = int((''.join(binary)),2)
r = 12345

#FAST POWER ALGORITHM FUNCTION
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

  #FINDING THE KEY: A**b % (p)
  m = 1
  for i in range(len(power)):
    m = (m * table[tablekey.index(power[i])])%int(one)
  return m

#FINDING C1 AND C2
c1 = modpow(g,r,p)
c2 = (m*modpow(A,r,p))%int(p)

#PRINTING RESULTS TO OUTPUT FILE - OUTPUT.TXT
output = open("output.txt","w") 
L = [p+'\n', g+'\n', a+'\n', str(c1)+'\n', str(c2)] 
output.writelines(L) 
output.close()

#FINDING THE INVERSE OF C1**a
new = int(a)*(int(p)-2)
test1 = modpow(c1,new,p)
test2 = modpow(c1,a,p)
#print((test1*test2)%int(p)) #SHOULD PRODUCE 1

#FINDING THE MESSAGE
message = (test1*c2)%int(p)
message = bin(message)[2:]
parts = [message[i:i+7] for i in range(0, len(message), 7)]
string = ''
for i in range(len(parts)):
  k = chr(int(parts[i],2))
  string += k
print('THE MESSAGE IS: ' + string)


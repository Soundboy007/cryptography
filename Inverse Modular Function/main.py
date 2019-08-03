#READ THE INPUT FILE TO GET p AND g
example = open('inputsmall.txt', 'r')
text = example.read().split('\n')

#CONVERT THE NUMBER p TO BINARY AND FIND IT'S SUBPARTS
binary = list(bin(int(text[0])-2))[2:]
power = []
for i in range(len(binary)):
  if binary[i] == '1':
    power.append(2**(len(binary)-i-1))

#CREATE table TO STORE VALUES OF p**g
#CREATE tablekey TO STORE g**(2**i)
table = []
tablekey = []
x=1
j = (int(text[1]))%int(text[0])
tablekey.append(x)
table.append(j)
while x<power[0]:
  j=(j*j)%int(text[0])
  table.append(j)
  x *= 2
  tablekey.append(x)
m = 1
for i in range(len(power)):
  m = (m * table[tablekey.index(power[i])])%int(text[0])
print("THE INVERSE MODULAR FUNCTION OF g IS: " + str(m))
print("THE PRODUCT OF BOTH MODULAR FUNCTIONS % BY p IS: " + str((m*int(text[1]))%int(text[0])))


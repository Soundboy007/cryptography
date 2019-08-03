#READ THE INPUT FILE TO GET all the variables
example = open('input.txt', 'r')
text = example.read().split('\n')
one, two, three, four, five = text[:]
#p, g, b, A, message respectively

#READING THE ENGLISH DICTIONARY FROM FILES
dictionary = open('dictionary.txt','r')
dicts = dictionary.read().split('\n')

#USING FAST POWER ALGORITHM
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
key = m

binary = bin(key)[2:]
key = list(binary)
five = list(five)

#XOR-ING THE KEY TO THE UNKNOWN BINARY MESSAGE
message = []
for i in range(len(five)):
  message.append(str(int(key[i])^int(five[i])))
new = ''.join(message)

#SPLITTING THE XOR-ED BINARY INTO 8-BIT SUBPARTS
#FINDING EACH SUBPART'S EQUAVALENT ASCII CHARECTER 
#MERGE ALL THE CHARECTERS INTO A STRING 
#FIND THE ENCRYPTED OR THE DECRYPED MESSAGE USING AN ENGLISH DICTIONARY
while len(new)%8!=0:
  new = '0'+new
parts = [new[i:i+8] for i in range(0, len(new), 8)]
string = ''
for i in range(len(parts)):
  k = chr(int(parts[i],2))
  string += k

test = string.upper().split(' ')
q = 0
for i in test:
  for j in dicts:
    if j == i:
      q += 1
if q/len(test) > 0.3:
  print('DECRYPTED MESSAGE IS: ' + string)
else:
  print('ENCRYPTED BINARY MESSAGE IS: ' + new)

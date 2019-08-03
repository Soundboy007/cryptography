#READING P, Q, AND e FROM THE INPUT TEXT FILE
example = open('input.txt', 'r')
text = example.read().split('\n')
p, q, e = text[:]
p, q, e = int(p), int(q), int(e)
n = p*q
phi = (p-1) * (q-1)

#FUNCTION FOR FAST POWERING
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
    m = (m * table[tablekey.index(power[i])])%int(one)
  return m

#EXTENDED EUCLID ALGORITHM FUNCTION
#FINDING THE INVERSE OF e
u, g, x, y, k = 1, e, 0, phi, []
def new(u,g,x,y):
  if y==0:
    v = (g-e*u)/phi
    k.append(g)
    k.append(u)
    k.append(int(v))
    h = 1 / 0
    print(h)
  q = g//y
  t = g%y
  s = u - q*x
  u = x
  g = y
  x = s
  y = t
  new(u,g,x,y)

try:
  new(u,g,x,y)
except:
  None

#ASSIGNING d = e**-1
d = k[1]%phi

#WRITING BOB'S MESSAGE TO BE ENCRYPTED AND SENT TO ALICE
m = 'okay okay so ha yeah im a comedian you listen to me k? good. so there is this magical room where only i can go in and no, not perry the platypus. okay i went in this room and i found out i was wonder woman but im actually a man so yeah im just sitting there then out of the blue a walrus comes up to me and says hey you eat tacos? i say yeah i love tacos, he says oh your the person ive been looking for but i have to leave so yeah your moms chest hair okay then this butt chucker came up to me and started to chuck my butt and i said hey stop chucking my butt so she said oh sorry wrong butt and she left so yeah basically what im trying to say is that is my room and only my room and i am a complete weirdo just like your living room floor and okay so i was drinking some vitamin water then this dude comes up to me and smacks the vitamin water out of my hand and i was like dude are you serious that costed more than a microwave on sims which is bucks like what i need a duck you got howard the duck playing and im like mannn how is this pg? if this was pg it would be appropriate for ages 11 and down like man wow i cant believe my toes! owie duct tape really hurts like ur uncle owch ooh would you like some ice with that burnnnnn yeah so okay bye now i never liked you anyways...okay okay so ha yeah im a comedian you listen to me k? good. so there is this magical room where only i can go in and no, not perry the platypus. okay i went in this room and i found out i was wonder woman but im actually a man so yeah im just sitting there then out of the blue a walrus comes up to me and says hey you eat tacos? i say yeah i love tacos, he says oh your the person ive been looking for but i have to leave so yeah your moms chest hair okay then this butt chucker came up to me and started to chuck my butt and i said hey stop chucking my butt so she said oh sorry wrong butt and she left so yeah basically what im trying to say is that is my room and only my room and i am a complete weirdo just like your living room floor and okay so i was drinking some vitamin water then this dude comes up to me and smacks the vitamin water out of my hand and i was like dude are you serious that costed more than a microwave on sims which is bucks like what i need a duck you got howard the duck playing and im like mannn how is this pg? if this was pg it would be appropriate for ages 11 and down like man wow i cant believe my toes! owie duct tape really hurts like ur uncle owch ooh would you like some ice with that burnnnnn yeah so okay bye now i never liked you anyways...'

#BREAKING A LONG MESSAGE INTO SMALLER MESSAGES
def mes2parts(m):
  mes = list(m)
  newmes = []
  s = ''
  for i in range(len(mes)):
    s += mes[i]
    if i%50==0 and i>0:
      newmes.append(s)
      s = ''
  newmes.append(s)
  return(newmes)
parts = (mes2parts(m))
#print(parts) #PRINTING ALL PARTS

#CONVERTING EACH MESSAGE INTO BINARY
def mes2dec(m):
  binary = []
  for i in range(len(m)):
    binary.append(bin(ord(m[i]))[2:])
  for i in range(len(binary)):
    while len(binary[i]) % 7 != 0:
      binary[i] = '0' + binary[i]
  return int((''.join(binary)),2)


#CALCULATING LIST c WITH MESSAGE, e AND n FROM ALICE
c = []
for i in range(len(parts)):
  c.append(modpow(mes2dec(parts[i]),e,n))
#print(c)

#CALCULATING LIST k FROM BOB'S c, AND ALICE'S d, n
k = []
for i in range(len(c)):
  k.append(modpow(c[i],d,n))
#print(k)

#USING k TO FIND BOB'S MESSAGE
#CONVERTING DECIMALS INTO MESSAGE
strings = []
def dec2msg(m, mess):
  message = bin(m)[2:]
  if mess[0]==' ':
    message = '0' + message  
  part = [message[i:i+7] for i in range(0, len(message), 7)]
  string = ''
  for i in range(len(part)):
    k = chr(int(part[i],2))
    string += k
  return string

for i in range(len(k)):
  strings.append(dec2msg(k[i], parts[i]))

print('THE MESSAGE IS: ' + ''.join(strings))
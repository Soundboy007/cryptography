#READING THE INPUT TEXT
example = open('input.txt', 'r')
text = example.read().split()

#CHECKING FOR ANY LETTERS
string = 'abcdefghijklmnopqrstuvwxyz'
string = list(string)
check = ' '.join(text)
m = False
for i in check:
  if i in string:
    m = True
    break

#IF NO LETTERS FOUND, BINARY GETS CONVERTED INTO TEXT
if m == False:
  k = 0
  words = []
  while k<len(text):
    for i in text:
      test=list(map(int, i))
      x = 0
      for i in range(len(test)):
        x=x+test[i]*(2**(len(test)-i-1))
      words.append(chr(x))
      k += 1
      test = []
  print(''.join(words))

#IF LETTERS FOUND, TEXT CONVERTED INTO BINARY
else:
  test = []
  words = []
  for i in check:
    test.append(ord(i))
  for i in test:
    binary = []
    while i>0:
      binary.append(i%2)
      i = i//2
    words.append("".join(str(x) for x in binary)[::-1])
  for i in range(len(words)):
    while len(words[i])<8:
      words[i] = '0'+words[i]
  print(' '.join(words))
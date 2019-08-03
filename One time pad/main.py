alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphas = list(alphabets)

#READING THE ENGLISH DICTIONARY FROM FILES
dictionary = open('dictionary.txt','r')
dicts = dictionary.read().split('\n')

#READING CONTENT FROM THE FILE AND STORING THE FIRST LINE AS KEY
example2 = open('input.txt','r')
text = example2.readlines()
text[1] = text[1].upper()
words = text[1].split()
key = list(map(int, text[0].split()))

#CHECKING THE PERCENTAGE OF ENGLISH SIMILARITY OF CONTENT
k = 0
for i in words:
  if i in dicts:
    k += 1

#IF THERE ARE NO ENGLISH WORDS, THEN DECRYPT THE CONTENT
if (k/len(words))<0.3:
  word=[]
  texts=[]
  x=0
  for i in text[1]:
    x %= 150
    if i in alphas:
      new = (alphas.index(i)-key[x])
      new %= 26
      i = alphas[new]
      x += 1
    texts.append(i)
  word = ''.join(texts)
  print("The new message is: " + word)

#IF THERE ARE ENGLISH WORDS, THEN ENCRYPT THE CONTENT
else:
  word=[]
  texts=[]
  x=0
  for i in text[1]:
    x %= 150
    if i in alphas:
      new = (alphas.index(i)+key[x])
      new %= 26
      i = alphas[new]
      x += 1
    texts.append(i)
  word = ''.join(texts)
  print("The new message is: " + word)  

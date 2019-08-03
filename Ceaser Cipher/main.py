#READING THE ENCRYPTED MESSAGE FROM read.txt FROM FILES
message = open("read.txt", 'r')
words = message.readlines()
message.close()

#READING THE ENGLISH DICTIONARY FROM dictionary.txt FROM FILES
dictionary = open("dictionary.txt", 'r')
dicts = (dictionary.read().split('\n'))[:-1] 
dictionary.close()

#SPLITTING THE ALPHABETS INTO A LIST
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphas = list(alphabets)

#CREATING A LIST OF POSSIBLE SOLUTIONS TO THE ENCRYPTED TEXT 
text=[]
j=0
while j<25:
  for i in words[j]:
    if i in alphabets:
      index1 = alphas.index(i) + 1
      index1 = index1%26
      i = alphas[index1]
    text.append(i)
  words.append(''.join(text))
  text.clear()
  j += 1  
  
#FINDING SIMILARITY OF EACH SOLUTION TO THE ENGLISH LANGUAGE
percent = []
k=0
for i in words:
  test = i.split()
  for word in test:
    if word in dicts:
      k += 1   
  percent.append(k/len(words))
  k = 0
  test.clear()

#PRINTING SOLUTIONS THAT HAVE MORE THAN 30% OF WORDS IN ENGLISH
for i in percent:
  if i > 0.3:
    print(words[percent.index(i)])
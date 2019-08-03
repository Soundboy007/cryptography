#READING THE MESSAGE TO BE ENCRYPTED FROM inputVigenere.txt FROM FILES
example = open("inputVigenere.txt", 'r')
words = example.read().split("\n")
print(words)

#SPLITTING THE ALPHABETS INTO A LIST
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphas = list(alphabets)

#CREATING THE ENCRYPTED MESSAGE 
text = []
new = []
j = 0
for i in words[1]:
  if i in alphas:
    j %= 7
    index = (alphas.index(i) + alphas.index(words[0][j]))%26
    i = alphas[index]
    j += 1
  text.append(i)
new.append(''.join(text))
print(new[0])

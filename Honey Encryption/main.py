import math 
import random
import csv
import socket 
import geocoder

# Function to display hostname and IP address 
# This will be helpful to identify the intruder
def Host_IP(): 
    try: 
        hostName = socket.gethostname() 
        hostIP = socket.gethostbyname(hostName)
        return(hostName, hostIP)  

    except: 
        print("Unable to get Hostname and IP") 
  
host_name, host_ip = Host_IP() 

# Finding the latitude and longitude of the intruder. In this case, 'me' refers to the computer running this code
g = geocoder.ip('me')

key_space = []
singular_nouns = []
present_verbs = []
past_verbs = []

# Reading the nouns.csv which contains a word and a weight
# The weight corresponds to the likeliness of usage during conversations
# We will be using this file to populate our Message Space to test our algorithm with single words
with open('nouns.csv','r') as csvreader:
	reader = csv.reader(csvreader, delimiter=',', quotechar='|')
	for row in reader:
		singular_nouns.append((row[0],row[1]))

# Reading the verbs.csv where each row contains a verb with present-tense and corresponding past-tense along with their weights
# The weights corresponds to the likeliness of usage during conversations
with open('verbs.csv','r') as csvreader:
	reader = csv.reader(csvreader, delimiter=',', quotechar='|')
	for row in reader:
		present_verbs.append((row[0], row[1]))
		past_verbs.append((row[2], row[3]))

# Rock-You dataset is a very famous dataset containing common passwords (open-sources after the famous Rock-You company breach)
# The rockyou.csv contains only a percentage of the total passwords available in the dataset. Number passwords have been excluded from the dataset
with open('rockyou.csv','r', encoding='latin-1') as csvreader:
	reader = csv.reader(csvreader)
	for row in (reader):
		key_space.append(row[0])

# Setting the Message space, which is usually lesser than the total number of common passwords to reduce computation.
keywordNum = len(singular_nouns)      

# Given the size of our Message Space, we now calculate the n-bit binary string to accomodate all messages
#Ex: if we have 8 messages, we will have 3-bit binary strings to accomodate all messages
n=math.ceil(math.log(keywordNum,2))

# Filling the Seed Space with all possible n-bit binary strings
seeds = []
for i in range(2**n): 
  seeds.append((bin(i)[2:].rjust(n, '0')))

# Using word weights, we pick those words that have high likeliness to appear in conversations  
best_present_verbs = []
for i,j in present_verbs:
  if int(j)>90:
    best_present_verbs.append(i)
#print(best_present_verbs)

# Using word weights, we pick those words that have high likeliness to appear in conversations
best_past_verbs = []
for i,j in past_verbs:
  if int(j)>50:
    best_past_verbs.append(i)
#print(best_past_verbs)

# Using word weights, we pick those words that have high likeliness to appear in conversations
best_singular_nouns = []
for i,j in singular_nouns:
  if int(j)>50:
    best_singular_nouns.append(i)
#print(best_singular_nouns)

"""
THESE ARE THE FIVE BASIC ENGLISH QUESTION STRUCTURES:

1. [is/was] + [he/she] + [verb (prog. tense)] + [d. object]
2. [are/were] + [you/we/they] + [verb (prog. tense)] + [d. object]
3. [does/did/will/would] + [he/she] + [verb (present tense)]+ [d. object]
4. [do/did/will/would] + [you/we/they] + [verb (present tense)]+ [d. object]
5. [has/have/had] + [he/she/you/we/they] + [verb (past tense)] + [d. object]
"""

# Randomly picking one of the above five cases and filling our Message Space
def random_sentence(rand):
  rand = (random.choice(['is','was']) + ' ' + random.choice(['he','she']) + ' ' + random.choice(best_present_verbs) + 'ing ' + random.choice(best_singular_nouns) + '?') or (random.choice(['are','were']) + ' ' + random.choice(['you','we','they']) + ' ' + random.choice(best_present_verbs) + 'ing ' + random.choice(best_singular_nouns) + '?') or (random.choice(['does','did','will','would']) + ' ' + random.choice(['he','she']) + ' ' + random.choice(best_present_verbs) + ' the ' + random.choice(best_singular_nouns) + '?') or (random.choice(['does','did','will','would']) + ' ' + random.choice(['you','we','they']) + ' ' + random.choice(best_present_verbs) + ' the ' + random.choice(best_singular_nouns) + '?') or (random.choice(['has','have','had']) + ' ' + random.choice(['he','she','you','we','they']) + ' ' + random.choice(best_past_verbs) + ' the ' + random.choice(best_singular_nouns) + '?')

  return rand

# 'sentences' forms our Message Space
rand = ''
sentences = []
for i in range(0,keywordNum):
  sentences.append(random_sentence(rand))
#print(sentences)

# Defining our Honey Encryption definition which takes in the Seed Space, Message Space and the Key Space to encrypt and decrypt a given message
def HE(seeds,message_space,key_space):
  choice = True
  countdown = 0

  """
  ENCRYPTION ====================================================
  """

  user_password = input('Please enter your password: \n')
  user_message = input('Please enter your message: \n')
  #user_password = 'anand'
  #user_message = 'does she make pasta?'
  
  # If the user message is a single word, then, we make a tuple with it. This makes it consistant with other words in the message space
  usermess = user_message.split(' ')
  if len(usermess)==1:
    user_message = (user_message, '0')

  random.shuffle(message_space)
  
  # For the Message function, we use decreasing order of the Seed Space
  seeds.sort(reverse=True)
  # Inserting user_message randomly into our Message space
  message_space[random.randint(0,len(message_space))] = user_message
  # Mapping index of user_message to the Seed space and getting the corresponding Seed binary
  MSbin = seeds[message_space.index(user_message)]
  
  # For the key function, we use ascending order of the Seed Space
  seeds.sort()
  # Inserting user_password randomly into our Key space
  key_space[random.randint(0,len(key_space))] = user_password
  # Mapping index of user_password to the Seed space and getting the corresponding Seed binary
  KSbin = seeds[key_space.index(user_password)%keywordNum]

  #print(MSbin, KSbin)

  def xor(string1, string2):
    xoxo = []
    for i in range(len(string1)):
      if string1[i] == string2[i]:
        xoxo.append('0')
      else:
        xoxo.append('1')
    xoxo = (''.join(xoxo))
    return xoxo

  # Taking XOR of MSbin and KSbin to get Xbin
  Xbin = xor(MSbin, KSbin)

  # Finding the index of Xbin in seeds and storing in 'i'
  i = seeds.index(Xbin)%keywordNum

  """
  DECRYPTION ==================================================
  """
  while choice:

    unknown_password = input('\nplease enter the password to unlock message: \n')
    #unknown_password = 'anand123'

    # If unknown_password is in key space, evidence of an attack can be seen
    if unknown_password in key_space:
      # Mapping index of user_password to the Seed space and getting the corresponding Seed binary - KSbinp (KSbin prime)
      KSbinp = seeds[key_space.index(unknown_password)%keywordNum]

      # XORing KXbinp and Xbin to yeild a binary string MSbinp (MSbin prime)
      MSbinp = xor(KSbinp, Xbin)

      seeds.sort(reverse=True)

      # Retrieving the index 'j' from the Seed space using the seeds index
      j = seeds.index(MSbinp)%keywordNum
      seeds.sort()
      
      # Using 'j' to output a message from Message Space
      # If j == i, then generated_message == user_message
      generated_message = message_space[j]
      
      # To be consistent with the rest of the Messages in the Message Space, the following is done
      try:
        if int(generated_message[1])>=0:
          print('THE MESSAGE IS:')
          print(generated_message[0])
      except:
        print('THE MESSAGE IS:')
        print(generated_message)
      
      # Coundown helps us define how many tries the attacker have to do to ring an alarm of possible data breach
      if unknown_password != user_password:
        countdown += 1

    # If the provided user_password doesn't appear in the common_passwords list, they do not pose any immediate threat to the system
    else:
      print('Invalid credentials')

    # The following message will be sent to the server/database directory/log file/phone of company owner when a potential breach is seen
    if countdown >= 3:
      print('\nINTRUDER DETECTED ####################################')
      print("Hostname :  ",host_name) 
      print("IP : ",host_ip)
      print("Latitude and Longitude: ", g.latlng)  
      print('######################################################')

    cont = input('\npress "y" to try again, press "n" to exit: ')
    if cont == ('n' or 'N'):
      choice = False

option = input('enter 1 to test against words, or enter 2 to test against sentences: ')
if option == 1 or option == '1':
  HE(seeds,singular_nouns,key_space)
elif option == 2 or option == '2':
  HE(seeds,sentences,key_space)
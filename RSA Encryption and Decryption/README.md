For this script, I will be both Alice and Bob. I will provide P, Q and e in the input.

For the Bob, half of my script will encrypt any message. I want this script to be able to handle messages that are longer than PQ. To do that, the scipt splits the message into smaller chunks based on the size of PQ, then encrypting the chunks individually. The ciphertext variable C of each chunk can then be appended to a list to later be handled iteratively. 

For the Alice half of the script, the encrypted message from Bob will be taken and calculates the decipher variable d, and prints out the decrypted message.

Source: https://en.wikipedia.org/wiki/RSA_(cryptosystem)

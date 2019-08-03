A brute-force attack involves repeated decryption with random keys; this is equivalent to picking random plaintexts from the space of all possible plaintexts with a uniform distribution. This is effective because even though the attacker is equally likely to see any given plaintext, most plaintexts are extremely unlikely to be legitimate i.e. the distribution of legitimate plaintexts is non-uniform. Honey encryption defeats such attacks by first transforming the plaintext into a space such that the distribution of legitimate plaintexts is uniform. Thus an attacker guessing keys will see legitimate-looking plaintexts frequently and random-looking plaintexts infrequently. This makes it difficult to determine when the correct key has been guessed. In effect, honey encryption serves up fake data in response to every incorrect guess of the password or encryption key.

The security of honey encryption relies on the fact that the probability of an attacker judging a plaintext to be legitimate can be calculated (by the encrypting party) at the time of encryption. This makes honey encryption difficult to apply in certain applications e.g. where the space of plaintexts is very large or the distribution of plaintexts is unknown.

The input files will be: 
List of nouns, verbs, transition verbs, for making a plausible sentence; and the Rock You dataset that contains a list of commonly used passwords.

source: 

Honey Encryption: Security Beyond the Brute-Force Bound 

By Ari Juels and Thomas Ristenpart 
https://link.springer.com/content/pdf/10.1007/978-3-642-55220-5_17.pdf

"The Password That Never Was" (Harvard's CRCS Lunch Seminar) 
https://www.youtube.com/watch?v=DV0k0rQpEX4

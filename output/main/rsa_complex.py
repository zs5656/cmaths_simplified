import random
import sys
import os
import cryptomath
import RabinMiller

def main():
    makeKeyFiles('Test_RSA', 2048)

def generateKeys(keySize):
    # Generate p and then q, then N = p * q
    print("Generating primes P and Q...")
    p = RabinMiller.generateLargePrime(keySize)
    q = RabinMiller.generateLargePrime(keySize)
    n = p * q

    name = "Test_RSA"
    print("\n")
    print("Writing the prime numbers P and Q to %s_primes.txt..." % name)
    file = open("%s_primes.txt" % name, 'w')
    file.write('%s,%s' % (p, q))
    file.close()

    # Generate E which is relatively prime to phi(N)
    print("Generating phi(N)...")
    phi_n = (p-1) * (q-1)

    print("Generating E that is relatively prime to phi(N)...")
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e, phi_n) == 1:
            break

    # Generate D which is the mod inverse of E
    print("Generating D that is the mod inverse of E...")
    d = cryptomath.findModInverse(e, phi_n)
    publicKey = (n, e)
    privateKey = (n, d)
    print("Public Key: ", publicKey)
    print("Private Key: ", privateKey)
    return (publicKey, privateKey)

    # Write out the public key and the private keys :D
def makeKeyFiles(name, keySize):
    if os.path.exists("%s_public.txt" % name) or os.path.exists("%s_public.txt" % name):
        sys.exit("The file already exists, unable to continue.") 
    else:
        publicKey, privateKey = generateKeys(keySize)
        print("\n")
        public0_len = len(str(publicKey[0]))
        public1_len = len(str(publicKey[1]))
        private0_len = len(str(privateKey[0]))
        private1_len = len(str(privateKey[1]))

        print("The public key is a ", public0_len, " and a ", public1_len, " digit nmber.")
        print("Writing public key to file %s_public.txt..." % name)

        file = open("%s_public.txt" % name, 'w')
        file.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
        file.close()

        print("\n")
        print("The private key is a ", private0_len, " and a ", private1_len, " digit nmber.")
        print("Writing private key to file %s_private.txt..." % name)

        file = open("%s_private.txt" % name, 'w')
        file.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
        file.close()

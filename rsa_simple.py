from string import ascii_letters
import primeg
import random

# For some reason numbers greater than 300 000 as a lower bound tend to fuck the system, error message put in.

def rsa_gen():
    largeNos = input("This program produces very large numbers in the encryption and decryption \nphases, would you like for them to be an output?\nYes has more detail, but overall takes longer than No.\nY = Yes, N = No\n")
    print("Also, try not to put the lower bound higher than about 300 000, numbers higher than that don't work very well to say the least.")
    if largeNos == 'Y':
        display_LargeNos = True
    else:
        display_LargeNos = False

    print("Enter in bounds for the generation of the prime keys.\n")
    print("=" * 30)

    low = int(input("What is the lower bound? "))
    upp = int(input("what is the upper bound? "))
    print("lower bound: ", low, "\nupper bound: ", upp)
    pr_list = primeg.primes(low, upp)
    pr_length = len(pr_list)

    if pr_length == 1:
        print("Bruh")
    else:
        p = pr_list[random.randint(0, pr_length - 1)]
        q = pr_list[random.randint(0, pr_length - 1)]

        while q == p:
            q = pr_list[random.randint(0, pr_length - 1)]
        
        print("=" * 15)
        print("p = ", p, ", q = ", q)

    n = p*q 
    print("n = ", p, " * ", q, " = ", n)

    phi_n = (p - 1)*(q - 1)
    print("Φ(n) = ", p-1, " * ", q-1, " = ", phi_n)

    e = 0
    for i in range (0, int(pr_length) - 1):
        if (phi_n % pr_list[i] != 0 and e != p and e != q):
            e = pr_list[i]
            print("e = ", e)
            break
    
    if (e == 0):
        print("No value of e found! Change upper and lower bounds")
        exit()

    d = 0
    x = 1
    while (((phi_n * x) + 1) / e) % 1 != 0:
        x = x + 1

    print("x = ", x)
    d = int(((phi_n * x) + 1) / e) 
    print("d = ", d)

    print("\n\nPublic Key e, n: ", e, " , " , n)
    print("Private Key d, n: ", d, " , " , n)

    msg = str(input("\nWhat is the message that you wish to encrypt?\n"))
    ascii_values = []
    for character in msg:
        ascii_values.append(ord(character))
    print("PlainText: \n", ascii_values)

    ascii_length = len(ascii_values)
    print(str(ascii_length) + "\n")

    # Entire series of decryptions and encryptions, all in one for loop :)
    ascii_cipher = []
    ascii_cipher2 = [] 
    ascii_decry = []
    ascii_decry2 = []

    if (display_LargeNos == True):
        for i in range (0, int(ascii_length)):
            ascii_cipher.append(ascii_values[i] ** e)
            ascii_cipher2.append(ascii_cipher[i] % n)
            ascii_decry.append(ascii_cipher2[i] ** d)
            ascii_decry2.append(ascii_decry[i] % n)

        print("Cipher, stage 1\n", ascii_cipher)
        print("Ciphertext\n", ascii_cipher2)
        print("Decry, stage 1\n", ascii_decry)
        print("Message\n", ascii_decry2)
    elif (display_LargeNos == False):
        for i in range (0, int(ascii_length)):
            # ascii_cipher.append((ascii_values[i] ** e) % n)
            # ascii_decry2.append((ascii_cipher[i] ** d) % n)
            ascii_cipher.append(pow(ascii_values[i], e, n))
            ascii_decry2.append(pow(ascii_cipher[i], d, n))
        print("Ciphertext\n", ascii_cipher)
        print("Message\n", ascii_decry2)

    d_message = []
    for i in range (0, int(ascii_length)):
        d_message.append(chr(ascii_decry2[i]))

    print("\n\nFinal Message:\n", d_message)
    s = ''.join(d_message)
    print(s)

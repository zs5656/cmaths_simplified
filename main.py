import primeg
import rsa_simple
import rsa_complex
from sympy import factorint
import time

def main():
    # sets what mode the program should run in, if called. 
    print("Select the mode this application should run:\n")
    print("1 - generate primes\n2 - simple factorisation\n3 - complex factorisation\n4 - Simple RSA Generation\n5 - even better factorisation")

    mode = int(input())
    if mode == 1:
        primeg.prime_userT()
        main()
    elif mode == 2:
        primeg.fact_simple()
        main()
    elif mode == 3:
        primeg.fact_complex()
        main()
    elif mode == 4:
        rsa_simple.rsa_gen()
        main()
    elif mode == 5:
        n_input = int(input("Enter the number you want to factorise: "))
        t0 = time.time()
        print(factorint(n_input))
        print(time.time() - t0, " s processing time. ")
        main()
    elif mode == 42069:
        rsa_complex.main()
        main()
    else:
        print("Bruh")
        main()

main()
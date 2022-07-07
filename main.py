import primeg
import rsa_simple
import rsa_complex

def main():
    # sets what mode the program should run in, if called. 
    print("Select the mode this application should run:\n")
    print("1 - generate primes\n2 - simple factorisation\n3 - complex factorisation\n4 - Simple RSA Generation")

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
    elif mode == 42069:
        rsa_complex.main()
        main()
    else:
        print("Bruh")
        main()

main()
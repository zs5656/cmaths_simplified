import math
import time

# This here is python 3.10 code. Now unfortunately because Visual Studio 2022 is a dumbfuck it didn't support it and I'm not changing it because I don't feel like it.
#match mode:
#    case 1:
#        prime_userT()
#    case 2:
#        fact_simple()
#    case 3:
#        fact_complex()
#    case _:
#        print("bruh")

def isPrime(num):
    # Function that runs through numbers and checks if it is prime.
    # Normally, you only have to search for number N possible factors up to N / 2 or sqrt(N)
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
                break
        else:
            return True
    else:
        return False

def prime_userT():
    # This is for if the prime function is triggered by the user manually and not as part of another function

    low = int(input("What is the lower bound? "))
    upp = int(input("what is the upper bound? "))
    primes(low, upp)

def primes(lower_bound, upper_bound):
    f = open("primes.txt", 'w')
    primes = []

    # Runs through numbers from LB -> UB to check for primes & appends it to val[] 
    for val in range(lower_bound, upper_bound):
        for i in range(2, int(math.sqrt(val) + 1)):
            if (val % i == 0):
                break
        else:
            primes.append(val)
            #print(val)
    print("Prime numbers generated: ", primes, "\n")    
    f.write(str(primes))
    f.close()
    return primes

def fact_simple():    
    # Simple factorisation method, which will run through every number until the number input say N is reduced to 1. 
    # Complex factorisation method first compiles a list of primes and will only test for the primes. However, this in practice ends up being even slower than simple factorisation for very small numbers...
    t0 = time.time()

    n_input = int(input("Enter the number you want to factorise: "))
    factors = []
    if (isPrime(n_input)):
        print(n_input)
    else:
        while(n_input != 1):
            for i in range(2, int(n_input), 1):
                while(n_input % i == 0):
                    print(i)
                    factors.append(i)
                    n_input /= i
                if(n_input == 1):
                    break
    
        print(factors)
        print(time.time() - t0, " s processing time. ")


def fact_complex():
    t0 = time.time()

    factors = []
    n_input = int(input("Enter the number you want to factorise: "))
    if (isPrime(n_input)):
        print(n_input)
        factors.append(int(n_input))
    else:
        primel = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

        sqrt_n = int(math.sqrt(n_input))
        if (sqrt_n > 997):
            primeL2 = primes(997, sqrt_n)
            primel.extend(primeL2)

        while(n_input != 1 and isPrime(n_input) == False):
            for i in range(0, len(primel)):
                while(n_input % primel[i] == 0):
                    print(primel[i])
                    factors.append(primel[i])
                    n_input /= primel[i]
                if n_input in primel:
                    break 
        print(int(n_input))
        factors.append(int(n_input))
    print(factors)
    print(time.time() - t0, " s processing time. ")

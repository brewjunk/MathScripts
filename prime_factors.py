#prime_factors.py
#Version 1.00 (Changed on 12 Jun 18:23)
#!/usr/bin/env python3

import time
with open('million_primes.txt', 'r')as million_prime_factors:
    prime_factor_list = []
    prime_factor_txt = million_prime_factors.read()
    split_prime_factor_txt = prime_factor_txt.split(',')
    for item in split_prime_factor_txt[0:100000000]:
        int_item = int(item)
        prime_factor_list.append(int_item)

while True:
    print("""
              |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
              |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
              |||||||||||!!|||||||PRIME FACTORS !||||||||!!||||||||||||||!!|||
              |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||

    """)
    user_num = input("              Please enter a number that is not less than or equal to 0!")

    if int(user_num) <= 0 or int(user_num) in prime_factor_list:
        print("                     Number is less than or equal to zero or you have entered a prime number")
        quit()
    else:
        print("""

        """)
        print("              Ok! Lets find the Prime Factors for {}".format(user_num))
    print("""

                  Calculating...
              ==========================""")
    time.sleep(1)
    prime_factors = []
    for num in prime_factor_list:
        if num >= int(user_num):
            break
        elif int(user_num) % num == 0:
            prime_factors.append(num)
            print("              {} is a prime factor of {}".format(num, user_num))
            print("              __________________________")
    calc_num = int(user_num)

    prime_factors_final = []
    index_position = -1
    while True:
        while calc_num % prime_factors[index_position] == 0:
            print("              ||||Checking..{}! {}/{} This number is divisible by {} ".format(prime_factors[index_position], calc_num, prime_factors[index_position], prime_factors[index_position]))
            calc_num = calc_num // prime_factors[index_position]
            prime_factors_final.append(prime_factors[index_position])
        index_position = index_position -1
        if calc_num == 1:
            break
        else:
            continue

    x = "x".join(str(item) for item in sorted(prime_factors_final, reverse = False))
    print("""
              ***************************************************
    """)
    print("              The Prime factors for the number {}".format(user_num),"are", x)
    print("""
              ***************************************************
    """)
    check = input("""              Would you like to try another number?: (Type 1 to try another, Or 0 to quit!)
    """)
    print("""

                  |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||""")
    if check == "0":
        print("                    Ok then, Thanks! Good bye!")
        print("""

                  |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||""")
        break
    elif check == "1":
        continue

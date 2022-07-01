#simplify_fraction.py
#Version 1.01 (Changed on 1 Jul 21:51)
#!/usr/bin/env python3

import time
while True:
    print("""
          |||||||||!!||||||||||||||!!||||||||||||||||!!||||||||||||||!!|||
          |||||||||!!||||||||||||||!!||||||||||||||||!!||||||||||||||!!|||
          |||||||||!!||||||||||SIMPLIFY A FRACTION||!!!||||||||||||||!!|||
          |||||||||!!||||||||||||||!!||||||||||||||||!!||||||||||||||!!|||
          Reducing or simplifying a fraction by dividing both the
          nominator and denominator by a number greater than 0.

    """)
    user_nom_input = input("          Please enter the nominator   >> ")
    user_denom_input = input("          Please enter the denominator >> ")

    if len(user_nom_input) == 0:
        quit()
    else:
        pass
    usr_num_list = []
    usr_num_list.append(int(user_nom_input))
    usr_num_list.append(int(user_denom_input))

    def find_divisors(usr_num_list):
        list_of_divisors = []
        for number in range(2):
            print("          | Number[{}] >>> {} ".format(number+1,usr_num_list[number]))
            for divisor in range(1, int(usr_num_list[number])+1):
                if int(usr_num_list[number]) % divisor == 0:
                    list_of_divisors.append(divisor)
        return(list_of_divisors)
    factors = find_divisors(usr_num_list)

    def list_common_factors(factors):
        common_factors = []
        for num in factors:
            if factors.count(num) == 2:
                if num not in common_factors:
                    common_factors.append(num)
        return common_factors

    x = list_common_factors(factors)
    HCF = x[-1]
    #print(HCF)
    result_lst = []
    for number in usr_num_list:
        result = number / HCF
        result_lst.append(int(result))

    print("""
                |  {}  |
                  ___
                |  {}  |

    """.format(result_lst[0],result_lst[1]))

    print("""


    """)

    check = input("""          Would you like to try another set?:
          (Type 1 to try another, Or 0 to quit!)
        """)
    print("""

          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||""")
    if check == "0":
        print("          Ok then, Thanks! Good bye!")
        print("""

          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||""")
        break
    elif check == "1":
        continue
    elif check != "1" and check != "2":
        check = input("""          Would you like to try another set?:
          (Type 1 to try another, Or 0 to quit!)
        """)
    print("""
    
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||""")

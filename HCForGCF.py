#Lowest common multiple or two or more numbers.
import time
while True:
    print("""
          |||||||||!!||||||||||||||!!||||||||||||||||!!||||||||||||||!!|||
          |||||||||!!||||||||||||||!!||||||||||||||||!!||||||||||||||!!|||
          |||||||||!!||FIND HIGHEST/GREATEST COMMON FACTOR|||||||||||!!|||
          |||||||||!!||||||||||||||!!||||||||||||||||!!||||||||||||||!!|||
          The greatest common factor (GCF) of a set of numbers is the
          largest factor that all the numbers share.
          Sometimes refered to as Greatest common divisor.
          For example, 12, 20, and 24 have two common factors: 2 and 4.
          The largest is 4, so we say that the GCF of 12, 20, and 24 is 4.
          GCF is often used to find common denominators.

    """)
    user_number_set = input("          Please enter a set of numbers seperated by a fullstop >> ")
    #print("          {}".format(user_number_set))
    list_user_numbers = user_number_set.split('.')
    #print(list_user_numbers)
    quantity_nums = len(list_user_numbers)
    print("""

    """)
    print("          | Calculating the HCF/GCF/GCD with: ")
    def find_divisors(list_user_numbers,quantity_nums):
        list_of_divisors = []
        for number in range(quantity_nums):
            print("          | Number[{}] >>> {} ".format(number+1,list_user_numbers[number]))
            for divisor in range(1, int(list_user_numbers[number])+1):
                if int(list_user_numbers[number]) % divisor == 0:
                    #print(divisor)
                    list_of_divisors.append(divisor)
        return(list_of_divisors)

    factors = find_divisors(list_user_numbers, quantity_nums)

    def list_common_factors(factors, quantity_nums):
        common_factors = []
        for num in factors:
            if factors.count(num) == quantity_nums:
                if num not in common_factors:
                    common_factors.append(num)
        return common_factors
    common_factors_output = list_common_factors(factors, quantity_nums)
        #print(factors.count(num) == quanity_nums)
    print("          | [ {} ] is the HCF (aka GCF,GCD)".format(common_factors_output[-1]))
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

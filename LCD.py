#Lowest common multiple or two or more numbers.
import time
while True:
    print("""
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
          |||||||||||!!||FIND LEAST COMMON DENOMINATOR|||||||||||||||!!|||
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
          "In mathematics, the lowest common denominator is the smallest
          number that all the numbers on the bottom of a particular group
          of fractions can be divided into." - google

    """)
    a = input("          Please enter the first nominator :")
    b = input("                           first denominator :")
    c = input("                           second nominator :")
    d = input("                           second denominator :")

    print("""          You have entered:

                       {}/{}

                       and

                       {}/{}
             """.format(a,b,c,d))
    a_list = []
    b_list = []
    for i in range(1,1000):
        mult_a = int(b) * i
        a_list.append(mult_a)
    for i in range(1,1000):
        mult_b = int(d) * i
        b_list.append(mult_b)
    for product in b_list:
        if product in a_list:
            LCD = int(product)

            print("          The LCD of the two denominators is {}".format(product))
            break
    print("""          So, The unsimplified answer is :

                       {}/{}

                       and

                       {}/{}
             """.format((((int(a))*(int(LCD/int(b))))),LCD,(int(c))*(int(LCD/int(d))),LCD))
    check = input("""          Would you like to try another pair?:
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

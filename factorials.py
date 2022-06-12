while True:
    print("""
    |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
    |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
    |||||||||||!!|||||||FACTORIALS!||||||||||||!!||||||||||||||!!|||
    |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
    
    
    """)
    usr_num = input("    Please enter an integer to find the factorial:")
    print("    You have entered ", usr_num)
    f_num = int(usr_num)
    count = int(usr_num)
    f_list = []

    for num in range(1,count+1):
        count = count - 1
        f_list.append(num)
    f_list_sorted = sorted(f_list, reverse = True)

    acc = f_num
    it_counter = 1
    for num in f_list_sorted:
        acc = acc * f_list_sorted[it_counter]
        if it_counter == f_num-1:
            continue
        else:
            it_counter += 1
    print("""      
    
    What is a factorial of {}?
     
    The value of factorial of {} is {}
    
    """.format(f_num,f_num,acc))
    x = "x".join(str(item) for item in f_list_sorted)
    print("    The expression for {}! = ".format(f_num),x)
    print("""
    
    
    
    |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
    |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
    
    """)
    check = input("""    Would you like to try another number?: (Type Yes to try another, Or No to quit!)
    """ )
    print("""

    |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||""")
    if check.upper() == "NO":
        print("Ok then, Thanks! Good bye!")
        break
    else:
        continue
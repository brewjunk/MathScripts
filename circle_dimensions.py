import math
while True:
    print("""
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
          ||||||!!||Find Circumference,radius,area of circle.||||||||!!|||
          |||||||||||!!||||||||||||||!!||||||||||||||!!||||||||||||||!!|||
          C = 2πr
                A = π(r)**2
                A = π × r2, where 'r' is the radius.
                A = (π/4) × d2, where 'd' is the diameter.
                A = C2/4π, where 'C' is the circumference.
                    r = C / π/2
                        D = r * 2

    """)
    def find_circumference(r):
        """C=2πr"""
        C = 2 * (math.pi) * float(r)
        print("          The circumference of the circle is:{:0.4f} units".format(C))

    def find_area_of_circle(r):
        """A = π(r)**2
        Area = π × r2, where 'r' is the radius.
        Area = (π/4) × d2, where 'd' is the diameter.
        Area = C2/4π, where 'C' is the circumference."""
        A = (math.pi) * (float(r)*float(r))
        print("          The area of the circle is :{:0.4f} Squared units".format(A))

    def find_radius_of_circle(C):
        """Find radius if you have circumference"""
        r = float(C)/(math.pi)/2
        print("          The radius of the circle is:{:0.4f} units".format(r))

    # Ask user what they want to know!
    ask = input("""          What would you like to find out ?
                    [0] Circumference [1] Area of the circle [2] Radius""")
    print("""

    """)
    if int(ask) == 0:
        find_circumference(input("          Please enter the radius of the circle to find circumference:"))
    elif int(ask) == 1:
        find_area_of_circle(input("          Please enter the radius of the circle to find area:"))
    elif int(ask) == 2:
        find_radius_of_circle(input("          Please enter the circumference of the circle to find radius:"))
    # Ask user what they want to know!
    print("""

    """)
    check = input("""          Would you like to find another?:
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

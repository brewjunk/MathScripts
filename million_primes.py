with open("P-1000000.txt", 'r') as million_pfactors:
    million_primes_factors = million_pfactors.readlines()
    million_primes = []
    for line in million_primes_factors[0:1000000]:
        line2 = line.replace(' ','')
        line_split = (line2.split(','))
        million_primes.append(line_split[1])
    with open("million_primes.txt", "w") as file:
        for items in million_primes:
            file.writelines(items + ',')

    print(million_primes)
    # .replace(' ','')
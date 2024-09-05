def CTF(celsius):
    return (celsius * 9/5) + 32


cV =input("enter the tempraturs with space:\n")
c=list(map(float, cV.split()))

my_map=list(map(CTF,c))
print(my_map)
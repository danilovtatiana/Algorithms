#calculate mass, density or volume

flag = input("What to calculate? (m,v,d):")

if flag == "m":
    d = float(input("Density:"))
    v = float(input("Volume:"))
    result = d * v
elif flag == "d":
    m = float(input("Mass:"))
    v = float(input("Volume:"))
    result = float(m/v)
else:
    m = float(input("Mass:"))
    d = float(input("Density:"))
    result = float(m/d)
print(result)
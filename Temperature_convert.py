#temperature convert C-F or vice versa

t = int(input())
scale = input()

if scale == "F" or scale == "f":
    t = round((t-32)/1.8)
elif scale == "C" or scale == "c":
    t = round(1.8*t + 32)
print(t)
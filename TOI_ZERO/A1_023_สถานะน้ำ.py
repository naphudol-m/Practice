t = int(input())
u = input()

if (u == "c" and t <= 0) or (u == "C" and t <= 0) : 
    print("solid")
elif (u == "c" and t >= 100) or (u == "C" and t >= 100) : 
    print("gas")
elif (u == "f" and t <= 32) or (u == "F" and t <= 32) : 
    print("solid")
elif (u == "f" and t >= 212) or (u == "F" and t >= 212) : 
    print("gas")
else:
    print("liquid")
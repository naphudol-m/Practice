y = int(input())
c = int(input())

if y <= 1990:
    if c <= 1500:
        print("1250")
    elif c > 1500 and c <= 2000:
        print("1400")
    elif c > 2000:
        print("2000")
elif y > 1990 and y < 2000 :
    if c <= 1500:
        print("1100")
    elif c > 1500 and c <= 2000:
        print("1300")
    elif c > 2000:
        print("1700")
elif y >= 2000 :
    if c <= 1500:
        print("1000")
    elif c > 1500 and c <= 2000:
        print("1200")
    elif c > 2000:
        print("1500")
t = input()
txt = ""
n = 0
c = t[0]

for i in t :
    if c == i:
        n+=1
    else:
        txt += str(n) + c
        c = i
        n = 1
txt += str(n) + i
print(txt)
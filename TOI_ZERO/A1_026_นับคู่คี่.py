a = int(input())
b = int(input())
c = int(input())
list_n = [a,b,c]
even =0
odd =0

for i in list_n :
    if i % 2 == 0 :
        even += 1
    else:
        odd += 1
print("even",even)
print("odd",odd)
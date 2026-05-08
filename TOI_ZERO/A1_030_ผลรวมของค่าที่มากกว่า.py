n = int(input())
number = [int(x) for x in input().split()]
if n == 1:
    print(max(number))
else:
    bigger = []
    for i in range(0,n*2,2):
        if number[i] > number[i+1]:
            bigger.append(number[i])
        else:
            bigger.append(number[i+1])
    result = sum(bigger)
    bigger_string = [str(x) for x in bigger]
s = " + ".join(bigger_string)
print(s+   " = " +  str(result))

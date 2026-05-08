num = input()
a = input()
sum = 0
multiple = 0
reversed_num = int(num[::-1])

if a == "+" and num[-1] == 0:
    sum = int(num) + int(num[-2])
    print(num , a , reversed_num ,"=" ,sum)

elif a == "+" and num[-1] != 0:
    sum = int(num) + int(num[::-1])
    print(num , a , reversed_num ,"=" ,sum)

else :
    multiple = int(num) * int(num[::-1])
    print(num , a , num[::-1] ,"=" ,multiple)
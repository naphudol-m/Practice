num = input()
a = input()
sum = 0
multiple = 0
reversed_num = int(num[::-1])

if a == "+":
    sum = int(num) + reversed_num
    print(num , a , reversed_num ,"=" ,sum)

else :
    multiple = int(num) * reversed_num
    print(num , a , num[::-1] ,"=" ,multiple)
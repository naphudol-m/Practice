input_1 = input()
point = input_1[0]
group = input_1[1]

# group_10 = input_1[-1]
# print(len(input_point_group))
# print(type(len(input_point_group)))
# print("เช็ค",input_1)

if input_1 == "10h" or input_1 == "10H" :
    print("10 of hearts")
elif input_1 == "10D" or input_1 == "10d" :
    print("10 of diamonds")
elif input_1 == "10S" or input_1 == "10s" :
    print("10 of spades")
elif input_1 == "10C" or input_1 == "10c" :
    print("10 of clubs")

elif point == "A" or point == "a" :
    if group == "D" or group == "d" :
        print("ace of diamonds")
    elif group == "H" or group == "h" :
        print("ace of hearts")
    elif group == "S" or group == "s" :
        print("ace of spades")
    elif group == "C" or group == "c" :
        print("ace of clubs")

elif point == "Q" or point == "q" :
    if group == "D" or group == "d" :
        print("queen of diamonds")
    elif group == "H" or group == "h" :
        print("queen of hearts")
    elif group == "S" or group == "s" :
        print("queen of spades")
    elif group == "C" or group == "c" :
        print("queen of clubs")

elif point == "J" or point == "j" :
    if group == "D" or group == "d" :
        print("jack of diamonds")
    elif group == "H" or group == "h" :
        print("jack of hearts")
    elif group == "S" or group == "s" :
        print("jack of spades")
    elif group == "C" or group == "c" :
        print("jack of clubs")

elif point == "K" or point == "k" :
    if group == "D" or group == "d" :
        print("king of diamonds")
    elif group == "H" or group == "h" :
        print("king of hearts")
    elif group == "S" or group == "s" :
        print("king of spades")
    elif group == "C" or group == "c" :
        print("king of clubs")

elif int(point) < 11 :
    if group == "D" or group == "d" :
        print(point," of diamonds")
    elif group == "H" or group == "h" :
        print(point," of hearts")
    elif group == "S" or group == "s" :
        print(point," of spades")
    elif group == "C" or group == "c" :
        print(point," of clubs")

# elif input_point_group[0] =="1" and input_point_group[1] =="0" : #กรณี 10D 10H 10S 10C
#     print("เข้าเงื่อนไข")
#     if group_10 == "D" or group_10 == "d" :
#         print("10 of diamonds")
#     elif group_10 == "H" or group_10 == "h" :
#         print("10 of hearts")
#     elif group_10 == "S" or group_10 == "s" :
#         print("10 of spades")
#     elif group_10 == "C" or group_10 == "c" :
#         print("10 of clubs")
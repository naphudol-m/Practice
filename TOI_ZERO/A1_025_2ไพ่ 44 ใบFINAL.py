input_1 = input()
point = input_1[0]
group = input_1[1]


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
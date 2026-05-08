# รหัสที่ถูกคือ H 4567 
alpha = input()
num = input()

if alpha == "H" and num == "4567" :
    print("safe unlocked")

elif alpha != "H" and num == "4567": #อักษรผิด,เลขถุก
    print("safe locked - change char")

elif alpha == "H" and num != "4567": #อักษรถูก,เลขผิด
    print("safe locked - change digit")

else:
    print("safe locked")
fname = input()
lname = input()
age = input()

if len(fname) > 5 :
    pass_1 = fname[0:2] + lname[-1] + age[-1]
    print(pass_1)

else:
    pass_2 = fname[0] + age + lname[-1]
    print(pass_2)
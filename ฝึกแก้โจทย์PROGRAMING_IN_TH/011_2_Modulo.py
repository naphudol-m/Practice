# รับ10ค่า
list_remainder = list()
for i in range(10) :
    num = int(input())
    remainder = num % 42
    list_remainder.append(remainder)

# จำนวนรูปแบบจากการ modulo
set_remainder = set(list_remainder)
print(len(set_remainder))
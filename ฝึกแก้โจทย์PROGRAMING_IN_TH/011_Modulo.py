remaindets = set()
for i in range(10):
    num = int(input())
    remaindets.add(num % 42)

print(len(remaindets))
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in reversed(range(1, 21)):
    print(i, end=' ')
print()

print("*")
number = int(input("Number: "))
for i in range(number):
    print("*", end=' ')
print()

print("---")
loop = 0
while loop < number:
    loop += 1
    print(loop*"*")

user_name = str(input("Insert user name: "))
file_write = open("data.txt", "w")
file_write.write(user_name)
file_write.close()

file_read = open("data.txt", "r")
print("Your name is", file_read.read())
file_read.close()

numbers = open("numbers.txt", "r")
line1 = int(numbers.readline())
line2 = int(numbers.readline())
line3 = int(numbers.readline())
sum1 = line1 + line2
print(sum1)

total_sum = line1 + line2 + line3
print(total_sum)
numbers.close()

"""
num = int(input("Number: "))
count = 0

while num != 0:
    num //= 10
    count += 1
print("Number of digits: " + str(count))

num1 = input("Son: ")
num2 = list(num1)
print(num2)
print("Uzunligi: ", len(num1))

step = 1
k = 10
while num >= k:
    k = k * 10
    step = step+ 1
    
print("Emil",step)"
  

s = input("stroke: ")

strArray = s.split()
result = []

for i in strArray:
    if i == ''.join(reversed(i)):
        result.append(i)

print(result)



number =input("Input -> ")
if number == ''.join(reversed(number)):    print("Palindrome")
else:    print('Not palindrome')

"""

x = 8768
result = [int(j) for j in str(x)]
print(result)








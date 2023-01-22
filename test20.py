n = int(input("Please enter n:"))
a = 1
b = 1
sum = 2
count = 1

print("Fibonacci series is: ", end = " ")

while(count <= n):
  count += 1
  print(a, end=" ")
  a = b
  b = sum
  sum = a + b
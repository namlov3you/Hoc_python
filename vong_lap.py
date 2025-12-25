for i in range(1, 6):
    #print(i, end=" ")
    if i%2 == 0:
        print(i)
        
for i in range(3):
    for j in range(2):
        print(i, j)
        
print("-----------")
data = {"a": 10, "b": 20}

for k in data:
    print(k, data[k])

print("-----------")
x = 1
while x < 10:
    x = x + 1
    print(x)

print("---Bài tập bảng cửu chương---")

n = int(input("Nhập số n: "))

for i in range(1,11):
    print(n, "x",i,"=",i*n)

print("--- đếm in happy new years ---")

import time

for i in range(10, 0, -2):
    print(i)
    time.sleep(1)

print("HAPPY NEW YEAR!")

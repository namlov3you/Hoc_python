n = int(input("nhập số n: "))

check = True

if n < 1:
    check = False
else:
    for i in range(2,n-1):
        if n % i == 0:
            check = False
            break

if check == True:
    print(n, "là số nguyên tố")
else:
    print(n,"không phải số nguyên tố")
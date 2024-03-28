#câub:
print("các số chính phương từ 1 đến 1000 là:")
S1 = 1
for i in range(1,1001):
    for j in range(1,i):
        if j*j == i:
            print(i, end=' ')
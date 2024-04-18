n = int(input("Nhập số phần tử của mảng: "))
list_1 = []

for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    list_1.append(so)
    if so > 1:
        neu_so = True
        for j in range(2, so):
            if so % j == 0:
                neu_so= False
                break
        if neu_so:
            print(f"{so} là số nguyên tố.")
    tong = 0
    for j in range(1, so):
        if so % j == 0:
            tong += j
    if tong == so:
        print(f"{so} là số hoàn hảo.")

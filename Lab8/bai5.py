def tong_cac_uoc(n):
    tong = 1  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:  
                tong += n // i
    return tong

def kiem_tra_amicable(so1, so2):
    if so1 == so2:  
        return False
    tong1 = tong_cac_uoc(so1)
    tong2 = tong_cac_uoc(so2)
    return tong1 == so2 and tong2 == so1

so1 = int(input("nhập vào một số:"))
so2 = int(input("nhập vào một số:"))

if kiem_tra_amicable(so1, so2):
    print(f"{so1} và {so2} là một cặp số amicable.")
else:
    print(f"{so1} và {so2} không phải là một cặp số amicable.")

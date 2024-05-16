#Ý1:
def tong_lap_phuong_cac_chu_so(n):
    tong_lap_phuong = 0
    while n > 0:
        chu_so = n % 10
        tong_lap_phuong += chu_so ** 3
        n = n // 10
    return tong_lap_phuong

n= int(input("nhập vào một số:"))
ket_qua = tong_lap_phuong_cac_chu_so(n)
print(f"Tổng các lập phương của các chữ số của {n} là:", ket_qua)


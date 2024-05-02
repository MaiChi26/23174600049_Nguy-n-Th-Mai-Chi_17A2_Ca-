ten_sinh_vien = input("Nhập tên sinh viên: ")
N = int(input("Nhập vào số nguyên N: "))

tu_dien_lap_phuong = {}
for x in range(1, N + 1):
    tu_dien_lap_phuong[x] = x ** 3

tu_dien_sinh_vien = {ten_sinh_vien: tu_dien_lap_phuong}

print(tu_dien_sinh_vien)

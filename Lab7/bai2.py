sinh_vien = {}

for i in range(1, 11):
    ten = input(f"Nhập tên sinh viên thứ {i}: ")
    diem = float(input(f"Nhập điểm thi của sinh viên thứ {i}: "))
    sinh_vien[ten] = diem

thong_ke = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for ten, diem in sinh_vien.items():
    if diem < 4.0:
        loai = 'F'
    elif diem < 5.5:
        loai = 'D'
    elif diem < 7.0:
        loai = 'C'
    elif diem < 8.5:
        loai = 'B'
    else:
        loai = 'A'
    
    thong_ke[loai] += 1

    
    print(f"Sinh viên {ten} có điểm {diem} được xếp loại {loai}.")

print("Thống kê số lượng sinh viên theo loại học lực:")
for loai, so_luong in thong_ke.items():
    print(f"{loai}: {so_luong} sinh viên")

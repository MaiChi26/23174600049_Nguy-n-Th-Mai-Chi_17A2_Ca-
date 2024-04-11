
str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

chuoi_str1 = set(str1[i:j] for i in range(len(str1)) for j in range(i + 1, len(str1) + 1))
chuoi_str2 = set(str2[i:j] for i in range(len(str2)) for j in range(i + 1, len(str2) + 1))

chuoi_con_chung = chuoi_str1.intersection(chuoi_str2)
if chuoi_con_chung:
    chuoi_con_chung_ngan_nhat = min(chuoi_con_chung, key=len)
    print(f"Chuỗi ký tự con chung có độ dài ngắn nhất: {chuoi_con_chung_ngan_nhat}")
else:
    print("Không có chuỗi ký tự con chung.")
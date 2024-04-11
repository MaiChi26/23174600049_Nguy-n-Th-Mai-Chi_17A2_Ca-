
chuoi = input("Nhập vào một chuỗi văn bản: ")
ky_tu_dac_biet = {}
tong_chieu_dai = len(chuoi)

for char in chuoi:
    if not char.isalnum():
        if char in ky_tu_dac_biet:
            ky_tu_dac_biet[char] += 1
        else:
            ky_tu_dac_biet[char] = 1
print("Số lần xuất hiện và tỷ lệ phần trăm của từng ký tự đặc biệt trong chuỗi:")
for char, count in ky_tu_dac_biet.items():
    so_phan_tram = (count / tong_chieu_dai) * 100
    print(f"Ký tự '{char}' xuất hiện {count} lần, chiếm {so_phan_tram:.2f}% của chuỗi.")

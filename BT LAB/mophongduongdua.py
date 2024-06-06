import csv
import random

# Thiết lập thông số cuộc đua
so_ngua = 5
do_dai_duong_dua = 500
ngua = {
    1: {'xac_suat': 0.2, 'khoang_cach': 0},
    2: {'xac_suat': 0.3, 'khoang_cach': 0},
    3: {'xac_suat': 0.1, 'khoang_cach': 0},
    4: {'xac_suat': 0.4, 'khoang_cach': 0},
    5: {'xac_suat': 0.25, 'khoang_cach': 0}
}

# Mô phỏng cuộc đua
ngua_ve_dich = []
vi_tri = 1

while len(ngua_ve_dich) < so_ngua:
    for ma_ngua, du_lieu_ngua in ngua.items():
        if ma_ngua not in ngua_ve_dich:
            di_chuyen = random.uniform(0, du_lieu_ngua['xac_suat'])
            du_lieu_ngua['khoang_cach'] += di_chuyen
            if du_lieu_ngua['khoang_cach'] >= do_dai_duong_dua:
                du_lieu_ngua['khoang_cach'] = do_dai_duong_dua
                ngua_ve_dich.append(ma_ngua)
                du_lieu_ngua['vi_tri'] = vi_tri
                vi_tri += 1

# Ghi kết quả vào file CSV
ten_file_csv = 'ket_qua_dua_ngua.csv'
with open(ten_file_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Vi tri', 'Ma ngua', 'Khoang cach di chuyen'])
    for ma_ngua, du_lieu_ngua in sorted(ngua.items(), key=lambda item: item[1].get('vi_tri', float('inf'))):
        writer.writerow([du_lieu_ngua.get('vi_tri', ''), ma_ngua, du_lieu_ngua['khoang_cach']])

# Hiển thị kết quả
for ma_ngua, du_lieu_ngua in sorted(ngua.items(), key=lambda item: item[1].get('vi_tri', float('inf'))):
    print(f"Vi tri: {du_lieu_ngua.get('vi_tri', '')}, Ma ngua: {ma_ngua}, Khoang cach di chuyen: {du_lieu_ngua['khoang_cach']}")

print(f"Ket qua da duoc luu vao file {ten_file_csv}")

str = input("Nhập vào một chuỗi văn bản: ")
tu_can_tim = input("Nhập vào từ cần tìm kiếm: ")

# Tìm vị trí của từ trong chuỗi
vi_tri = str.find(tu_can_tim)
if vi_tri != -1:
    print(f"Vị trí của từ '{tu_can_tim}' trong chuỗi: {vi_tri}")
else:
    print(f"Từ '{tu_can_tim}' không xuất hiện trong chuỗi.")

words = str.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

tu_tim_nhieu_nhat = max(word_count, key=word_count.get)
max_count = word_count[tu_tim_nhieu_nhat]

print(f"Từ xuất hiện nhiều nhất là '{tu_tim_nhieu_nhat}' với {max_count} lần xuất hiện.")

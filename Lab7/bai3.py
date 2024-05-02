# Văn bản đầu vào
van_ban = "My house is small but beautiful. It has three rooms, a kitchen, toilets and a small veranda. It is three sides open. All rooms are very well ventilated. We are five members in the house. I share my room with my younger brother. House provides us privacy and safety. I love my house very much."
van_ban = van_ban.lower()

import string
van_ban = van_ban.translate(str.maketrans('', '', string.punctuation))

tu_list = van_ban.split()

tu_dien = {}

for tu in tu_list:
    if tu in tu_dien:
        tu_dien[tu] += 1
    else:
        tu_dien[tu] = 1

# Tìm từ xuất hiện nhiều nhất và ít nhất
max_tu = None
min_tu = None
max_count = 0
min_count = float('inf')

for tu, count in tu_dien.items():
    if count > max_count:
        max_count = count
        max_tu = tu
    if count < min_count:
        min_count = count
        min_tu = tu

print(f"Từ xuất hiện nhiều nhất là '{max_tu}' với {max_count} lần.")
print(f"Từ xuất hiện ít nhất là '{min_tu}' với {min_count} lần.")

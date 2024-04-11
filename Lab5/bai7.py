str = input("nhập vào một chuỗi:")

upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

for char in str:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print("Số lượng chữ hoa:", upper_count)
print("Số lượng chữ thường:", lower_count)
print("Số lượng chữ số:", digit_count)
print("Số lượng ký tự đặc biệt:", special_count)
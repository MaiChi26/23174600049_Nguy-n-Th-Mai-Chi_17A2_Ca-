str = input("nhập vào một chuỗi có 10 ký tự: ")

if len(str) > 10:
    # a) Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8
    chuoi_a = str[1:8]  # Python indexing starts at 0
    print("Chuỗi từ vị trí thứ 2 đến vị trí thứ 8:", chuoi_a)
    
    # b) Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5
    chuoi_b = str[4:9]  # Start at index 4, end at index 9
    print("Chuỗi gồm 5 ký tự từ vị trí thứ 5:", chuoi_b)
    
    # c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự
    chuoi_c = str[-3:]  # Lấy 3 ký tự cuối cùng
    print("Chuỗi gồm 3 ký tự cuối:", chuoi_c)
    
    # d) Chuyển đổi chuỗi thành chữ thường
    lower_string = str.lower()
    print("Chuỗi chuyển thành chữ thường:", lower_string)
    
    # e) Chuyển đổi chuỗi thành chữ hoa
    upper_string = str.upper()
    print("Chuỗi chuyển thành chữ hoa:", upper_string)
    
    # f) Đảo ngược chuỗi
    reversed_string = str[::-1]
    print("Chuỗi đảo ngược:", reversed_string)
else:
    print("Chuỗi phải dài hơn 10 ký tự!!!")
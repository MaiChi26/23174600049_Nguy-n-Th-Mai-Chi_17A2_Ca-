str1= input("nhập vào một chuỗi:")
str2= input("nhập vào một chuối:")
ket_hop = ""
i=0
len1= len(str1)
len2= len(str2)
while i < len1 or i < len2:
    if i< len1:
        ket_hop +=str1[i] + "-"
    if i< len2:
        ket_hop +=str2[i] + "-"
    i += 1
print("ký tự sau khi trộn theo quy tắc và yêu cầu là:", ket_hop[:-1])
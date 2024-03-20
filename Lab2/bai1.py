a = float(input("nhập giá trị của a:"))
b = float(input("nhập giá trị của b:"))
if a == 0 and b==0:
    print("phương trình có vô số nghiệm!!!")
elif a == 0  and b!=0:
    print("phương trình vô nghiệm!!!")
else:
    x= -b/a
    print("phương trình có nghiệm duy nhất: x = {}".format(x))
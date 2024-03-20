a, b = map(float, input("Nhập hệ số góc và hệ số tự do của đường thẳng thứ nhất: ").split()) #y = ax + b
x, y = map(float, input("Nhập tọa độ tâm của đường tròn (x , y): ").split())
r = float(input("Nhập bán kính của đường tròn: "))
d = abs(a*x -y +b) / ((a**2 + 1)**0.5) 
if d < r:
    print("Đường thẳng cắt đường tròn.")
elif d == r:
    print("Đường thẳng tiếp xúc đường tròn.")
elif d > r:
    print("Đường thẳng nằm ngoài đường tròn.")
else:
    print("Đường thẳng nằm trong đường tròn.")
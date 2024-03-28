n = 7  # Chiều cao của tam giác

for i in range(1, n + 1):
    khoang_trang = n - i
    print(' ' * khoang_trang + '*' * (2*i - 1))
a = 3 # cạnh hình vuông
for i in range(a):
    print(" " * 5, end="")
    print('*' *a)
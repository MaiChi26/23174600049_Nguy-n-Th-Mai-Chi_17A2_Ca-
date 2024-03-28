#câud:
print(f"Các số hoàn hảo nhỏ hơn {500} là:")
for i in range(1,501):
    # Kiểm tra số i có phải là số hoàn hảo không?
    sum = 0 
    for j in range(1,i):
        if i % j == 0:
            sum = sum + j
    if sum == i:
        print(i)
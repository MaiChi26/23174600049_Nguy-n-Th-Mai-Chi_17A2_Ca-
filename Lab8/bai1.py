def so_nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def so_nguyen_to_sinh_doi():
    for num in range(3, 1000, 2): 
        if so_nguyen_to(num) and so_nguyen_to(num + 2):
            print(f"({num}, {num + 2})")


so_nguyen_to_sinh_doi()

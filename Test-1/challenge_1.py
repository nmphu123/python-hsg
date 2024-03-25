# Hàm kiểm tra số phong phú
def is_abundant(n):
    divisor = 1
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor += i + (n // i)
    return divisor > n

# Đọc file input
fi = open('cau1.inp')
a, b = map(int, fi.readline().split())

# Thuật toán xử lý
abundant_count = 0
for i in range(a, b):
    if is_abundant(i):
        abundant_count += 1

# Ghi file output
fo = open('cau1.out','w')
fo.write(str(abundant_count))
fo.close()

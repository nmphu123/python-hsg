# Hàm kiểm tra số nguyên tố
def is_prime(a):
    if(a < 2):
        return False
    for i in range(2, a//2+1):
        if a % i == 0:
            return False
    return True

# Đọc file input
fi = open('cau2.inp')
n = int(fi.readline())
num_list = list(map(int, fi.readline().split()))
fi.close()

# Thuật toán xử lý
prime_count = 0
for i in num_list:
    if is_prime(i): prime_count += 1

# Ghi file output
fo = open('cau2.out','w')
fo.write(str(prime_count))
fo.close()

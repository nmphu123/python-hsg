# Đọc file input
fi = open('cau4.inp')
n, a, b = map(int,fi.readline().split())
fi.close()

# Thuật toán tính chất chia hết số nguyên
step = -1
for i in range(n//b, -1, -1):
    if (n - i*b) % a == 0:
        step = i + ((n - i*b) // a)
    break

# Ghi file output
fo = open('cau4.out','w')
fo.write(str(step))
fo.close()

# Hàm đếm số cặp đôi khiêu vũ
def count_dancing_pairs(n, k, h):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(h[i] - h[j]) == k:
                count += 1
    return count

# Đọc file input
fi = open('cau4.inp')
n, k = map(int, fi.readline().split())
h = map(list, fi.readline().split())
count = count_dancing_pairs(n, k, h)

# Ghi file output
fo = open('cau4.out', 'w')
fo.write(str(count))
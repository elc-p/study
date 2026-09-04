num_list = [7, 1, 4, 2]
n = len(num_list)

def insert_sort(a, n):
    # 1からスタートすることで、0の要素をソート済みと定義
    for i in range(1, n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = v
    return a

print(insert_sort(num_list, n))
def sort(data):
    size = len(data)
    i = 1
    while i < size:
        j = i
        temp = data[j]
        while j > 0 and temp < data[j - 1]:
            data[j] = data[j - 1]
            j -= 1
        data[j] = temp
        i += 1

a = [1,5,8,38,34,-4,-7,-2,56,100]
sort(a)
print(a)
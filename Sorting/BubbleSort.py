def sort(data):
    size = len(data)
    i = 0
    while i < size - 1:
        j = 0
        while j < size - 1 - i:
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            j += 1
        i += 1


data = [1,5,8,34,3,6,83,23]
sort(data)
print(data)
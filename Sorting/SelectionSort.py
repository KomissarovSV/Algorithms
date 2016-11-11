def sort(data):
    size = len(data)
    i = 0
    while i < size - 1:
        j = i + 1
        min = i
        while j < size:
            if data[min] > data[j]:
                min = j
            j += 1
        data[i],data[min] = data[min],data[i]
        i += 1


data = [1,5,8,34,3,6,83,23]
sort(data)
print(data)
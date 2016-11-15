def partition(data,start,end):
    pivot = data[start]
    i = start + 1
    j = end
    while True:
        while data[i] < pivot and i != j:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i >= j:
            break
        data[i],data[j] = data[j],data[i]
    data[start],data[j] = data[j],data[start]
    return j

def sort(data,start = 0,end = None):
    if end is None:
        end = len(data) - 1
    if start >= end:
        return
    pivot = partition(data,start,end)
    sort(data,start,pivot - 1)
    sort(data,pivot + 1,end)


a = [1,5,8,38,34,-4,-7,-2,56,100]
sort(a)
print(a)



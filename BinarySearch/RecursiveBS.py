def search(list,value,start=0,end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1
    mid = int(start + (end - start)/2)
    if list[mid] == value:
        return mid
    elif list[mid] > value:
        return search(list,value,start, mid - 1)
    else:
        return search(list,value,mid + 1,end)


list = [6, 3, 7, 84, 2, 0, 10]

list.sort()
print(list)
print(search(list,7))
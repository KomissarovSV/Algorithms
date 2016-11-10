def search(list,value):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int(low + (high - low)/2)
        if list[mid] == value:
            return mid
        elif list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    if value > list[mid]:
        return -mid - 1
    else:
        return -mid


list = [6,3,7,84,2,0,10]

list.sort()
print(list)
print(search(list,7))
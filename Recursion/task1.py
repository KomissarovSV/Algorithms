def getMax(data,start = 0,end = None):
    if end is None:
        end = len(data) - 1
    if len(data) < 1:
        return None

    if start == end:
        return data[start]
    else:
        max = getMax(data,start + 1,end)
        if data[start] > max:
            return data[start]
        else:
            return max

data = [1,2,3,43,23,65,12,7,10]

print(getMax(data))


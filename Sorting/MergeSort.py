
class Sorting:
    def __init__(self):
        self.buf = []

    def merge(self,data,start,end,mid):
        i = start
        while i <= end:
            self.buf[i] = data[i]
            i += 1
        i = start
        j = mid + 1
        k = start
        while k <= end:
            if i > mid:
                data[k] = self.buf[j]
                j += 1
            elif j > end:
                data[k] = self.buf[i]
                i += 1
            elif  self.buf[i] > self.buf[j]:
                data[k] = self.buf[j]
                j += 1
            else:
                data[k] = self.buf[i]
                i += 1
            k += 1

    def mergeSort(self,data,start,end):
        if end <= start:
            return
        mid = int(start + (end - start)/2)
        self.mergeSort(data,start,mid)
        self.mergeSort(data,mid + 1,end)
        self.merge(data,start,end,mid)

    def sort(self,data):
        self.buf = data.copy()
        self.mergeSort(data,0,len(data) - 1)

s = Sorting()

a = [1,5,8,38,34,-4,-7,-2,56]

s.sort(a)
print(a)
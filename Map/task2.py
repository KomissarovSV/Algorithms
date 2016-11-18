from Map import task1


# Complexity is O(M)
def test(map1,map2):
    for item in map1:
        if map2.get(item) is None:
            return False
    return True


m = 50
n = 70

map1 = task1(m)
map2 = task1(n)

i = 0
while i < m:
    map1.put(i,i)
    i += 1

i = 0
while i < n:
    map2.put(i,i)
    i += 1

print(test(map1,map2))




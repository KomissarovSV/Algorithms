def get_fib(position, cache = None):
    if cache is None:
        cache = {0:0,1:1}
    if cache.get(position) is None:
        number = get_fib(position - 1,cache) + get_fib(position - 2,cache)
        cache[position] = number
    else:
        number = cache.get(position)
    return number

print(get_fib(9))

def digits(number):
    if number < 10:
        return 1
    else:
        return 1 + digits(number/10)

print(digits(15))
print(digits(105))
print(digits(15105))
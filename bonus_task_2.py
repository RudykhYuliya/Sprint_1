def digit_root(num):
    while num >= 10:
        total = 0
        for digit in str(num):
            total += int(digit)
        num = total
    return num

print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))
print(digit_root(5))
print(digit_root(10000000))
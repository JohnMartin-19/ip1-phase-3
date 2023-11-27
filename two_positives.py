def check_two_positive(a, b, c):
    # Convert the numbers to booleans
    a = bool(a)
    b = bool(b)
    c = bool(c)

    return (a and b) or (a and c) or (b and c)

print(check_two_positive(2,-2,3))
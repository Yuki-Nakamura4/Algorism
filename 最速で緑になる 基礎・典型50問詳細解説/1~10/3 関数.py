t = int(input())


def f(x):
    return x**2 + 2 * x + 3  # return文が必要、2xではなく2*xと書く


print(f(f(f(t) + t) + f(f(t))))

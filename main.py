from math import sin, pi


def trpazoidal_method(func, sections):
    a = 0
    b = pi
    h = float(b-a) / sections
    s = 0.5 * (func(a) + func(b))
    for i in range(1, sections):
        s += func(a + i*h)
    integral = h * s
    print('solution = %f' % integral)
    # func(1) is the max value for this function
    error = 0.000002
    # error_but2 = (h**3/12)*sections*func(1)
    max_iter = (pi**3 * 1 / (error*12))**0.5
    print('In order for the error not to exceed %f, the section must be divided into' % error, max_iter, 'sections')


def simpson_method(func, sections):
    a = 0
    b = pi

    if sections % 2 != 0:
        return None
    h = (b-a)/sections
    first = f(a)
    last = f(b)
    x = a
    sum = 0
    for i in range(sections-1):
        x += h
        value = f(x)
        if i % 2 == 0:
            sum += 4 * value
        else:
            sum += 2 * value
    total = (h/3)*(first+sum+last)
    print('solution =', total)

    # f(1) is the max value for this function
    error = 1/180 * h**4 * (b-a) * func(1)
    print('error =', error)


f = lambda x: sin(x)


print("######trpazoidal method######")
trpazoidal_method(f, 4)
print("######simpson method######")
simpson_method(f, 4)


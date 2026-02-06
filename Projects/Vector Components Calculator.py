# I use 'k' as a variable for the solution of any function
# I use 'i' for iteration

vector_magnitude = float(input("Please Enter the Vector's Magnitude: "))
vector_angle = float(input("Please Enter the Vector's Angle: "))


def factorial(x):
    flag = True
    k = 1
    if x == 0:
        return 1
    while flag:
        k = k * x
        x = x-1
        if x <= 1:
            flag = False
    return k


def taylor_series(x):
    n = 3
    k = x
    i = 10
#Here the loop always adds the 2nd term of the series first so it must be negative
#and since it loops 10 I made it so each time it is even it puts a negative as it is
#in the taylor series of the sin
    while i > 0:
        if i % 2 == 0:
            k -= (x ** n) / (factorial(n))
        elif i % 2 != 0:
            k += (x ** n) / (factorial(n))
        n += 2
        i -= 1
    return k


#converts the given angle from degree to radians
def rad(x):
    pi = 3.14159265359
    r = x * (pi/180)
    return r


def sin(x):
    x = rad(x)
    k = taylor_series(x)
    return k


def cos(x):
    x = 90 - x
    k = sin(x)
    return k


# checks that angle is not greater than 360
flag2 = True
if vector_angle > 360 or vector_angle < 0:
    flag2 = False
    print("The Angle must be between 0 and 360")


#calls trig functions and prints results
if flag2:
    x_component = vector_magnitude * cos(vector_angle)
    y_component = vector_magnitude * sin(vector_angle)
    print("x_component equals: ", round(x_component,3))
    print("y_component equals: ", round(y_component,3))

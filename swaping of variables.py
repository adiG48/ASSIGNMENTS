def without_tem_var(x,y):
    x, y = y, x
    print("x =", x)
    print("y =", y)
def addition_subtraction(x,y):
    x = x + y
    y = x - y
    x = x - y
    print("x =", int(x))
    print("y =", int(y))
def multiplication_division(x,y):
    x = x * y
    y = x / y
    x = x / y
    print("x =", int(x))
    print("y =", int(y))
def exclusive_or(x,y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print("x =", int(x))
    print("y =", int(y))
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
a=int(input("""
what method u choose:
1.without temporary variable
2.Addition and subtracion
3.multiplication and division
4.exclusive OR
ENTER CHOICE AS 1234:
"""))
if a==1:
    without_tem_var(x, y)
elif a==2:
    addition_subtraction(x, y)
elif a==3:
    multiplication_division(x, y)
elif a==4:
    exclusive_or(x, y)
else:
    print("not a valid input")


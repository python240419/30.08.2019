try:
    a = 1
    b = 0
    c = a / b
except FileNotFoundError as a:
    print("----- ERROR:")
    print(a)
    print("------------")
except ArithmeticError:
    print("----- ERROR ZERO")
except Exception as a:
    print("----- ERROR:")
    print(a)
    print("------------")
finally:
    print("are you here?")
print("go on ...")

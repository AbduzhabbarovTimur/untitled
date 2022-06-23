def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return
    return result


try:
    n1 = float(input("a = "))
    n2 = float(input("b = "))
    print(f"a / b = {divide(n1, n2)}")
except ValueError:
    print("Incorrect input value")

